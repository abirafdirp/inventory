inventory.controller('MainController', [
  '$scope', 'BaseItem', function($scope, BaseItem) {
    return $scope.baseitems= BaseItem.get();
  }
]);