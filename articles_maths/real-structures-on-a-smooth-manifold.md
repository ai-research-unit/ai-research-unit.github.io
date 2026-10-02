# __Real Structures on a Smooth Manifold__

## Introduction

A **real structure** on a smooth manifold is a smooth **involution**: a diffeomorphism $\sigma : M \to M$ with $\sigma^2 = \mathrm{id}$. It is the smooth analogue of complex conjugation, and it acts on the whole differential geometry of the manifold — on the functions by $\sigma^*$, on the forms by pullback, on the cohomology, on the metrics and the connections that are invariant under it. The points fixed by $\sigma$ are the **real points**, and the quotient by the involution is the manifold — or orbifold — of orbits. On a complex manifold the compatible involutions are the **antiholomorphic** ones, and their fixed sets are the **real forms**.

The article develops the involutions of a smooth manifold as the involution layer of the group. It defines the real structure, exhibits the classical examples, proves that the set of real points is a closed submanifold by the linearisation of the involution at a fixed point, and describes the quotient and its singularities at the real points. It then develops the induced involution on the algebra of functions and on the graded algebra of forms: the pullback $\sigma^*$ is an algebra automorphism of order two, its $\pm1$-eigenspaces decompose both algebras, and it commutes with the exterior derivative, so it acts on the de Rham cohomology. It treats the structures invariant under $\sigma$ — metric, connection, volume form — which descend to the quotient, and the extension of the differential to the complexified tangent bundle, where the antiholomorphic case and the real forms appear; the antiholomorphic involution of a complex manifold and the geometry of the real forms are *Real Structures on a Complex Manifold* in Part IV.

The article assumes the smooth manifolds, the smooth maps, the differential and the submanifolds of *Smooth Manifolds and Differential Geometry*; the differential forms, the exterior derivative and the de Rham cohomology of *Differential Forms and Stokes' Theorem*; the metric and the Levi-Civita connection of *Hermitian Metrics and the Levi-Civita Connection* and *The Covariant Derivative* in this category; the almost complex structures and the type decomposition of *Hermitian Geometry and Almost Complex Structures* in Part IV; and the quotient manifolds and the group actions of *Foundations of Topology*, *Topology on Groups* and *Lie Groups*. No physics is invoked.

## Involutions of a Smooth Manifold

### Definition and Examples

**Definition.** A **real structure** on a smooth manifold $M$ is a smooth map $\sigma : M \to M$ with $\sigma^2 = \mathrm{id}_M$; equivalently, a smooth action of the group $\mathbb{Z}/2$ on $M$. The **real points** of the real structure are the fixed points, $M^\sigma = \{x \in M : \sigma(x) = x\}$, and a real structure is **free** if $M^\sigma = \emptyset$.

An involution is a diffeomorphism, because $\sigma\circ\sigma=\mathrm{id}$ exhibits $\sigma^{-1}=\sigma$, and its differential is an involution of the tangent bundle: $d\sigma_x : T_xM \to T_{\sigma(x)}M$ and $d\sigma_{\sigma(x)}\circ d\sigma_x = \mathrm{id}$; at a fixed point $d\sigma_x$ is an involution of $T_xM$.

**Examples.** The **antipodal map** $\sigma(x)=-x$ on the sphere $S^n$ is a free involution, and its quotient is the real projective space $\mathbb{RP}^n$. The **complex conjugation** on $\mathbb{C}^n$, $\sigma(z)=\bar z$, is an involution whose real points are $\mathbb{R}^n$, and the conjugation on $\mathbb{CP}^n$ has real points the real projective space $\mathbb{RP}^n = \{[z] : z \in \mathbb{R}^{n+1}\setminus\{0\}\}/\mathbb{R}^*$. On a product $M\times N$ the exchange $\sigma(x,y)=(y,x)$ is an involution with real points the diagonal. The identity is a real structure whose real points are the whole manifold, and the involution of the flat torus $\mathbb{R}^n/\mathbb{Z}^n$ induced by $x\mapsto-x$ has real points the two-torsion points $\{0,1/2\}^n$.

### The Real Points as a Submanifold

**Theorem.** Let $\sigma$ be a real structure on a smooth manifold $M$. Then the set $M^\sigma$ of real points is a closed submanifold of $M$, possibly empty and possibly with components of different dimensions; about every fixed point there is a chart in which $\sigma$ is the linear involution $(x^1,\ldots,x^n) \mapsto (x^1,\ldots,x^p,-x^{p+1},\ldots,-x^n)$ for some $p$, and in that chart $M^\sigma$ is the coordinate subspace $\{x^{p+1}=\cdots=x^n=0\}$.

*Proof.* Choose any Riemannian metric $g$ on $M$ and replace it by $\bar g = \tfrac12(g+\sigma^*g)$, which is again a Riemannian metric, since the average of two positive definite forms is positive definite, and which is invariant: $\sigma^*\bar g = \bar g$. Let $x$ be a fixed point. The differential $d\sigma_x$ is an involution of $T_xM$, so it is diagonalisable with eigenvalues $+1$ and $-1$, and $T_xM = V_+\oplus V_-$ accordingly. The exponential map of the invariant metric at $x$ is equivariant for the involution, $\sigma(\exp_x v) = \exp_x(d\sigma_x v)$, because the geodesics are transported to geodesics and the metric is invariant; hence in the normal coordinates it defines, $\sigma$ is the linear involution with the $+1$ eigenspace $V_+$ and the $-1$ eigenspace $V_-$, and $M^\sigma$ is locally $\exp_x(V_+)$, a submanifold of dimension $p=\dim V_+$. The argument is local about each fixed point, and the union of the local pieces is the closed set $M^\sigma$; being closed and locally a submanifold, it is a closed submanifold. The dimensions of the different components can differ, because the dimension of $V_+$ may vary with the component.

### The Quotient

**Proposition.** The quotient $M/\sigma$ of $M$ by the involution carries a unique smooth structure making the projection $\pi : M \to M/\sigma$ a smooth map, in the following sense: if $\sigma$ is free, $M/\sigma$ is a smooth manifold of the same dimension and $\pi$ is a local diffeomorphism; if $\sigma$ has real points, $M/\sigma$ is a smooth orbifold whose singular points are the images of the real points, and away from them it is a manifold.

*Proof.* The action is by diffeomorphisms, so the quotient of a manifold by a free proper action of a discrete group is a manifold with $\pi$ a local diffeomorphism; this is the quotient-manifold theorem of *Foundations of Topology* and *Topology on Groups*. At a fixed point the model is the quotient of $\mathbb{R}^n$ by the linear involution of the previous theorem, which is the orbifold chart $\mathbb{R}^p\times(\mathbb{R}^{n-p}/(\pm1))$; the resulting structure is an orbifold, as in the orbifold theory of *Geometric Topology* in Part II.

## The Induced Involution on Functions and Forms

### The Pullback Involution

**Definition.** The **induced involution** on the algebra of functions is the pullback

$$
\sigma^* : C^\infty(M) \longrightarrow C^\infty(M), \qquad \sigma^*f = f\circ\sigma,
$$

and the induced involution on the forms is the pullback $\sigma^* : \Omega^k(M)\to\Omega^k(M)$. Both are $\mathbb{R}$-linear and multiplicative, and $(\sigma^*)^2=\mathrm{id}$ because $\sigma^2=\mathrm{id}$.

**Proposition.** The pullback is an algebra automorphism of order two of each of the algebras $C^\infty(M)$ and $\Omega^\bullet(M)$; it commutes with the exterior derivative, $\sigma^*d = d\sigma^*$; it preserves the wedge product; and it respects the grading of the forms. Hence it acts on the de Rham cohomology, $[\sigma^*]$ on $H^k_{dR}(M)$, and the induced action is again of order two.

*Proof.* The pullback along any smooth map is a multiplicative $\mathbb{R}$-linear map, and it composes as $(F\circ G)^*=G^*F^*$, so $\sigma^*\sigma^* = (\sigma\circ\sigma)^*=\mathrm{id}$. The commutation with $d$ is the naturality of the exterior derivative under pullback, $\sigma^*d=d\sigma^*$, of *Differential Forms and Stokes' Theorem*; the preservation of the grading is the definition of the pullback on $k$-forms; the action on cohomology is the standard fact that a cochain map induces a map on cohomology, and it is again an involution.

### The Eigenspace Decomposition

**Theorem.** The $\pm1$-eigenspaces of the involution decompose the two algebras, and the decompositions are compatible with the products and the linear structure.

**(a)** Each function $f$ is a sum of its **symmetric** and **antisymmetric** parts, $f = f_+ + f_-$ with $f_\pm = \tfrac12(f \pm \sigma^*f)$ and $\sigma^*f_\pm = \pm f_\pm$; similarly for forms, $\Omega^k(M)=\Omega^k_+(M)\oplus\Omega^k_-(M)$, and the exterior derivative preserves the decomposition, $d\Omega^k_\pm\subseteq\Omega^{k+1}_\pm$.

**(b)** A form is $\sigma$-invariant, $\sigma^*\omega=\omega$, exactly when it is the pullback of a form on the quotient away from the real points, when $\sigma$ is free; the invariant forms form the subalgebra $\Omega^\bullet_+$.

**(c)** The de Rham cohomology decomposes as $H^k_{dR}(M) = H^k_+ \oplus H^k_-$ into the $\pm1$-eigenspaces of $[\sigma^*]$, when the ground field is taken to be $\mathbb{R}$; the invariant classes are the images of the cohomology of the quotient when $\sigma$ is free.

*Proof.* The averaging operator $f\mapsto\tfrac12(f\pm\sigma^*f)$ is the projection onto the eigenspace with eigenvalue $\pm1$, because $(\sigma^*)^2=\mathrm{id}$; the two projections are the standard decomposition. The compatibility with $d$ follows from $\sigma^*d=d\sigma^*$: if $\sigma^*\omega=\pm\omega$, then $\sigma^*(d\omega)=d\sigma^*\omega=\pm d\omega$. The descent of an invariant form to the quotient is the standard property of the pullback along a covering map: a form on $M$ is the pullback of a form on $M/\sigma$ if and only if it is invariant under the deck transformation $\sigma$, and this is the construction of the forms on the quotient; the statement on cohomology follows because the pullback $\pi^*$ is injective. The decomposition of the cohomology is the functoriality of the cohomology under the automorphism $\sigma^*$ and the fact that a finite-order automorphism is diagonalisable when $2$ is invertible in the field.

## Structures Invariant under the Involution

**Proposition.** A Riemannian metric $g$ with $\sigma^*g=g$ is **invariant** under the real structure; it induces a metric on the quotient $M/\sigma$, a Riemannian metric when $\sigma$ is free and an orbifold metric in general, and its Levi-Civita connection is invariant and descends. The volume form of an invariant metric satisfies $\sigma^*\mathrm{vol}_g=\pm\mathrm{vol}_g$, with the sign $+$ when $\sigma$ preserves the orientation and $-$ when it reverses it; when $\sigma$ is orientation-preserving and the quotient is oriented, the volume form descends.

*Proof.* The invariance of the metric is the equation $\sigma^*g=g$; the quotient metric is defined by pushing forward the inner products through the local diffeomorphism $\pi$, which is well defined exactly because the metric is invariant under the ambiguous deck transformation. The Levi-Civita connection is constructed from the metric by the Koszul formula, so an invariant metric has an invariant connection. The sign of the volume form is read from the determinant of $d\sigma$, which is $\pm1$ at every point; the descent follows when the sign is $+$.

**Proposition (the complexified differential).** Suppose $M$ carries an almost complex structure $J$; the differential of the involution extends $\mathbb{C}$-linearly to an involution $d\sigma$ of the complexified tangent bundle $T_{\mathbb{C}}M$. The involution is **holomorphic** if it commutes with $J$, $d\sigma\circ J = J\circ d\sigma$, and **antiholomorphic** if it anticommutes, $d\sigma\circ J = -J\circ d\sigma$. An antiholomorphic involution exchanges the eigenbundles $T^{1,0}$ and $T^{0,1}$; a holomorphic involution preserves them.

*Proof.* The differential is real, so it extends uniquely to a $\mathbb{C}$-linear map of $TM\otimes\mathbb{C}$; the two commutation rules with $J$ are the definitions of holomorphic and antiholomorphic, and the exchange or preservation of the eigenbundles is immediate from either rule applied to the eigenvalue equations $Jv=\pm iv$.

**Remark.** On a complex manifold an antiholomorphic involution is the **real structure** of the complex geometry, and its fixed set — a real submanifold of half the real dimension, when it is nonempty and transverse — is a **real form** of the complex manifold. The classification of the real forms, the real algebraic geometry they define, and the antiholomorphic involutions of a complex manifold are *Real Structures on a Complex Manifold* in Part IV; the present article supplies the smooth involution, its real points, the induced involution on the forms and the descent of the invariant structures, which is the operator-level content that the Part IV article uses.

## Summary

A real structure on a smooth manifold is a smooth involution $\sigma$; its real points $M^\sigma$ form a closed submanifold, and about each real point there is a chart in which $\sigma$ is the linear involution $(x',x'')\mapsto(x',-x'')$, obtained by averaging a metric to make it invariant and using the exponential map. The quotient $M/\sigma$ is a manifold when $\sigma$ is free and an orbifold with the real points as singularities otherwise; the antipodal map on the sphere and the complex conjugation are the classical examples.

The involution acts on the functions and the forms by the pullback $\sigma^*$, an order-two algebra automorphism commuting with the exterior derivative and hence acting on the de Rham cohomology. The $\pm1$-eigenspaces decompose both algebras and the cohomology, the invariant functions are the functions on the quotient, and the invariant forms descend. An invariant metric descends to the quotient together with its Levi-Civita connection, and the volume form descends when the involution is orientation-preserving. On a complex manifold the differential extends to the complexified tangent bundle, and an antiholomorphic involution — one anticommuting with the complex structure — exchanges the type bundles and defines the real forms, the subject of *Real Structures on a Complex Manifold* in Part IV.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma : M \to M$, $\sigma^2 = \mathrm{id}$ | Real structure; a smooth involution of $M$ |
| $M^\sigma = \{x : \sigma(x)=x\}$ | Real points; a closed submanifold |
| $(x',x'')$, $\dim V_+ = p$ | Linear model of $\sigma$ at a fixed point; $M^\sigma$ locally $\{x''=0\}$ |
| $M/\sigma$, $\pi$ | Quotient by the involution; manifold if free, orbifold otherwise |
| $\sigma^*f = f\circ\sigma$, $\sigma^*\omega$ | Induced involution on the functions and the forms |
| $(\sigma^*)^2=\mathrm{id}$, $\sigma^*d=d\sigma^*$ | Order two; commutation with the exterior derivative |
| $f = f_++f_-$, $\Omega^k = \Omega^k_+\oplus\Omega^k_-$ | $\pm1$-eigenspace decomposition |
| $H^k_{dR}(M) = H^k_+\oplus H^k_-$ | Action on the de Rham cohomology |
| $\sigma^*g = g$ | Invariant metric, descending to the quotient |
| $M/\sigma$ | Quotient; a manifold when free, an orbifold at the real points |
| $d\sigma\circ J = \pm J\circ d\sigma$ | Holomorphic / antiholomorphic extension to $T_{\mathbb{C}}M$ |
| Real form | Fixed set of an antiholomorphic involution; Part IV |

## Further Reading

- John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed. (Springer, 2013), for involutions, the fixed-point submanifold and quotients by group actions.
- Michael Spivak, *A Comprehensive Introduction to Differential Geometry*, vol. I (Publish or Perish, 3rd ed. 1999), for the equivariant normal form at a fixed point and the invariant metric.
- Frank W. Warner, *Foundations of Differentiable Manifolds and Lie Groups* (Springer, 1983), for the induced action on the de Rham cohomology and the descent of invariant forms.
- Klaus Fritzsche and Hans Grauert, *From Holomorphic Functions to Complex Manifolds* (Springer, 2002), for the antiholomorphic involutions and the real forms of a complex manifold.
- Alessio Corti and others, *Real Algebraic Geometry* (lecture notes), for the real points and the real structures in the algebraic setting, cited for the forward reference to Part IV.
