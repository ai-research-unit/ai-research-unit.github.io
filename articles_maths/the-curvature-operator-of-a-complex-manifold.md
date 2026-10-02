
# __The Curvature Operator of a Complex Manifold__

## Introduction

On a complex manifold the curvature operator has a second structure beyond the self-adjointness it has on any Riemannian manifold: the complexified second exterior power splits by type,
$$
\Lambda^2T_pM\otimes\mathbb{C} = \Lambda^{2,0}\oplus\Lambda^{1,1}\oplus\Lambda^{0,2},
$$
and both the complex structure $J$ and the curvature of a Hermitian or Kähler metric act on the three pieces. The curvature of the **Chern connection** — the unique connection of a Hermitian metric whose $(0,1)$-part is the Cauchy–Riemann operator — is a form of type $(1,1)$ with values in $\mathfrak{u}(n)$, so its operator is complex-linear and preserves the type; when the metric is Kähler the Chern connection is the Levi-Civita connection, the type-preservation passes to the Riemannian curvature operator, and the curvature tensor acquires the extra symmetries of a Kähler metric. The readings of the operator that this article develops are the **Chern curvature**, the curvature of the canonical connection of a Hermitian metric with its first Chern form, and the **Kähler curvature**, the curvature of a Kähler metric with its holomorphic sectional curvature, its Ricci form and its Kähler–Einstein condition.

The article has four sections: the curvature operator and the action of the complex structure on bivectors; the Chern curvature and the first Chern form; the Kähler curvature and its symmetries; and the decomposition of the operator by the unitary group. The Riemannian curvature operator, the bivectors, its self-adjointness and its scalar-triple decomposition are *The Curvature Operator*, earlier in this Part, which defers the complex and Hermitian case to this article; the Hermitian metric and the Chern connection are *Hermitian Geometry and Almost Complex Structures* and *Hermitian Metrics and the Levi-Civita Connection*; the Kähler metric and the fundamental form are *Kähler Geometry*, and the closedness of the Kähler form and the Kähler identities are *Kähler Manifolds and the Hermitian Form*, later in this category; the first Chern class and the curvature of a connection are *Characteristic Classes*; the Hodge star splitting of the curvature operator in dimension four is *The Involution on the Curvature Operator*. None of that is re-derived. The particular case of the curvature operator of a Kähler surface and its relation to the invariant decomposition is named and not used.

Throughout, $(M,J,g)$ is a complex manifold of complex dimension $n$ with a Hermitian metric $g$, $T_pM$ is a tangent space with the almost complex structure $J$, $\Lambda^2T_pM\otimes\mathbb C$ is the complexified second exterior power, $\mathcal{R}$ is the Riemannian curvature operator of the metric, $\nabla$ is the Chern connection, $\Theta = \nabla^2$ is its curvature, and $\rho$ is the Ricci form.

## The Curvature Operator and the Complex Structure

**Definition.** On the complexified bivectors the complex structure acts by applying $J$ to each leg, $J(X\wedge Y) = JX\wedge Y + X\wedge JY$, so that the type decomposition
$$
\Lambda^2T_pM\otimes\mathbb C = \Lambda^{2,0}\oplus\Lambda^{1,1}\oplus\Lambda^{0,2}
$$
is the eigenspace decomposition of the induced operator $\mathcal J$ on $\Lambda^2T_pM\otimes\mathbb C$, with eigenvalues $+2i$ on $\Lambda^{2,0}$, $0$ on $\Lambda^{1,1}$ and $-2i$ on $\Lambda^{0,2}$. A complex-linear operator on the second exterior power is one commuting with $\mathcal J$ and hence preserving the type.

**Proposition.** Write $g$ for the Hermitian metric and let $\mathcal{R}$ be its Riemannian curvature operator. If $g$ is Kähler then $\mathcal{R}$ commutes with $\mathcal J$,
$$
[\mathcal R, \mathcal J] = 0 ,
$$
so $\mathcal{R}$ preserves the type of bivectors and decomposes into a Hermitian part on $\Lambda^{1,1}$ and a pair of conjugate parts on $\Lambda^{2,0}$ and $\Lambda^{0,2}$; if $g$ is merely Hermitian the Riemannian curvature operator need not commute with $\mathcal J$, and it is the curvature of the Chern connection that preserves the type.

**Proof.** For a Kähler metric the Levi-Civita connection preserves the complex structure, $\nabla J = 0$; the curvature is the commutator of covariant derivatives, so it commutes with the parallel tensor $J$, and on bivectors this is $[\mathcal R,\mathcal J]=0$. The type of a bivector is its $\mathcal J$-eigenvalue, so commuting with $\mathcal J$ is preserving the type. For a Hermitian metric with $\nabla J\neq0$ the parallel-transport argument fails and the curvature can exchange $\Lambda^{2,0}$ with $\Lambda^{0,2}$; that the Chern curvature is type-preserving is its definition as a $(1,1)$-form with values in $\mathfrak{u}(n)$, below.

**Remark (what the operator records).** The decomposition of the curvature operator by type is the decomposition of the Riemannian curvature into a Hermitian piece and a conjugate pair of pieces, and for a Kähler metric it is a decomposition into three genuinely independent operators; for a Hermitian metric the Riemannian operator has an additional mixed part, measured by $\nabla J$, and the Hermitian structures of this category select the type-preserving part.

## The Chern Curvature

**Definition.** On a Hermitian manifold the **Chern connection** is the unique connection $\nabla$ on $TM$ that is metric for $g$, has $\nabla^{0,1} = \bar\partial$ as its $(0,1)$-part, and satisfies $\nabla J = 0$ in its $(1,1)$-part; its **curvature** is $\Theta = \nabla^2 \in \Omega^{1,1}(\operatorname{End}TM)$, a $(1,1)$-form with values in the skew-Hermitian endomorphisms $\mathfrak{u}(n)$ of each tangent space.

**Proposition (the Chern curvature operator preserves type).** The curvature of the Chern connection is of type $(1,1)$ with values in $\mathfrak u(n)$; its operator $R^{\mathbb C} = \Theta$ on $\Lambda^2T_pM\otimes\mathbb C$ acts as a complex-linear map preserving the bidegree, $R^{\mathbb C}(\Lambda^{p,q})\subseteq\Lambda^{p,q}$, and its action on $\Lambda^{1,1}$ is the Hermitian part of the curvature operator,
$$
\langle R^{\mathbb C}(X\wedge\bar Y), Z\wedge\bar W\rangle = \Theta(X,\bar Y; Z,\bar W) ;
$$
in local holomorphic coordinates the components $R_{i\bar j}{}^{k}{}_{l}$ with
$$
\Theta_{\bar j}{}^{k}{}_{l} = \sum_i R_{i\bar j}{}^{k}{}_{l}\,dz^i
$$
are the Chern curvature coefficients.

**Proof.** A $(1,1)$-form with values in $\mathfrak u(n)$ is complex-linear and lowers the bidegree by at most one in each factor, hence preserves the bidegree of a bivector; the identification with the Hermitian part of the curvature operator is the contraction against the metric on the two legs that the $(1,1)$-form does not carry. The existence and uniqueness of the Chern connection above are *Hermitian Geometry and Almost Complex Structures*.

**Proposition (the first Chern form).** The trace form
$$
c_1(g) = \frac{i}{2\pi}\operatorname{tr}\Theta
$$
is a closed real $(1,1)$-form whose de Rham class is the first Chern class $c_1(M)$, independent of the Hermitian metric; in a holomorphic frame of a line bundle the form is $\frac{i}{2\pi}\partial\bar\partial\log\|s\|^2$, and for the tangent bundle it is the Ricci form of the chosen metric up to a factor.

**Proof.** The trace of a $\mathfrak u(n)$-valued $(1,1)$-form is a real $(1,1)$-form, closed by the Bianchi identity of the connection, and its class is the Chern class by the Chern–Weil construction; the change of a Hermitian metric on a line bundle multiplies a local frame by a positive function, and the difference of two first Chern forms is $\frac{i}{2\pi}\partial\bar\partial\log(f)$, which is exact. The Chern–Weil theory is *Characteristic Classes*.

**Remark (the Ricci form).** For the tangent bundle with the metric $g$ the trace of $\Theta$ in a unitary frame is the **Ricci form**
$$
\rho = i\sum_{j,k}R_{i\bar j k\bar k}\,dz^i\wedge d\bar z^j,
$$
which satisfies $\rho = i\,\partial\bar\partial\log\det(g_{j\bar k})$ and $[\rho] = 2\pi c_1(M)$; this is the precise sense in which the Chern curvature of the tangent bundle is the Ricci curvature read as a $(1,1)$-form.

## The Kähler Curvature

**Definition.** Let $g$ be Kähler. The **Kähler curvature** is the Riemannian curvature tensor read in holomorphic coordinates,
$$
R_{i\bar j k\bar l} = \bigl\langle R(\partial_i,\partial_{\bar j})\partial_k, \partial_{\bar l}\bigr\rangle ,
$$
and it satisfies the three symmetry relations
$$
R_{i\bar j k\bar l} = \overline{R_{j\bar i l\bar k}}, \qquad R_{i\bar j k\bar l} = R_{k\bar l i\bar j}, \qquad R_{i\bar j k\bar l} = R_{i\bar l k\bar j},
$$
the first the reality of the curvature, the second the pair symmetry, and the third equivalent to the Bianchi identity in the Kähler case.

**Proposition (the operator commutes with the complex structure).** For a Kähler metric the curvature operator commutes with $\mathcal J$, its type decomposition is $(2,0)+(1,1)+(0,2)$, and the curvature tensor is determined by its $(1,1)$-components $R_{i\bar j k\bar l}$ alone; the components $R_{i\bar j k\bar l}$ and their conjugates assemble the operator on $\Lambda^{2,0}\oplus\Lambda^{0,2}$, and the operator on $\Lambda^{1,1}$ is the Hermitian part.

**Proof.** The commutation is the previous section. The determination of the tensor by the $(1,1)$-components is the content of the symmetry relation $R_{i\bar j k\bar l}=R_{i\bar l k\bar j}$ together with the Bianchi identity: the $(2,0)$ components $R_{ijkl}$ are the $\partial\bar\partial$-derivatives of $R_{i\bar j k\bar l}$, and for a Kähler metric the tensor is recovered from the mixed components, which is the Kähler case of the Bianchi computation. The Chern connection coincides with the Levi-Civita connection for a Kähler metric, so the Chern curvature and the Kähler curvature are the same object.

**Definition.** For a nonzero holomorphic vector $X$ the **holomorphic sectional curvature** is
$$
H(X) = \frac{R(X, \bar X, X, \bar X)}{g(X,\bar X)^2} ,
$$
and the metric has **constant holomorphic sectional curvature** $c$ when $H$ is the constant $c$ for every $X$; by the Kähler analogue of Schur's theorem, the constancy of $H$ forces the curvature tensor to take the form
$$
R_{i\bar j k\bar l} = \frac{c}{4}\bigl(g_{i\bar j}g_{k\bar l} + g_{i\bar l}g_{k\bar j}\bigr) .
$$

**Proof.** The holomorphic sectional curvature is the sectional curvature of the real two-plane spanned by $X$ and $JX$; if it is constant the second Bianchi identity propagates the constancy, as in Schur's theorem of *Curvature and Geodesics*, and the displayed form is the unique tensor with the symmetries of the Kähler curvature and the constant value $c$. The models are $\mathbb C^n$ with $c=0$, $\mathbb{CP}^n$ with $c>0$ and the complex hyperbolic space with $c<0$, and their classification as the space forms is *Kähler Geometry*.

**Remark (the Ricci form and Kähler–Einstein).** For a Kähler metric the Ricci form is $\rho = i\sum_{j,k}R_{i\bar j k\bar k}dz^i\wedge d\bar z^j$, and it satisfies $\rho = i\,\partial\bar\partial\log\det(g)$ and $[\rho] = 2\pi c_1(M)$; the metric is **Kähler–Einstein** when $\rho = \lambda\,\Omega$ for the Kähler form $\Omega$, equivalently $R_{i\bar j} = \lambda g_{i\bar j}$, and then the scalar curvature is the constant $2n\lambda$. The constant-holomorphic-sectional-curvature metrics are the Kähler–Einstein metrics with the strongest rigidity, and the existence problem for the general Kähler–Einstein metric, and its obstruction, belong to *Kähler Geometry* and beyond.

## The Decomposition by the Unitary Group

**Definition.** The space of algebraic curvature tensors at a point is a representation of the orthogonal group $O(2n)$ and, for a Kähler metric, of the unitary group $U(n)$ acting on the complexified tangent space; an **invariant decomposition** is a decomposition into subrepresentations, and the **irreducible parts** of the curvature operator are the isotypic components.

**Proposition (the unitary decomposition).** For a Kähler metric the space of algebraic curvature tensors decomposes under $U(n)$ into the scalar part, the traceless-Ricci part, the Bochner part and the Weyl part,
$$
\mathcal R = \mathcal R_{\text{scalar}} + \mathcal R_{\text{Ric}} + \mathcal R_{\text{Bochner}} + \mathcal R_{\text{Weyl}} ,
$$
and the first three are determined by the scalar curvature, the traceless Ricci form and the $(2,0)$-part of the curvature, while the Weyl part is the conformally invariant remainder; in complex dimension two the Weyl part splits further by the Hodge star into the self-dual and anti-self-dual halves.

**Proof.** The decomposition is the restriction to $U(n)$ of the $O(2n)$-decomposition of *The Curvature Operator*; the subrepresentations are the scalar, the traceless-Ricci, the Bochner (the $(2,0)$-type part) and the Weyl tensors, and the traceless-Ricci part is the traceless part of the Ricci tensor, the scalar part its trace. The four-dimensional splitting of the Weyl part is *The Involution on the Curvature Operator*. Constant holomorphic sectional curvature is exactly the vanishing of the last three parts, which is the operator form of the classification of the Kähler space forms.

## Summary

On a complex manifold the complexified second exterior power splits into the pieces of type $(2,0)$, $(1,1)$ and $(0,2)$, and the complex structure $\mathcal J$ acts on them with eigenvalues $2i,0,-2i$. The Riemannian curvature operator commutes with $\mathcal J$, $[\mathcal R,\mathcal J]=0$, exactly for a Kähler metric, so that it preserves the type; for a Hermitian metric the type-preserving curvature is that of the Chern connection, a $(1,1)$-form with values in $\mathfrak u(n)$ whose trace $c_1(g)=\frac{i}{2\pi}\operatorname{tr}\Theta$ is the first Chern form, of class $c_1(M)$, and whose contraction is the Ricci form $\rho = i\,\partial\bar\partial\log\det g$ with $[\rho]=2\pi c_1(M)$. For a Kähler metric the Chern connection is the Levi-Civita connection, the curvature tensor satisfies $R_{i\bar j k\bar l}=\overline{R_{j\bar i l\bar k}}=R_{k\bar l i\bar j}=R_{i\bar l k\bar j}$, it is determined by the mixed components, and the holomorphic sectional curvature $H(X)=R(X,\bar X,X,\bar X)/g(X,\bar X)^2$, when constant, forces $R_{i\bar j k\bar l}=\frac{c}{4}(g_{i\bar j}g_{k\bar l}+g_{i\bar l}g_{k\bar j})$ with $\mathbb C^n$, $\mathbb{CP}^n$ and the complex hyperbolic space as the models. Under the unitary group the operator decomposes into the scalar, traceless-Ricci, Bochner and Weyl parts, the Kähler space forms being those with only the scalar part. The Riemannian operator and its $O(2n)$-decomposition are *The Curvature Operator*; the complex and Hermitian structures are *Hermitian Geometry and Almost Complex Structures*, *Hermitian Metrics and the Levi-Civita Connection* and *Kähler Geometry*; the Chern classes are *Characteristic Classes*; the four-dimensional splitting is *The Involution on the Curvature Operator*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Lambda^{2,0}\oplus\Lambda^{1,1}\oplus\Lambda^{0,2}$ | the type decomposition of the complexified bivectors |
| $\mathcal J$ | the complex structure induced on bivectors |
| $\mathcal R$ | the Riemannian curvature operator |
| $\nabla$, $\Theta=\nabla^2$ | the Chern connection and its curvature |
| $R_{i\bar j k\bar l}$ | the Kähler curvature components |
| $\rho=i\,\partial\bar\partial\log\det g$ | the Ricci form, $[\rho]=2\pi c_1(M)$ |
| $H(X)=R(X,\bar X,X,\bar X)/g(X,\bar X)^2$ | holomorphic sectional curvature |
| $\mathcal R=\mathcal R_{\text{scalar}}+\mathcal R_{\text{Ric}}+\mathcal R_{\text{Bochner}}+\mathcal R_{\text{Weyl}}$ | the unitary decomposition |

## Further Reading

- Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry II* (Interscience, 1969), for the Chern connection, the Hermitian and Kähler curvatures and the type decomposition of the curvature.
- Phillip Griffiths and Joseph Harris, *Principles of Algebraic Geometry* (Wiley, 1978), for the Kähler curvature, the Ricci form and the Chern classes.
- Arthur L. Besse, *Einstein Manifolds* (Springer, 1987), for the Kähler–Einstein condition, the holomorphic sectional curvature and the decomposition of the curvature.
- Shiing-Shen Chern, *Complex Manifolds without Potential Theory* (Springer, second edition, 1979), for the Chern connection and the first Chern form.
