from bob.gradiant.pipelines import Pipeline, FeaturesScaleNormalizer, AverageFeatures, RbfSvc


def get_pipeline_average_features_scaled_rbfsvc(name):
    pipeline = Pipeline(name, [AverageFeatures(),
                               FeaturesScaleNormalizer(),
                               RbfSvc(name='RbfSvc')])
    return pipeline


