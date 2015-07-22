var inventoryControllers = angular.module('inventoryControllers', []);

inventoryControllers.controller('BaseItemListCtrl', ['$scope', 'BaseItem',
  function($scope, BaseItem) {
    return $scope.baseitems = BaseItem.get();
  }
]);

inventoryControllers.controller('CategoryListCtrl', ['$scope', 'Category',
  function($scope, Category) {
    return $scope.categories = Category.get();
  }
]);