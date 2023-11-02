# Lecture 15.1: Git Remote Repo | Git 远程仓库  
**通过远程仓库，你可以在工作上进行协作：“undo”撤销操作，“try ideas”尝试想法和“merge”合并工作**  


## 通过远程仓库与他人协作  
远程仓库意味着我们可以与合作者共享我们的工作，Git会跟踪谁做了哪些更改  

### 在团队中使用 Git 需要练习  
- 个人在合作时需要在工作中添加步骤，以避免把他们的项目弄得一团糟  
- 现在就努力学习这个，以后的小组项目就会顺利得多  

### 团队需要工作流（workflow）方法  
当学生开始团队工作时，他们经常与远程工作发生争执。  
- 经常克隆一个仓库，而不是向其中添加更多代码。  
- 读取错误并在网络上查找，以便您了解如何修复和避免它们。  

### 本地和远程仓库需要保持同步  
![Local and remote need to be kept synced](img/15-1-01-Local_and_remote_need_to_be_kept_synced.png)  
一个团队需要：  
- 完成你的工作，然后从远程拉取（pull）更改，  
- 然后进行测试看看哪里出了问题  
- 然后修复团队所做的更改，  
- 然后再次测试，  
- 然后再次从远程拉取以确保是最新的，  
- 只有在所有测试都通过时才推送（push）到远程  

### 敏捷方法（agile method）与 Git 使用的重叠（overlap）  
- 团队需要在代码中确定任务的优先级，并决定谁在做什么，这样重叠的工作就最小化了  
- 使用 GitHub 中的 Issues 来识别任务  
- 使用 [Trello](https://trello.com/) 或 Issues 来跟踪工作/任务  

### 将代码推送到生产环境（production）可以消除关键的产品风险  
使用远程仓库作为“部署”版本，你可以确保代码在其他机器上正常工作  

### 我们可以使用 Git 部署到像 Heroku 这样的远程站点  
参考 [https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true](https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true)  
- 现在先忽略数据库部分，不过我们很快就会这样做  
#### 为什么我们要使用 Heroku ？  
我们可以在自己的系统上运行大型应用程序， Codio 让我们向其他人展示这些应用程序，那么为什么要使用 Heroku 呢？  
主要原因有几个：  
1. 它现在独立于我们的代码库运行，这是可以共享的  
2. 我们可以从一开始就慢慢发展远程应用程序  

### 我们希望主分支保持最新  
我们希望定期将新代码推向生产环境  
- 仅创建少量的分支，经常将它们合并（merge）到主分支，然后删除  