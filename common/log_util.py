import logging
import os

class LogUtil:
    _is_configured = False  # 类变量，用于标记日志是否已经配置
    _log_counters = {}   #类变量，用于维护日志序号

    @staticmethod
    def setup_logging(log_file_name="default.log"):
        if LogUtil._is_configured:
            logging.info("日志配置已存在，跳过重复配置")
            return

        # 确保日志文件路径有效
        log_dir = os.path.dirname(log_file_name)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)

        #创建日志记录器
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)   #设置日志记录器的级别

        #创建文件处理器
        file_handler = logging.FileHandler(log_file_name,encoding="utf-8")
        file_handler.setLevel(logging.INFO)     #设置文件处理器的级别


        #创建控制台处理器
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)       #设置控制台处理器的级别

        #创建日志格式
        log_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s",datefmt="%Y-%m-%d %H:%M:%S")

        #将格式添加到处理器
        file_handler.setFormatter(log_format)
        stream_handler.setFormatter(log_format)

        #将处理器添加到日志记录器
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

        logging.info(f'日志配置完成,日志文件：{log_file_name}')
        LogUtil._is_configured = True #标记日志已经配置


        # # 配置日志
        # logging.basicConfig(
        #     level=logging.INFO,
        #     format="%(asctime)s - %(levelname)s - %(message)s",
        #     handlers=[
        #         logging.FileHandler(log_file_name, encoding='utf-8'),  # 指定文件编码
        #         logging.StreamHandler()  # 同时输出到控制台
        #     ]
        # )
        # logging.info(f"日志配置完成，日志文件: {log_file_name}")
        # LogUtil._is_configured = True  # 标记日志已配置


    def _get_log_message(logger_name,message):
        if logger_name not in LogUtil._log_counters:
            LogUtil._log_counters[logger_name] = 0
        LogUtil._log_counters[logger_name] += 1
        # LogUtil._log_counter += 1  #增加日志序号
        return f"[{LogUtil._log_counters[logger_name]}]{message}"  #返回带序号的日志消息

    @staticmethod
    def info(logger_name,message):
        logging.getLogger(logger_name).info(LogUtil._get_log_message(logger_name,message))

    # @staticmethod
    # def info(message):
    #     logging.info(LogUtil._get_log_message(message))

    @staticmethod
    def error(logger_name,message):
        logging.getLogger(logger_name).error(LogUtil._get_log_message(logger_name,message))
        # logging.error(LogUtil._get_log_message(message))

    @staticmethod
    def debug(logger_name,message):
        logging.getLogger(logger_name).debug(LogUtil._get_log_message(logger_name,message))
        # logging.debug(LogUtil._get_log_message(message))

    @staticmethod
    def warn(logger_name,message):
        logging.getLogger(logger_name).warning(LogUtil._get_log_message(logger_name,message))
        # logging.warning(LogUtil._get_log_message(message))