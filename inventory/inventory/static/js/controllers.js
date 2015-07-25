var inventoryControllers = angular.module('inventoryControllers', []);

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
inventoryControllers.controller('FormValidationCtrl', ['$scope', '$location',
  function($scope, $location) {
    $scope.is_form_validation = $location.url();
  }
]);

