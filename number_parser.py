import os
import re


def get_number(filepath: str) -> str:
    """
    >>> from number_parser import get_number
    >>> get_number("/Users/Guest/AV_Data_Capture/snis-829.mp4")
    'snis-829'
    >>> get_number("/Users/Guest/AV_Data_Capture/snis-829-C.mp4")
    'snis-829'
    >>> get_number("C:¥Users¥Guest¥snis-829.mp4")
    'snis-829'
    >>> get_number("C:¥Users¥Guest¥snis-829-C.mp4")
    'snis-829'
    >>> get_number("./snis-829.mp4")
    'snis-829'
    >>> get_number("./snis-829-C.mp4")
    'snis-829'
    >>> get_number(".¥snis-829.mp4")
    'snis-829'
    >>> get_number(".¥snis-829-C.mp4")
    'snis-829'
    >>> get_number("snis-829.mp4")
    'snis-829'
    >>> get_number("snis-829-C.mp4")
    'snis-829'
    """
    filepath = os.path.basename(filepath)

    if '-' in filepath or '_' in filepath:  # 普通提取番号 主要处理包含减号-和_的番号
        filepath = filepath.replace("_", "-")
        filepath.strip('22-sht.me').strip('-HD').strip('-hd')
        filename = str(re.sub("\[\d{4}-\d{1,2}-\d{1,2}\] - ", "", filepath))  # 去除文件名中时间
        # filepath = filepath.replace("_", "-")
        filepath.strip('22-sht.me').strip('-HD').strip('-hd')
        filename = str(re.sub("\[\d{4}-\d{1,2}-\d{1,2}\] - ", "", filepath))  # 去除文件名中时间
        if 'FC2' or 'fc2' in filename:
            filename = filename.replace('-PPV', '').replace('PPV-', '').replace('FC2PPV-', 'FC2-').replace(
                'FC2PPV_', 'FC2-')
        # file_number = re.search(r'\w+-\w+', filename, re.A).group() #org
        if re.search(r"\d{5,6}.\d{2,3}",filename) and 'h0930' not in filename.lower() and 'h4610' not in filename.lower() and 'c0930' not in filename.lower():
            file_number = re.search(r'\d{5,6}.\d{2,3}', filename, re.A).group()
        else:
            file_number = re.search(r'\w+-\w+', filename.replace('_', '-'), re.A).group()
        return file_number
    else:  # 提取不含减号-的番号，FANZA CID
        try:
            return str(re.findall(r'(.+?)\.', str(re.search('([^<>/\\\\|:""\\*\\?]+)\\.\\w+$', filepath).group()))).strip("['']").replace('_', '-')
        except:
            return re.search(r'(.+?)\.', filepath)[0]
