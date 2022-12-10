getwd()
#setwd("/Users/jaclynm/Library/CloudStorage/OneDrive-SharedLibraries-Zephyr.us/VCU-DAPT\ -\ Documents/004_Projects/02_Altria/SWaM-DATA/DataExploration")

PO_master <- read.csv("../../Tables/PO_master.csv", header = TRUE, stringsAsFactors = FALSE, na.strings = c("null", "NA"))

'''Reformat PO_master'''

colnames(PO_master) <- c("AGENCY_KEY"
                         ,"NIGP_KEY" 
                         ,"VENDOR_KEY" 
                         ,"ITEM_DESC" 
                         ,"ORDER_ID"
                         ,"UNIT_PRICE"
                         ,"UOM_ID"
                         ,"PO_LINE_NUMBER"
                         ,"QUANTITY_ORDERED"
                         ,"TOTAL_COST"
                         ,"TOTAL_COST_CHANGE"
                         ,"MANUFACTURER_PART"
                         ,"ORDER_STATUS"
                         ,"SHIPPING_ADDRESS"
                         ,"DATE_REQUISITION_SUBMITTED"
                         ,"DATE_REQUISITION_APPROVED"
                         ,"DATE_ORDER"
                         ,"DATE_MOST_RECENT_RECEIVING"
                         ,"SWAM_MINORITY"
                         ,"SWAM_WOMAN"
                         ,"SWAM_SMALL"
                         ,"SWAM_MICRO"
                         ,"CATEGORY_DESC"
                         ,"PO_CATEGORY"
                         ,"PROCUREMENT_TRANSACTION_TYPE"
                         ,"ORDER_TYPE"
                         ,"CONTRACT_NO"
                         ,"CONTRACT_TYPE"
)

#PO_master$TOTAL_COST <- format(PO_master$TOTAL_COST, nsmall=2, scientific = FALSE)
#PO_master$TOTAL_COST_CHANGE <- format(PO_master$TOTAL_COST_CHANGE, nsmall=2, scientific = FALSE)
#PO_master$SWAM_MINORITY[is.na(PO_master$SWAM_MINORITY)] <- 0
#PO_master$SWAM_WOMAN[is.na(PO_master$SWAM_WOMAN)] <- 0
#PO_master$SWAM_SMALL[is.na(PO_master$SWAM_SMALL)] <- 0
#PO_master$SWAM_MICRO[is.na(PO_master$SWAM_MICRO)] <- 0
PO_master$DATE_ORDER <- strptime(PO_master$DATE_ORDER, format = "%d-%b-%Y")
PO_master$DATE_ORDER <- as.Date(PO_master$DATE_ORDER, format = "%m/%d/%y")


write.csv(PO_master,"../ToUpload/PO_master.csv", ,na='', row.names = FALSE)
