PO_formatted <- read.csv("../../Outputs/PO_master.csv", header = TRUE, stringsAsFactors = FALSE, na.strings = c("null", "NA"))

#CREATE AND EXPORT A "VENDOR_HAS_SETASIDE" TABLE

myTable = PO_formatted
colnames(myTable)

myTable$SWAM_MINORITY
myTable$SWAM_WOMAN
myTable$SWAM_SMALL
myTable$SWAM_MICRO

vendor_has_minority_cert <- myTable[myTable$SWAM_MINORITY > 0, c("VENDOR_KEY","SWAM_MINORITY")]
vendor_has_minority_cert <- vendor_has_minority_cert[!duplicated(vendor_has_minority_cert), ]
vendor_has_minority_cert$SWAM_MINORITY <- replace(vendor_has_minority_cert$SWAM_MINORITY, vendor_has_minority_cert$SWAM_MINORITY == 1, "Minority-owned")
vendor_has_minority_cert <- vendor_has_minority_cert[rowSums(is.na(vendor_has_minority_cert)) != ncol(vendor_has_minority_cert), ]
colnames(vendor_has_minority_cert)<- c("VENDOR_KEY", "SWAM_CERT")

vendor_has_woman_cert <- myTable[myTable$SWAM_WOMAN > 0, c("VENDOR_KEY","SWAM_WOMAN")]
vendor_has_woman_cert <- vendor_has_woman_cert[!duplicated(vendor_has_woman_cert), ]
vendor_has_woman_cert$SWAM_WOMAN <- replace(vendor_has_woman_cert$SWAM_WOMAN, vendor_has_woman_cert$SWAM_WOMAN == 1, "Woman-owned")
vendor_has_woman_cert <- vendor_has_woman_cert[rowSums(is.na(vendor_has_woman_cert)) != ncol(vendor_has_woman_cert), ]
colnames(vendor_has_woman_cert)<- c("VENDOR_KEY", "SWAM_CERT")

vendor_has_small_cert <- myTable[myTable$SWAM_SMALL > 0, c("VENDOR_KEY","SWAM_SMALL")]
vendor_has_small_cert <- vendor_has_small_cert[!duplicated(vendor_has_small_cert), ]
vendor_has_small_cert$SWAM_SMALL <- replace(vendor_has_small_cert$SWAM_SMALL, vendor_has_small_cert$SWAM_SMALL > 0, "Small Business")
vendor_has_small_cert <- vendor_has_small_cert[rowSums(is.na(vendor_has_small_cert)) != ncol(vendor_has_small_cert), ]
colnames(vendor_has_small_cert)<- c("VENDOR_KEY", "SWAM_CERT")

vendor_has_micro_cert <- myTable[myTable$SWAM_MICRO > 0, c("VENDOR_KEY","SWAM_MICRO")]
vendor_has_micro_cert <- vendor_has_micro_cert[!duplicated(vendor_has_micro_cert), ]
vendor_has_micro_cert$SWAM_MICRO <- replace(vendor_has_micro_cert$SWAM_MICRO, vendor_has_micro_cert$SWAM_MICRO > 0, "Micro Business")
vendor_has_micro_cert <- vendor_has_micro_cert[rowSums(is.na(vendor_has_micro_cert)) != ncol(vendor_has_micro_cert), ]
colnames(vendor_has_micro_cert)<- c("VENDOR_KEY", "SWAM_CERT")

vendor_has_cert <- data.frame()
vendor_has_cert <- rbind(vendor_has_cert, vendor_has_minority_cert)
vendor_has_cert <- rbind(vendor_has_cert, vendor_has_woman_cert)
vendor_has_cert <- rbind(vendor_has_cert, vendor_has_small_cert)
vendor_has_cert <- rbind(vendor_has_cert, vendor_has_micro_cert)
write.csv(vendor_has_cert,"../Tables/VendorHasCerts.csv", ,na='', row.names = FALSE)
