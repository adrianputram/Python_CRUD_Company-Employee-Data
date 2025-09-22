
# Python CRUD Application for Employee Management  

A comprehensive Python application for managing **Employee Data** with Create, Read, Update, and Delete (CRUD) operations.  

---

## Business Understanding  

This project caters to the **Human Resources (HR) / Employee Management** domain, specifically addressing the need to manage **employee data** efficiently. Employee data plays a crucial role in ensuring smooth HR operations and organizational decision-making.  

### Benefits:  
- Improved data accuracy and consistency.  
- Streamlined HR data management processes.  
- Enhanced decision-making through readily available employee information.  
- User-friendly interface for managing employee records.  

### Target Users:  
This application is designed for **HR staff, managers, and administrators** within an organization to facilitate their **HR activities** related to employee records.  

---

## Features  

- **Create**  
  - Add new employee entries with essential details like Employee ID (`No_id`), Name, Position (`Jabatan`), and Department (`Departemen`).  
  - Validation rules to avoid duplicate `No_id`.  

- **Read**  
  - View all employee records in a structured table format.  
  - Search and retrieve employee records by `No_id`.  
  - Display comprehensive employee information in a user-friendly format.  

- **Update**  
  - Modify existing employee data (e.g., name, position, department).  
  - Confirmation required before updating to ensure data integrity.  

- **Delete**  
  - Remove an employee record based on `No_id`.  
  - Confirmation step to prevent accidental deletion.  

- **Reporting**  
  - Generate reports for all employees.  
  - Display specific employee details based on `No_id`.  

---

## Installation  

### 1. Prerequisites  
- Python 3.x installed on your system.  
- No external libraries required (uses only Python built-ins).  

### 2. Installation  
Clone this project or copy the script file into your working directory.  

```bash
git clone https://github.com/<your-username>/employee-crud.git
cd employee-crud
```

### 3. Run the Application  
```bash
python CAPSTONE_1_Data_Karyawan.py
```

---

## Usage  

When you run the script, the main menu will appear:  

1. **Report Data Karyawan**  
   - View all employee records.  
   - Search employee by `No_id`.  

2. **Menambah Data Karyawan**  
   - Add a new employee (requires `No_id`, Name, Position, Department).  

3. **Mengubah Data Karyawan**  
   - Update an employee’s details by selecting `No_id`.  

4. **Menghapus Data Karyawan**  
   - Delete an employee record by `No_id`.  

5. **EXIT**  
   - Exit the program.  

---

## Data Model  

This project uses a **list of dictionaries** in Python to represent employee data.  
Each employee record contains:  

- `No_id` (string) → Unique identifier (e.g., MK01, FN02).  
- `Nama` (string) → Employee name.  
- `Jabatan` (string) → Employee position (e.g., Manager, Supervisor).  
- `Departemen` (string) → Department name (e.g., Marketing, Finance).  

---

## Contributing  

We welcome contributions to this project! Please feel free to fork, submit pull requests, or open issues if you encounter any problems or have suggestions for improvements.  
