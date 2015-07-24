var inventoryControllers = angular.module('inventoryControllers', []);

inventoryControllers.controller('BaseItemListCtrl', ['$scope', 'BaseItem',
  function($scope, BaseItem) {
    return $scope.baseitems = BaseItem.query();
  }
]);

inventoryControllers.controller('CategoryListCtrl', ['$scope', 'Category',
  function($scope, Category) {
    return $scope.categories = Category.query();
  }
]);

inventoryControllers.controller('BrandListCtrl', ['$scope', 'Brand',
  function($scope, Brand) {
    return $scope.brands = Brand.query();
  }
]);

inventoryControllers.controller('ItemListCtrl', ['$scope', 'Item',
  function($scope, Item) {
    return $scope.items = Item.query();
  }
]);
