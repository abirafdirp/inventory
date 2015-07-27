var inventoryControllers = angular.module('inventoryControllers', []);

inventoryControllers.controller('NavCtrl', ['$scope', '$route',
  function($scope, $route) {
    $scope.$route = $route;
  }
]);

inventoryControllers.controller('BaseItemListCtrl', ['$scope', 'BaseItem',
  function($scope, BaseItem) {
    $scope.baseitems = BaseItem.query();
    $scope.title = 'Create Base Item';
  }
]);

inventoryControllers.controller('BaseItemEditCtrl', ['$scope',
  function($scope) {
    $scope.title = 'Edit Base Item';
  }
]);

inventoryControllers.controller('CategoryListCtrl', ['$scope', 'Category',
  function($scope, Category) {
    $scope.categories = Category.query();
    $scope.title = 'Create Category';
  }
]);

inventoryControllers.controller('CategoryEditCtrl', ['$scope',
  function($scope) {
    $scope.title = 'Edit Category';
  }
]);

inventoryControllers.controller('BrandListCtrl', ['$scope', 'Brand',
  function($scope, Brand) {
    $scope.brands = Brand.query();
    $scope.title = 'Create Brand';
  }
]);

inventoryControllers.controller('BrandEditCtrl', ['$scope',
  function($scope) {
    $scope.title = 'Edit Brand';
  }
]);

inventoryControllers.controller('ItemListCtrl', ['$scope', 'Item',
  function($scope, Item) {
    $scope.items = Item.query();
    $scope.title = 'Create Item';
  }
]);

inventoryControllers.controller('ItemEditCtrl', ['$scope',
  function($scope) {
    $scope.title = 'Edit Item';
  }
]);

inventoryControllers.controller('TransactionListCtrl', ['$scope', 'Transaction',
  function($scope, Transaction) {
    $scope.transactions = Transaction.query();
    $scope.title = 'Create Transaction';
  }
]);

inventoryControllers.controller('TransactionEditCtrl', ['$scope',
  function($scope) {
    $scope.title = 'Edit Transaction';
  }
]);

inventoryControllers.controller('LocationListCtrl', ['$scope', 'Location',
  function($scope, Location) {
    $scope.locations = Location.query();
    $scope.title = 'Create Location';
    $scope.items_in_locations = {};
  }
]);

inventoryControllers.controller('LocationEditCtrl', ['$scope', 'Location',
  function($scope, Location) {
    $scope.title = 'Edit Location';
  }
]);

inventoryControllers.controller('ItemsInLocationsCtrl', ['$scope', 'ItemsInLocations',
  function($scope, ItemsInLocation) {
    $scope.items_in_locations = ItemsInLocation.query();
  }
]);

inventoryControllers.controller('FormValidationCtrl', ['$scope', '$location',
  function($scope, $location) {
    $scope.not_form_validation = $location.url();
  }
]);
inventoryControllers.controller('SearchSortPaginationCtrl', ['$scope',
  function($scope) {
    $scope.sort = function(keyname){
        $scope.sortKey = keyname;   //set the sortKey to the param passed
        $scope.reverse = !$scope.reverse; //if true make it false and vice versa
    }
  }
]);
