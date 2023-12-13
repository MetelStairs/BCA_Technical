# main.tf

provider "azurerm" {
  features        = {}
  subscription_id = "<subscription_id>"
  client_id       = "<client_id>"
  client_secret   = "<client_secret>"
  tenant_id       = "<tenant_id>"
}

# Define variables
variable "resource_group_name" {
  description = "The name of the Azure Resource Group"
  default     = "BCA-Dev-Hailstone"
}

variable "location" {
  description = "The Azure region where resources will be created"
  default     = "South UK"
}

variable "acr_name" {
  description = "The name of the Azure Container Registry"
  default     = "bca-acr-dev"
}

variable "az_function_name" {
  description = "The name of the Azure Function"
  default     = "bca-az-function"
}

variable "app_service_plan_name" {
  description = "The name of the app service plan assigned to the function app"
  default = "bca-function-app-service-plan"
}

variable "storage_account_name" {
  description = "The name of the Azure Storage Account"
  default     = "bca-storage-account"
}

# Create a resource group
resource "azurerm_resource_group" "rg" {
  name     = var.resource_group_name
  location = var.location
}

# Create Azure Container Registry
resource "azurerm_container_registry" "acr" {
  name                = var.acr_name
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  sku                 = "Standard"  # You can change this to "Basic" or "Premium" as needed
}

resource azurerm_storage_account "primary" {
  name                     = var.storage_account_name
  resource_group_name      = azurerm_resource_group.primary.name
  location                 = azurerm_resource_group.primary.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource azurerm_app_service_plan "primary" {
  name                = var.app_service_plan_name
  location            = azurerm_resource_group.primary.location
  resource_group_name = azurerm_resource_group.primary.name
  kind                = "FunctionApp"

  sku {
    tier = "Dynamic"
    size = "Y1"
  }
}

resource azurerm_function_app "primary" {
  name                       = var.az_function_name
  resource_group_name        = azurerm_resource_group.primary.name
  location                   = azurerm_resource_group.primary.location

  app_service_plan_id        = azurerm_app_service_plan.primary.id

  storage_account_name       = azurerm_storage_account.primary.name
  storage_account_access_key = azurerm_storage_account.primary.primary_access_key

  os_type                    = "linux"
  version                    = "~3"

  site_config {
    always_on = true
  }
}