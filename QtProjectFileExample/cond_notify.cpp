#include <iostream>
#include <vector>
#include <string>
#include <iostream>
#include <thread>
#include <chrono>
#include <ctime>
#include <cstdlib>
#include <mutex>
#include <condition_variable>
#include <functional>

/*********************************************
多线程测试
在调用别人的sdk时，如果接收到的数据是异步的，
可以在客户端利用多线程的cond wait实现异步转同步
**********************************************/

//------------------------------定时器类----------------------------//
class Timer {
    bool clear = false;

    public:
        void setTimeout(std::function<void()> function, int delay);
        void setInterval(std::function<void()> function, int interval);
        void stop();

};

void Timer::setTimeout(std::function<void()> function, int delay) {
    this->clear = false;
    std::thread t([=]() {
        if(this->clear) return;
        std::this_thread::sleep_for(std::chrono::milliseconds(delay));
        if(this->clear) return;
        function();
    });
    t.detach();
}

void Timer::setInterval(std::function<void()> function, int interval) {
    this->clear = false;
    std::thread t([=]() {
        while(true) {
            if(this->clear) return;
            std::this_thread::sleep_for(std::chrono::milliseconds(interval));
            if(this->clear) return;
            function();
        }
    });
    t.detach();
}

void Timer::stop() {
    this->clear = true;
}

//------------------------------测试类----------------------------//
class ThreadCondTest
{
public:
    static ThreadCondTest* Instance();
    //生产者线程函数
    static void producerThread1();
	static void producerThread2();
	//消费者线程函数
	static void consumerThread();
private:
	static std::vector<std::string> ansy_send_buf_; //异步发送缓冲区
	//线程同步条件变量
	static std::mutex mtx_;
	static std::condition_variable cv_;
	//异步发送线程停止标志
	bool ansy_thread_stop_flag_;
};

//初始化
std::vector<std::string> ThreadCondTest::ansy_send_buf_ = std::vector<std::string>(); //异步发送缓冲区
std::mutex ThreadCondTest::mtx_;
std::condition_variable ThreadCondTest::cv_;

ThreadCondTest* ThreadCondTest::Instance()
{
	static ThreadCondTest object;
	return &object;
}

//生产者1线程函数
void ThreadCondTest::producerThread1()
{
	//获取线程id
	std::thread::id tid = std::this_thread::get_id();
	static Timer t;
	t.setInterval([&](){
		try{
			std::thread::id tidTimer = std::this_thread::get_id();
			//产生随机数
			srand((int)time(NULL));
			int data = rand()%100;
			std::string dataStr = "producerThread1_" + std::to_string(data);
			//std::cout << "tid_producer1:" << tid << "dataStr:" << dataStr << std::endl;
			std::cout << "tid_producer1:" << tidTimer << std::endl;
			std::cout << "dataStr:" << dataStr << std::endl;
			//加锁后将生产的数据写入缓存
			std::unique_lock<std::mutex> locker(mtx_);
			std::cout << "------producer1_1--------" << std::endl;
			ansy_send_buf_.push_back(dataStr);
			std::cout << "------producer1_2--------" << std::endl;
			//通知其它线程，唤醒其它线程的cv_.wait()等待函数
			cv_.notify_all();
		}catch(std::exception){
			std::cout<<"ThreadCondTest::producerThread1 -> exception"<<std::endl;
		}
	}, 1000);
	
	//1000ms超时，结束定时器
	t.setTimeout([&]() {
        std::cout << "Hey.. After 5s. But I will stop the timer!" << std::endl;
		ThreadCondTest::Instance()->ansy_thread_stop_flag_ = true;
        t.stop();
    }, 5000); 
}

//生产者2线程函数
void ThreadCondTest::producerThread2()
{
	std::thread::id tid = std::this_thread::get_id();
	static Timer t;
	t.setInterval([&](){
		try{
			std::thread::id tidTimer = std::this_thread::get_id();
			srand((int)time(NULL));
			int data = rand()%100;
			std::string dataStr = "producerThread2_" + std::to_string(data);
			std::cout << "tid_producer2:" << tidTimer << std::endl;
			std::cout << "dataStr:" << dataStr << std::endl;
			std::unique_lock<std::mutex> locker(mtx_); //加锁
			std::cout << "------producer2_1--------" << std::endl;
			ansy_send_buf_.push_back(dataStr);
			std::cout << "------producer2_2--------" << std::endl;
			cv_.notify_all();
		}catch(std::exception){
			std::cout<<"ThreadCondTest::producerThread1 -> exception"<<std::endl;
		}
		
	}, 1000);
	
	//5000ms超时，结束定时器
	t.setTimeout([&]() {
        std::cout << "Hey.. After 5s. But I will stop the timer!" << std::endl;
		ThreadCondTest::Instance()->ansy_thread_stop_flag_ = true;
        t.stop();
    }, 5000); 
}

//消费者线程函数
void ThreadCondTest::consumerThread()
{
	std::thread::id tid = std::this_thread::get_id();
	std::vector<std::string> ansy_send_buf;
	while(!ThreadCondTest::Instance()->ansy_thread_stop_flag_)
	{
		std::cout << "tid_consumer:" << tid << std::endl;
		do
		{
			std::cout << "------4--------" << std::endl;
			std::unique_lock<std::mutex> locker(mtx_);
			std::cout << "------5--------" << std::endl;
			if(ansy_send_buf_.empty())
			{
				std::cout << "------6--------" << std::endl;
				cv_.wait(locker);
			}
			std::cout << "------7--------" << std::endl;
			ansy_send_buf.clear();
			std::cout << "------8--------" << std::endl;
			ansy_send_buf.swap(ansy_send_buf_);
		}while(0);
		std::cout << "------9--------" << std::endl;
		auto it = ansy_send_buf.begin();
		for(;it != ansy_send_buf.end(); ++it)
		{
			std::cout << "------10--------" << std::endl;
			std::cout << "comsumer receive:" << *it << std::endl;
		}
		//发完就清空
		ansy_send_buf.clear();
		std::this_thread::sleep_for(std::chrono::milliseconds(500));
	}
}

int main()
{
	std::thread producerThread1(ThreadCondTest::producerThread1);
	producerThread1.detach();
	std::thread producerThread2(ThreadCondTest::producerThread2);
	producerThread2.detach();
	std::thread comsumerThread(ThreadCondTest::consumerThread);
	comsumerThread.detach();
	
    getchar();
    return 0;
}
















