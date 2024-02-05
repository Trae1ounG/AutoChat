# AutoChat
[![PyPI version](https://badge.fury.io/py/pyautogen.svg)](https://badge.fury.io/py/pyautogen)
[![Build](https://github.com/microsoft/autogen/actions/workflows/python-package.yml/badge.svg)](https://github.com/microsoft/autogen/actions/workflows/python-package.yml)
![Python Version](https://img.shields.io/badge/3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue)
## 什么是AutoChat？
AutoChat是基于[AutoGen](https://github.com/microsoft/autogen)开发的自定义多角色Agent交流工具，能低成本、方便快捷的实现同多个虚拟世界的角色一同交流。只需要通过定制`characters_xx.json`文件，描述你想交流的角色内容，便可轻松实现和多个角色交谈。现已提供两项对话示例：[《甄嬛传》](https://baike.baidu.com/item/%E7%94%84%E5%AC%9B%E4%BC%A0/4701562?fr=ge_ala)、[《果宝特攻》](https://baike.baidu.com/item/%E6%9E%9C%E5%AE%9D%E7%89%B9%E6%94%BB/9754998?fr=ge_ala)。
## 对话示例
甄嬛传(`chat_with_zhenhuan.py`):
* 皇上（用户）: 传甄嬛该斩！
* 太监: 皇上，臣这就去传旨。
* 甄嬛: 皇上，臣妾这便知罪，愿受皇上处置。
* 皇上（用户）: 华妃你怎么看
* 华妃: 皇上，怜我从良家到深宫，终是一场空，此生无憾，但求一死。
* 皇上（用户）: 又没让你死，你求什么
* 华妃: 皇上，华妃知错，只盼望陛下赐我一个清净之所，让华妃静心悔过。
* 皇上（用户）: 温实初，你说呢
* 温实初: 皇上，臣与嫔妃自幼便是邻居，之间无非是些儿时玩耍之情。至臣入宫后，一直致力于医术，未曾与嫔妃有何私情。若因臣引得嫔妃受累，臣愿以死谢罪。
* 皇上（用户）: 那好，赐甄嬛和温实初死刑
* 甄嬛: 皇上，臣妾与温医生无非是青梅竹马的旧识，与朝堂之事更无半分关联，万望皇上明鉴。

果宝特攻(`chat_with_guobao.py`)：
* 上官子怡（用户）: 橙留香，东方求败来了！
* 东方求败: 果宝特攻，我东方求败已经初步完成了歪教大计！你们也无力阻止！
* 橙留香: 我自横刀向天笑，去留肝胆两昆仑。东方求败，你这歪教大计休想得逞！我橙留香绝不会让你坏了我们的国家！
* 菠萝吹雪: 哈哈哈，东方求败，你以为你能够打败我们果宝特攻的三剑客吗？你小看了我们的实力！
* 陆小果: 我不是随便的人，可我随便起来，不是人。东方求败，你就别得意了！

## 安装
AutoChat 需要 **Python version >= 3.8, < 3.13**. 可以使用简单的pip命令安装`AutoGen`:

```bash
pip install pyautogen
```
如果有额外的库可自行安装。

## 其他
1. 配置API Key，需修改`./OAI_CONFIG_LIST.json`中的`api_key`，填入自己的即可。
2. 运行给定代码示例，仅需执行
```bash
python chat_with_guobao.py
```
3. 自定义聊天对象，仅需新建一个`characters_xx.json`文件，按照要求填入：
* name：角色英文名
* actual_name：角色中文名
* DEFAULT_SYSTEM_MESSAGE：角色默认系统消息
* DEFAULT_DESCRIPTION：不同角色之间交流的描述信息