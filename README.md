# Business-Intelligence
BI 项目的代码, 用来解析 XML 文件然后做相应的处理

依赖的库：
	beautifulsoup4 用来解析xml

BI_classify.py：
	对用户语句的目的，通过是否出现疑问词来做简单的判断。出现疑问词的是数据探索
	
BI_report.py：
	解析“打开报表”相关xml的脚本
	
BI_report_BUSINESS_THEME.py：
	解析“数据探索”相关xml的脚本。使用前需要调试，xml文件中如果有&.*; 这种符号会使beautifulsoup4 解析失败