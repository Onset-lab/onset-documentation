# Infrastructure

This guide provides an overview of the essential IT resources available in the lab.

## 📂 Shared Network Drive (I:\)

Think of the **I:\\** drive as a large, shared storage space that everyone in the lab can access from their computer when connected to the CRCHUM network.

If you cannot see or access the `I:\` drive, please ask Dr. Obaid and Guillaume Theaud to grant you access.

Here is a breakdown of the important folders on this drive:

| Path | Description | Note |
| :--- | :--- | :--- |
| `I:\Chercheurs\Obaid_Sami` | Dr. Obaid's main shared folder. | |
| `I:\Chercheurs\Obaid_Sami\Datasets` | Contains all the shared datasets used in the lab. | **Important:** This is a read-only library. To use a dataset, please copy it to your personal project folder. **Do not edit or move the original files.** |
| `I:\Chercheurs\Obaid_Sami\Projets_Inter_Equipe` | This is where you will store your project data. | New students should create a folder here using their first name (e.g., `Guillaume`). |

For more details, please see the [I:\\ shared folder guide](../data/i_shared_folder.md).

## 📧 Mailing List

We primarily use Discord for our day-to-day communications. However, the mailing list is used to communicate with the entire lab at once. Invitations for lab meetings and other important announcements, such as accepted lab papers, will be sent via this mailing list.

To be added, please ask Guillaume Theaud and provide him with your Google account email address. Once added, you can email the entire lab at `onsetlab@googlegroups.com`.

## 💻 Lab Computers and Operating Systems

Our lab computers run on the Windows Operating System (OS). However, many of the scientific tools we use are designed for another system called Linux. To bridge this gap, we use a few different solutions.

### 🐧 Windows Subsystem for Linux (WSL)

The recommended method is to use the Windows Subsystem for Linux (WSL). This powerful feature lets you run a full Linux environment directly on Windows, without needing to restart your computer.

WSL should already be installed on your lab computer. If it isn't, please contact Guillaume Theaud for assistance.

To install a Linux distribution (we use Ubuntu), open the Windows `PowerShell` application (you can find it in the Start Menu) and type the following command:

```powershell
wsl --install ubuntu-20.04
```

Once inside your Linux environment, you can easily access your Windows files. For example, your `C:\` drive is available at the path `/mnt/c`.

### 🔄 Dual-Boot Systems

Some of our computers are set up with a "dual-boot" system. This means both Windows and Linux are installed separately, and you can choose which one to start when you turn on the computer.

If you are assigned a dual-boot machine, Guillaume Theaud will provide you with a separate username and password for Linux, which are different from your Windows credentials.
