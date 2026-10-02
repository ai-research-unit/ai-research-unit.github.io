
# __Conformal Geometry and the Twistor Operator__

## Introduction

Conformal geometry is the geometry of a metric up to the rescaling of the metric by a positive function, and its natural operators are the conformally **covariant** differential operators: they act on fields of definite **weight** and transform by a power of the conformal factor. The prototype is the Yamabe operator $L=\Delta+\frac{n-2}{4(n-1)}S$ on functions, and the spinor prototype is the **twistor operator** of *The Twistor Operator*, whose kernel is conformally invariant. This article sets the twistor operator in the conformal landscape: the weights, the comparison with the scalar operators of the same weight, and the model of conformal geometry in which the invariance is realised by the action of the conformal group.

The organising statement is that the twistor operator and the Yamabe operator are the first two members of the same family: both are first-order (for the twistor operator) or second-order (for the Yamabe operator) operators built from a connection with a weight correction, both have zero sets that are conformal invariants, and both arise from the same geometric datum, a conformal class. The modern formulation of the family is the tractor calculus and the ambient metric of Fefferman–Graham, where the operators are the restrictions of trivial operators on a bundle over a larger space; this article names the framework and locates the twistor operator in it.

**The boundaries.** The operator, its symbol and its conformal covariance are *The Twistor Operator* and *The Penrose Operator*; the Clifford multiplication and the spin connection are *The Clifford Multiplication Operator* and *The Spinor Operator*; the conformal group, the conformal model of Euclidean space and the conformal compactification are *Conformal Geometry* and *The Conformal Model of Euclidean Space*; the twistor space and the Penrose transform are the sibling `- * Theory` articles. The base is a Riemannian spin manifold $(M,g)$ of dimension $n\ge3$.

## Conformal Weights

**Definition.** A field $\varphi$ of **weight** $w$ with respect to the conformal class $[g]$ is a field that transforms under a conformal change $\hat g=\Omega^2g$ by $\hat\varphi=\Omega^{-w}\varphi$ under the standard identification of the bundles; a conformally covariant operator of weight $w$ and order $k$ is a differential operator $P$ with

$$
P^{\hat g}(\Omega^{-w}\varphi) = \Omega^{-w-k}P^{g}(\varphi) ,
$$

where the powers are those fixed by the normalisations of the bundles.

**Proposition (the weights of the category).** With the normalisation in which a spinor is identified under the conformal change by $\hat\sigma=\Omega^{-1/2}\sigma$:

**(a)** a **function** has weight $0$ and the conformal Laplacian has weight $(n-2)/2$;

**(b)** a **spinor** has weight $1/2$ and the twistor equation is the equation $\mathcal{T}\sigma=0$, which is conformally invariant as a zero set;

**(c)** a **vector field** has weight $0$ and the conformal Killing equation is the corresponding conformally invariant condition on the conformal current.

**Proof.** The first and the third are the standard conformal weights of scalar and vector fields and of the Yamabe equation; the second is the covariance statement of *The Twistor Operator*, quoted with the weight normalisation of this article. The consistency of the three is the table of the next section.

## The Conformally Invariant Operators

**Proposition (the table).** The operators of the category fit into the following table of orders, weights and conformal status:

| Operator | Acts on | Order | Weight | Conformal status |
|---|---|---|---|---|
| Exterior derivative $d$ | forms | $1$ | $0$ | invariant on closed forms |
| Codifferential $d^*$ | forms | $1$ | $n$ | covariant |
| Yamabe operator $L$ | functions | $2$ | $(n-2)/2$ | covariant |
| Cauchy–Riemann $D$ | spinors | $1$ | $n/2$ | not covariant; acquires a zeroth-order term |
| Twistor operator $\mathcal{T}$ | spinors | $1$ | $1/2$ | covariant; zero set invariant |
| Conformal Killing equation | vector fields | $1$ | $0$ | invariant |

The entry for the Cauchy–Riemann operator is the reason the twistor operator exists: the conformally natural first-order spinor operator is not $D$ but the projection of the covariant derivative onto $\ker c$, which is $\mathcal{T}$.

**Proof sketch.** The orders and weights are read from the definitions and from the conformal covariance computations of the references; the non-covariance of $D$ is the computation recorded in *The Spinor Operator*, where a zeroth-order term $c(\operatorname{grad}\log\Omega)$ appears, and the covariance of $\mathcal{T}$ is the cancellation of that term with the trace correction. The table is the operator-theoretic content of the article.

**Remark (the scalar analogue of the twistor equation).** The conformal Killing equation on vector fields is the scalar analogue of the twistor equation on spinors: both express that a distinguished field is in the kernel of a conformally invariant first-order operator, and the current $X_\sigma=\sum_i(\sigma,e_i\cdot\sigma)e_i$ of *The Penrose Operator* sends twistor spinors to conformal Killing fields. The correspondence is the real-geometric face of the conformal invariance.

## The Model and the Group

**Proposition.** In the conformally flat model the twistor operators of the metrics in the class have kernels that are exchanged by the conformal group and that span a $2\dim\Delta_n$-dimensional representation of the conformal Lie algebra; the conformal group of the model is $\mathrm{Spin}(n+1,1)$ (the orientation-preserving part of $O(n+1,1)$), and the twistor spinors are its spinor-valued distribution.

**Proof sketch.** The conformal invariance of the equation and the transitivity of the conformal group make the solution space a representation; the dimension count is *The Penrose Operator*; the identification of the group and its spinor representation is the standard conformal representation theory quoted from *The Conformal Model of Euclidean Space*.

**Remark (the tractor framework).** The modern formulation of the whole table is the **tractor calculus**: on a conformal manifold there is a vector bundle (the tractor bundle) with a connection, and the conformally invariant operators are the operators induced by trivial operators on the tractor bundle; the twistor operator is the spinor member of the family. The framework is named here and developed in the referenced literature; it is the natural home of the table above.

## Worked Cases

### The Round Sphere

On $S^n$ the conformal group is the orthogonal group of the ambient space, the twistor spinors are the sums of the two Killing families, and the Yamabe operator has the constant eigenfunctions of the round Laplacian; the two operators share the quadratic form of the conformal representation theory but are not the same operator.

### The Flat Model

On $\mathbb{R}^n$ the twistor operator has the constants and the linear spinor fields in its kernel, and the conformal Killing fields are generated by the translations, the rotations, the dilation and the special conformal transformations; the table is verified in this model, where the conformal factor of a special conformal transformation is smooth away from the pole.

### A Conformal Compactification

The compactification of flat space is the sphere, and the extension of the flat twistor spinors across the conformal boundary is the conformal invariance of the table made concrete: the equation extends because the operator is covariant, and not because the fields are bounded.

## Summary

Conformal geometry studies the metric up to rescaling, and its natural operators are **conformally covariant**: they act on fields of a definite **weight** and transform by a power of the conformal factor. The **Yamabe operator** $L=\Delta+\frac{n-2}{4(n-1)}S$ on functions of weight $(n-2)/2$ and the **twistor operator** $\mathcal{T}$ on spinors of weight $1/2$ are the two prototypes, with the conformal Killing equation on vector fields completing the family; the **Cauchy–Riemann operator** is not conformally covariant, acquiring a zeroth-order term, and this failure is the reason the twistor operator exists. The table of orders, weights and conformal status is the article's content, and the modern formulation is the **tractor calculus**, the reference framework for the conformally invariant operators. In the conformally flat model the twistor spinors form a $2\dim\Delta_n$-dimensional representation of $\mathrm{Spin}(n+1,1)$, and the conformal current carries twistor spinors to conformal Killing fields. The operator and its symbol are *The Twistor Operator*; the equation and the current are *The Penrose Operator*; the model is *The Conformal Model of Euclidean Space*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\hat g=\Omega^2g$ | Conformal change |
| $\hat\varphi=\Omega^{-w}\varphi$ | Field of conformal weight $w$ |
| $P^{\hat g}(\Omega^{-w}\varphi)=\Omega^{-w-k}P^g\varphi$ | Conformal covariance of order $k$, weight $w$ |
| $L=\Delta+\frac{n-2}{4(n-1)}S$ | Yamabe operator, weight $(n-2)/2$ |
| $D$ | Cauchy–Riemann operator; **not** conformally covariant |
| $\mathcal{T}$ | Twistor operator; conformally covariant, weight $1/2$ |
| $X_\sigma$ | Conformal current; twistor spinors to conformal Killing fields |
| $\mathrm{Spin}(n+1,1)$ | Conformal group of the model |
| Tractor calculus | Framework for the conformally invariant operators |

## Further Reading

- Helga Baum, Thomas Friedrich, Ralf Grunewald and Ines Kath, *Twistors and Killing Spinors on Riemannian Manifolds* (Teubner, 1991), for the twistor operator and its conformal weight.
- Andreas Čap and A. Rod Gover, "Tractor Calculi for Parabolic Geometries", *Transactions of the American Mathematical Society* 354 (2002), 1511–1548, for the tractor framework of the conformally invariant operators.
- Charles Fefferman and C. Robin Graham, *The Ambient Metric* (Princeton University Press, 2012), for the ambient construction and the conformal invariants.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time, Volume 2* (Cambridge University Press, 1986), for the conformal compactification, the conformal group and the conformal Killing spinors.
