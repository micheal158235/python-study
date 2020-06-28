#pragma once

#include <iostream>
#include <string>
#include <vector>
#include <chrono>
#include <thread>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <random>
#include <regex>
#include <time.h>
#ifdef _WIN32
#include <Windows.h>
#include <string.h>
#else
#include <unisted.h>
#include <strings.h>
#endif

#define MAX_PATH 256
using namespace std;

class commonFunc
{
public:
    static std::string GetCrrThreadId()
	{
	    std::stringstream strStream;
		std::thread::id currTdId = std::this_thread::get_id();
		strStream << currTdId;
		return strStream.str();
	}
	//获取当前时间2020-06-24 20:20:20
    static std::string GetCurrTimeStr()
    {
        time_t tick = time(NULL);
    	char buff[32] = {0};
    	strftime(buff, sizeof(buff), "%Y-%m-%d %H:%M:%S", localtime(&tick));
    	std:string str_time = buff;
    	return str_time;
    }
   	//获取当前日期20200624
    static std::string GetDateStr()
    {
        time_t tick = time(NULL);
    	char buff[32] = {0};
    	strftime(buff, sizeof(buff), "%Y%m%d", localtime(&tick));
    	std:string str_time = buff;
    	return str_time;
    }
	//获取时间戳
	static std::time_t GetTimeStamp()
    {
        std::chrono::system_clock::duration d = std::chrono::system_clock::now().time_since_epoch();
    	auto millsec = std::chrono::duration_cast<std::chrono::milliseconds>(d);
    	std::time_t timestamp = millsec.count();
    	return timestamp;
    }
	//带毫秒的13位时间戳时间转为字符串时间2020-06-24 20:20:20.555
    static std::string TimeStamp2String(std::time_t t)
    {
		std::time_t millisec = t%1000;
		std::string dataTimeStr= Datetime2String(t/1000);
        std::string timeStampStr = dataTimeStr + "." + std::to_string(millisec);
    	return timeStampStr;
    }
	//字符串时间2020-06-24 20:20:20转为秒数时间
    static std::time_t String2Datetime(std::string str)
    {
        tm tm_;
    	int year, month, day, hour, minute, second;
    	sscanf(str.c_str(), "%d-%d-%d %d:%d:%d", &year, &month, &day, &hour, &minute, &second);
    	tm_.tm_year = year - 1900;
    	tm_.tm_mon = month - 1;
    	tm_.tm_mday = day;
    	tm_.tm_hour = hour;
    	tm_.tm_min = minute;
    	tm_.tm_sec = second;
    	tm_.tm_isdst = 0;
    	std::time_t t_ = mktime(&tm_);
    	return t_;
    }
	//秒数时间转为字符串时间2020-06-24 20:20:20
    static std::string Datetime2String(std::time_t t)
    {
        char buf[128] = {0};
    	struct tm local = {0};
    	#if defined(_WIN32)
    	localtime_s(&local, &t);
    	#else
    	localtime_r(&t, &local);
    	#endif
    	strftime(buf, 64, "%Y-%m-%d %H:%M:%S", &local);
    	return buf;
    }
	static unsigned int RandomChar() 
	{
        std::random_device rd;
        std::mt19937 gen(rd());
        std::uniform_int_distribution<> dis(0, 255);
        return dis(gen);
    }

    static std::string GenerateHex(const unsigned int len)
	{
        std::stringstream ss;
        for (auto i = 0; i < len; i++) 
	    {
            const auto rc = RandomChar();
            std::stringstream hexstream;
            hexstream << std::hex << rc;
            auto hex = hexstream.str();
            ss << (hex.length() < 2 ? '0' + hex : hex);
        }
        return ss.str();
    }
    //生成GUID
    static std::string CreateGuid()
    {
        return GenerateHex(16);
    }
	//替换所字符串：用dst字符串替换掉src字符串
    static std::string ReplaceAllDistinct(const std::string &str, const std::string &src, const std::string &dst)
    {
        std::string temp = str;
    	if(src == dst)
    	    return temp;
        std::string::size_type pos = temp.find(src);
    	while(pos != std::string::npos)
    	{
    	    temp.replace(pos, src.length(), dst);
    		pos = temp.find(src);
    	}
    	return temp;
    }
	static std::string ReadFileContent(const std::string &filePath)
    {
        std::ifstream fs(filePath);
    	std::stringstream buffer;
    	buffer << fs.rdbuf();
    	std::string contents(buffer.str());
    	return contents;
    }
	//获取运行程序路径
    static std::string GetProgramDir()
	{
	#ifdef _WIN32
	    char exe_full_path[MAX_PATH];
		std::string str_path = "";
		GetModuleFileNameA(NULL, exe_full_path, MAX_PATH);
		str_path = std::string(exe_full_path);
		int pos = str_path.find_last_of('\\', str_path.length());
		return str_path.substr(0, pos);
	#else
	    char abs_path[MAX_PATH];
		int cnt = readlink("/proc/self/exe", abs_path, MAX_PATH);
		if(cnt < 0 || cnt >= MAX_PATH)
		{
		    return "";
		}
		std::string str_path = abs_path;
		int pos = str_path.find_last_of('/', str_path.length());
		return str_path.substr(0, pos);
	#endif
	}
};


int main()
{
    std::cout << "CreateGuid: " << commonFunc::CreateGuid() << std::endl;
	std::cout << "GetCrrThreadId: " << commonFunc::GetCrrThreadId() << std::endl;
	std::cout << "GetCurrTimeStr: " << commonFunc::GetCurrTimeStr() << std::endl;
	std::cout << "GetTimeStamp: " << commonFunc::GetTimeStamp() << std::endl;
	std::cout << "String2Datetime: " << commonFunc::String2Datetime("2020-06-24 20:20:20") << std::endl;
	std::cout << "String2Datetime: " << commonFunc::Datetime2String(std::time_t(1593001220)) << std::endl;
	std::cout << "TimeStamp2String: " << commonFunc::TimeStamp2String(std::time_t(1593311482510)) << std::endl;
	std::cout << "GetProgramDir: " << commonFunc::GetProgramDir() << std::endl;
    getchar();
    return 0;
}


























