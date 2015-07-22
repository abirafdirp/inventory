var baseItemControllers = angular.module('baseItemControllers', []);

baseItemControllers.controller('BaseItemListCtrl', ['$scope', 'BaseItem',
  function($scope, BaseItem) {
    return $scope.baseitems= BaseItem.get();
  }
]);