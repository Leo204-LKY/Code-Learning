# Lecture 14: Git and Versioning | Git 和版本管理  

## 讨论  
- 如果你或你的团队在开发一个项目，你或你们该如何管理源代码？  
    - 尝试新事物，但不要弄乱现有的代码。  
    - 追查一开始出了什么问题。需要一个日志来记录所有相关信息。  
    - 不同的团队成员编辑相同的文件。  

## Version Source Control 版本源代码控制  
- 这是什么？  
    - 也称为 Source Control （源代码控制）  
    - 源代码和项目相关文档变更的管理  
- 为什么我们需要它？  
    - 讨论的结果（_From discussion_）  
    - “what if 如果” 场景  
    - “undo 撤销”场景  

### 源代码控制的种类  
- 本地  
- 服务器，如 SVN  
- 分布式，如 Git 、 Mercurial  

## 每个项目使用一个 Git 仓库  
在自己的文件夹中创建一个新项目，然后在项目中创建一个存储库：  
```Shell
git init
git add .
git commit -m 'initial commit'
```

## Git 基础  
### Git 跟踪文件修改  
Git 是一个版本控制系统，它跟踪存储库中文件的更改  
只要你把文件放入仓库跟踪系统， Git 将知道更改了什么  
Git监视文件，跟踪不同版本文件之间的差异，并存储这些差异——因此它非常轻量级和快速  
它只保留版本之间的差异  

### Git 提供快照（Snapshot）  
- 其他系统跟踪文件中的更改，例如subversion、CVS等  
    ![Other Systems](https://github.com/Leo204-LKY/Code-Learning/assets/57821066/fa9bab8f-4d92-4f8d-a942-e7f6b5ee9507)  
- Git 将数据存储为快照，因此克隆是项目的完整备份  
    ![Git](https://github.com/Leo204-LKY/Code-Learning/assets/57821066/dfbea986-05a5-4f28-a8d4-910db3572f66)  

### Git 有三个操作区域  
![Three areas of operation of Git](https://github.com/Leo204-LKY/Code-Learning/assets/57821066/62542462-812a-4015-80b8-465dcc4aeb63)  
- **Modified** - 已修改，未提交的文件  
- **Staged** - 标记为进入提交快照的修改文件  
- **Committed** - 意味着数据在存储库中  

### 以及四个文件选项  
![Four file status options](https://github.com/Leo204-LKY/Code-Learning/assets/57821066/c33087ba-ebfb-441b-8200-655885d1b455)  
- **Untrack** - 被忽略的文件  
- **Unmodified** - 未修改的文件  
- **Modified** - 已修改，但未进入提交阶段（Stage of commit）的文件  
- **Staged** - 会在下次提交（Commit）中添加的文件  

## Git 基础演示  
- **Git 手册** - https://guides.github.com/introduction/git-handbook/  
- **Git Real** - http://gitreal.codeschool.com/?utm_source=github&utm_medium=codeschool_option&utm_campaign=trygit  
- **Git 工作流**（已失效） - <del>https://www.youtube.com/watch?v=47E-jcuQz5c&index=1&list=PLg7s6cbtAD17Gw5u8644bgKhgRLiJXdX4</del>  

## Git 进阶  
### 你可以从 Staging 中删除项目  
- https://git-scm.com/book/en/v2/Git-Basics-Undoing-Things  
- 用 `reset` 和 `checkout` 从 Stage 中删除更改  
- **注意：** 丢弃的更改不可恢复  

### 回滚提交的修改  
- https://git-scm.com/book/en/v2/Git-Tools-Reset-Demystified  
- 使用 `reset` 来撤销提交
- 硬复位和软复位可以撤销提交（_Hard and Soft resets move you back in commits_）

### Git 允许你创建分支  
- 一个存储库有一个代码的 `master` 分支（主分支），你可以为新的部分创建更多分支(就像树一样)——比如应用程序中的一个新功能  
- 提示：有些地方会使用 `main` 而不是 `master`  

### 你应在工作中使用微提交（Micro-commits）  
- https://www.industriallogic.com/blog/whats-this-about-micro-commits/  
- 当你完成了迈向更大部分的小步骤时，你应该频繁地提交  
- > 在你做的时候把东西保存起来。如果你想要“实验”，那么你可以很容易地知道你可以删除上次提交后的更改  

### 分支很容易被扔掉（toss away）  
- 如果你改变了主意，你可以删除一个分支（branch）——就像砍掉一根树枝（tree branch）一样  
- 让“先尝后买”变得容易  

### 我们也可以合并分支到 `master`  
如果新代码很好地完成了目标，我们可以将其“合并”（merge）到代码的主分支中，从而删除该分支  

### Git 与远程存储库一起工作  
- 确保我们的代码可以在笔记本电脑之外的地方通过远程存储库保存下来  
- 这消除了通过 U 盘小心地将代码复制到其他位置的麻烦，而不会覆盖版本  

### 对远程存储库使用 SSH 密钥  
- 使用公钥和私钥来检查远程仓库，而不是使用登录名  
    - Git 在安装时就已经为你设置好了  
    - 如果没有，参照[这里](http://git-scm.com/book/en/Git-on-the-Server-Generating-Your-SSH-Public-Key)设置  

### 为您的工作创建私有存储库  
- 你可以在 Bitbucket （一个 git 系统）上使用私有仓库  
- 创建账户，然后为每个项目创建一个仓库，以确保您不会损失任何东西  

#### 对**所有**课程作业都使用仓库  
- 自 2019 年以来， GitHub 地免费帐户可以免费使用无限的私人和公共项目(最多三个合作者)。  
    - 而 GitHub 学生账户包含更多内容  
- 你也可以使用 [Bitbucket](https://bitbucket.org/)  

#### 使用公共仓库易使你“被抄袭”  
如果你把你的作品放在公共存储库中，其他人可以复制你的作品，你可能会犯抄袭罪  
**因此，对于课程作业应使用私有仓库**  

#### 将 Git 添加进你的项目  
- 回到正在进行的示例，并在每个示例中创建 Git 存储库  
- 开始使用 Git 存储库(本地和远程)来完成所有的工作  