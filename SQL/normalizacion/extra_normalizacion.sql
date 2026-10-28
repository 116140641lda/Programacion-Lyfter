
PRAGMA foreign_keys = ON;


-- EJERCICIO 1: NORMALIZACION DE EMPLEADOS Y PROYECTOS


-- 1FN:
-- La tabla original ya cumple 1FN porque cada celda contiene un solo valor.




-- 2FN:
-- Separamos Employees y Projects porque sus atributos
-- dependen de una sola parte de la clave compuesta.



-- 3FN:
-- Separamos Departments porque DepartmentPhone depende
-- del departamento y no directamente del empleado.

DROP TABLE IF EXISTS EmployeeProjects;
DROP TABLE IF EXISTS Employees;
DROP TABLE IF EXISTS Projects;
DROP TABLE IF EXISTS Departments;

CREATE TABLE Departments (
    Department TEXT PRIMARY KEY,
    DepartmentPhone TEXT NOT NULL
);

CREATE TABLE Employees (
    EmployeeID INTEGER PRIMARY KEY,
    EmployeeName TEXT NOT NULL,
    Department TEXT NOT NULL,
    FOREIGN KEY (Department)
        REFERENCES Departments(Department)
);

CREATE TABLE Projects (
    ProjectID TEXT PRIMARY KEY,
    ProjectName TEXT NOT NULL,
    ProjectBudget REAL NOT NULL CHECK (ProjectBudget >= 0)
);

CREATE TABLE EmployeeProjects (
    EmployeeID INTEGER NOT NULL,
    ProjectID TEXT NOT NULL,
    PRIMARY KEY (EmployeeID, ProjectID),
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID),
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID)
);

INSERT INTO Departments (Department, DepartmentPhone) VALUES
('IT', '2222-2222'),
('Marketing', '1111-1111');

INSERT INTO Employees (EmployeeID, EmployeeName, Department) VALUES
(201, 'Ana Rivera', 'IT'),
(202, 'Luis Mendez', 'Marketing');

INSERT INTO Projects (ProjectID, ProjectName, ProjectBudget) VALUES
('P001', 'Web App', 50000),
('P002', 'API REST', 25000),
('P003', 'Campaña TV', 30000);

INSERT INTO EmployeeProjects (EmployeeID, ProjectID) VALUES
(201, 'P001'),
(201, 'P002'),
(202, 'P003');


-- =====================================================
-- EJERCICIO 2: NORMALIZACION DE REGISTRO DE CLASES
-- =====================================================

-- 1FN:
-- Cada celda contiene un solo valor.
--
-- 2FN:
-- Separamos Students, Courses y Enrollments para
-- eliminar dependencias parciales de la clave compuesta.
--
-- 3FN:
-- Separamos Instructors porque el correo electronico
-- depende del instructor, no del curso.

DROP TABLE IF EXISTS Enrollments;
DROP TABLE IF EXISTS Courses;
DROP TABLE IF EXISTS Students;
DROP TABLE IF EXISTS Instructors;

CREATE TABLE Students (
    StudentID INTEGER PRIMARY KEY,
    StudentName TEXT NOT NULL
);

CREATE TABLE Instructors (
    InstructorID TEXT PRIMARY KEY,
    InstructorName TEXT NOT NULL,
    InstructorEmail TEXT NOT NULL UNIQUE
);

CREATE TABLE Courses (
    CourseCode TEXT PRIMARY KEY,
    CourseName TEXT NOT NULL,
    InstructorID TEXT NOT NULL,
    FOREIGN KEY (InstructorID)
        REFERENCES Instructors(InstructorID)
);

CREATE TABLE Enrollments (
    StudentID INTEGER NOT NULL,
    CourseCode TEXT NOT NULL,
    PRIMARY KEY (StudentID, CourseCode),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseCode) REFERENCES Courses(CourseCode)
);

INSERT INTO Students (StudentID, StudentName) VALUES
(301, 'Marco Gómez'),
(302, 'Carla Ruiz');

INSERT INTO Instructors
    (InstructorID, InstructorName, InstructorEmail)
VALUES
('I01', 'Juan Pérez', 'juan@uni.edu'),
('I02', 'Laura Rojas', 'laura@uni.edu');

INSERT INTO Courses (CourseCode, CourseName, InstructorID) VALUES
('CS101', 'Python I', 'I01'),
('CS102', 'Python II', 'I02');

INSERT INTO Enrollments (StudentID, CourseCode) VALUES
(301, 'CS101'),
(301, 'CS102'),
(302, 'CS101');


-- =====================================================
-- EJERCICIO 3: NORMALIZACION DE HOSPITAL Y CITAS
-- =====================================================

-- 1FN:
-- Cada cita tiene un identificador y valores atomicos.
--
-- 2FN:
-- La clave AppointmentID es simple, por lo que no existen
-- dependencias parciales de una clave compuesta.
--
-- 3FN:
-- Separamos Patients y Doctors para almacenar los datos
-- del paciente y del medico una sola vez.

DROP TABLE IF EXISTS Appointments;
DROP TABLE IF EXISTS Patients;
DROP TABLE IF EXISTS Doctors;

CREATE TABLE Patients (
    PatientID TEXT PRIMARY KEY,
    PatientName TEXT NOT NULL,
    PatientPhone TEXT NOT NULL
);

CREATE TABLE Doctors (
    DoctorID TEXT PRIMARY KEY,
    DoctorName TEXT NOT NULL,
    Specialty TEXT NOT NULL
);

CREATE TABLE Appointments (
    AppointmentID TEXT PRIMARY KEY,
    PatientID TEXT NOT NULL,
    DoctorID TEXT NOT NULL,
    AppointmentDate TEXT NOT NULL,
    AppointmentTime TEXT NOT NULL,
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
    FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID)
);

INSERT INTO Patients (PatientID, PatientName, PatientPhone) VALUES
('PAT01', 'Diana Vargas', '8888-1111'),
('PAT02', 'Edwin Mora', '8999-2222');

INSERT INTO Doctors (DoctorID, DoctorName, Specialty) VALUES
('DOC01', 'Dr. Soto', 'Pediatría'),
('DOC02', 'Dr. Mora', 'Cardiología');

INSERT INTO Appointments
    (AppointmentID, PatientID, DoctorID, AppointmentDate, AppointmentTime)
VALUES
('A01', 'PAT01', 'DOC01', '2024-08-01', '10:00 AM'),
('A02', 'PAT01', 'DOC01', '2024-08-10', '10:00 AM'),
('A03', 'PAT02', 'DOC02', '2024-08-05', '01:00 PM');


-- =====================================================
-- CONSULTAS PARA VERIFICAR LOS RESULTADOS
-- =====================================================

-- Consulta 1: empleados, departamentos y proyectos
SELECT
    e.EmployeeID,
    e.EmployeeName,
    e.Department,
    d.DepartmentPhone,
    p.ProjectID,
    p.ProjectName,
    p.ProjectBudget
FROM Employees e
JOIN Departments d
    ON e.Department = d.Department
JOIN EmployeeProjects ep
    ON e.EmployeeID = ep.EmployeeID
JOIN Projects p
    ON ep.ProjectID = p.ProjectID
ORDER BY e.EmployeeID, p.ProjectID;

-- Consulta 2: estudiantes, cursos e instructores
SELECT
    s.StudentID,
    s.StudentName,
    c.CourseCode,
    c.CourseName,
    i.InstructorName,
    i.InstructorEmail
FROM Students s
JOIN Enrollments en
    ON s.StudentID = en.StudentID
JOIN Courses c
    ON en.CourseCode = c.CourseCode
JOIN Instructors i
    ON c.InstructorID = i.InstructorID
ORDER BY s.StudentID, c.CourseCode;

-- Consulta 3: citas con datos del paciente y del medico
SELECT
    a.AppointmentID,
    p.PatientName,
    p.PatientPhone,
    d.DoctorName,
    d.Specialty,
    a.AppointmentDate,
    a.AppointmentTime
FROM Appointments a
JOIN Patients p
    ON a.PatientID = p.PatientID
JOIN Doctors d
    ON a.DoctorID = d.DoctorID
ORDER BY a.AppointmentID;

-- Verificar errores de claves foraneas
PRAGMA foreign_key_check;
