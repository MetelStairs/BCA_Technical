# main.tf

provider "azurerm" {
  features        = {}
}

# Define variables
variable "resource_group_name" {
  description = "The name of the Azure Resource Group"
}

variable "location" {
  description = "The Azure region where resources will be created"
}

variable "az_function_name" {
  description = "The name of the Azure Function"
}

variable "app_service_plan_name" {
  description = "The name of the app service plan assigned to the function app"
}

variable "storage_account_name" {
  description = "The name of the Azure Storage Account"
}

# Create a resource group
resource "azurerm_resource_group" "rg" {
  name     = var.resource_group_name
  location = var.location
}

resource azurerm_storage_account "stg_act" {
  name                     = var.storage_account_name
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource azurerm_app_service_plan "app_plan" {
  name                = var.app_service_plan_name
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  kind                = "FunctionApp"

  sku {
    tier = "Dynamic"
    size = "Y1"
  }
}

resource azurerm_function_app "function" {
  name                       = var.az_function_name
  resource_group_name        = azurerm_resource_group.rg.name
  location                   = azurerm_resource_group.rg.location

  app_service_plan_id        = azurerm_app_service_plan.app_plan.id

  storage_account_name       = azurerm_storage_account.stg_act.name
  storage_account_access_key = azurerm_storage_account.stg_act.primary_access_key

  os_type                    = "linux"
  version                    = "~3"

  site_config {
    always_on = true
  }
}