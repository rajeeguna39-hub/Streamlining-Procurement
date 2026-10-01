CREATE TABLE laptop_requests (
  ritm_id VARCHAR(20) PRIMARY KEY,
  emp_id VARCHAR(20),
  model VARCHAR(100),
  status VARCHAR(20),
  po_number VARCHAR(20),
  vendor_name VARCHAR(100)
);
INSERT INTO laptop_requests VALUES ('RITM0010001', 'user1', 'Dell Latitude 5430', 'Approved', 'PO20241001', 'Dell Official');