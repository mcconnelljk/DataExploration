#Merge Contracts Tables

C_16 <- read.csv("../ToMerge/Contracts/VCU_Class_Contract_fis16.csv", header = TRUE, stringsAsFactors = FALSE, na.strings = c("null", "NA"))
C_17 <- read.csv("../ToMerge/Contracts/VCU_Class_Contract_fis17.csv", header = TRUE, stringsAsFactors = FALSE, na.strings = c("null", "NA"))
C_18 <- read.csv("../ToMerge/Contracts/VCU_Class_Contract_fis18.csv", header = TRUE, stringsAsFactors = FALSE, na.strings = c("null", "NA"))
C_19 <- read.csv("../ToMerge/Contracts/VCU_Class_Contract_fis19.csv", header = TRUE, stringsAsFactors = FALSE, na.strings = c("null", "NA"))
C_20 <- read.csv("../ToMerge/Contracts/VCU_Class_Contract_fis20.csv", header = TRUE, stringsAsFactors = FALSE, na.strings = c("null", "NA"))
C_21 <- read.csv("../ToMerge/Contracts/VCU_Class_Contract_fis21.csv", header = TRUE, stringsAsFactors = FALSE, na.strings = c("null", "NA"))

sum(nrow(C_16), nrow(C_17), nrow(C_18), nrow(C_19), nrow(C_20), nrow(C_21))
Contracts_master <- rbind(C_16, C_17, QQ_18, C_19, C_20, C_21)
write.csv(Contracts_master,"../ToMerge/Solicitations_Modern/QQ_master.csv", ,na='', row.names = FALSE)


#Merge PO Tables

PO_16 <- read.csv("../ToMerge/PurchaseOrders/VCU_Class_PO_fis16.csv", header = TRUE, stringsAsFactors = FALSE, na.strings = c("null", "NA"))
PO_17 <- read.csv("../ToMerge/PurchaseOrders/VCU_Class_PO_fis17.csv", header = TRUE, stringsAsFactors = FALSE, na.strings = c("null", "NA"))
PO_18 <- read.csv("../ToMerge/PurchaseOrders/VCU_Class_PO_fis18.csv", header = TRUE, stringsAsFactors = FALSE, na.strings = c("null", "NA"))
PO_19 <- read.csv("../ToMerge/PurchaseOrders/VCU_Class_PO_fis19.csv", header = TRUE, stringsAsFactors = FALSE, na.strings = c("null", "NA"))
PO_20 <- read.csv("../ToMerge/PurchaseOrders/VCU_Class_PO_fis20.csv", header = TRUE, stringsAsFactors = FALSE, na.strings = c("null", "NA"))
PO_21 <- read.csv("../ToMerge/PurchaseOrders/VCU_Class_PO_fis21.csv", header = TRUE, stringsAsFactors = FALSE, na.strings = c("null", "NA"))

sum(nrow(PO_16), nrow(PO_17), nrow(PO_18), nrow(PO_19), nrow(PO_20), nrow(PO_21))
PO_master <- rbind(PO_16, PO_17, PO_18, PO_19, PO_20, PO_21)
write.csv(PO_master,"../ToMerge/Solicitations_Modern/PO_master.csv", ,na='', row.names = FALSE)


#Merge SO Tables

SO_16 <- read.csv("../ToMerge/Solicitations_Legacy/VCU_Class_SO_fis16.csv", header = TRUE, stringsAsFactors = FALSE, na.strings = c("null", "NA"))
SO_17 <- read.csv("../ToMerge/Solicitations_Legacy/VCU_Class_SO_fis17.csv", header = TRUE, stringsAsFactors = FALSE, na.strings = c("null", "NA"))
SO_18 <- read.csv("../ToMerge/Solicitations_Legacy/VCU_Class_SO_fis18.csv", header = TRUE, stringsAsFactors = FALSE, na.strings = c("null", "NA"))
SO_19 <- read.csv("../ToMerge/Solicitations_Legacy/VCU_Class_SO_fis19.csv", header = TRUE, stringsAsFactors = FALSE, na.strings = c("null", "NA"))
SO_20 <- read.csv("../ToMerge/Solicitations_Legacy/VCU_Class_SO_fis20.csv", header = TRUE, stringsAsFactors = FALSE, na.strings = c("null", "NA"))
SO_21 <- read.csv("../ToMerge/Solicitations_Legacy/VCU_Class_SO_fis21.csv", header = TRUE, stringsAsFactors = FALSE, na.strings = c("null", "NA"))

sum(nrow(SO_16), nrow(SO_17), nrow(SO_18), nrow(SO_19), nrow(SO_20), nrow(SO_21))
SO_master <- rbind(SO_16, SO_17, SO_18, SO_19, SO_20, SO_21)
write.csv(SO_master,"../ToMerge/Solicitations_Modern/SO_master.csv", ,na='', row.names = FALSE)


#Merge QQ Tables

QQ_16 <- read.csv("../ToMerge/Solicitations_Modern/VCU_Class_QQ_fis16.csv", header = TRUE, stringsAsFactors = FALSE, na.strings = c("null", "NA"))
QQ_17 <- read.csv("../ToMerge/Solicitations_Modern/VCU_Class_QQ_fis17.csv", header = TRUE, stringsAsFactors = FALSE, na.strings = c("null", "NA"))
QQ_18 <- read.csv("../ToMerge/Solicitations_Modern/VCU_Class_QQ_fis18.csv", header = TRUE, stringsAsFactors = FALSE, na.strings = c("null", "NA"))
QQ_19 <- read.csv("../ToMerge/Solicitations_Modern/VCU_Class_QQ_fis19.csv", header = TRUE, stringsAsFactors = FALSE, na.strings = c("null", "NA"))
QQ_20 <- read.csv("../ToMerge/Solicitations_Modern/VCU_Class_QQ_fis20.csv", header = TRUE, stringsAsFactors = FALSE, na.strings = c("null", "NA"))
QQ_21 <- read.csv("../ToMerge/Solicitations_Modern/VCU_Class_QQ_fis21.csv", header = TRUE, stringsAsFactors = FALSE, na.strings = c("null", "NA"))

sum(nrow(QQ_16), nrow(QQ_17), nrow(QQ_18), nrow(QQ_19), nrow(QQ_20), nrow(QQ_21))
QQ_master <- rbind(QQ_16, QQ_17, QQ_18, QQ_19, QQ_20, QQ_21)
write.csv(QQ_master,"../ToMerge/Solicitations_Modern/QQ_master.csv", ,na='', row.names = FALSE)