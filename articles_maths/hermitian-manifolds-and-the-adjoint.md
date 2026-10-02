# __Hermitian Manifolds and the Adjoint__

## Introduction

On a Hermitian manifold the metric and the complex structure are tied together by the Hermitian condition, and the **adjoint** is the operation that makes the tie visible. The complex structure is **anti-self-adjoint** for the Hermitian pairing, $J^{*} = -J$, because it is an orthogonal operator with $J^2 = -\mathrm{id}$; the Hermitian pairing itself is the complexification of the metric, $\langle X, Y\rangle_{\mathbb{C}} = g(X, \bar Y)$; the **Lefschetz operator** $L$ of wedging with the Kähler form has the **contraction** $\Lambda$ as its adjoint, $L^{*} = \Lambda$; and the **Kähler identities** express the adjoints of $\partial$ and $\bar\partial$ by the commutators with $\Lambda$. The article collects these adjoint relations, which are the operator-theoretic content of the Hermitian structure, and reads the geodesic operator of the preceding articles in this language.

The article develops the adjoint on a Hermitian manifold. It defines the Hermitian pairing of the complexified tangent bundle and proves that the complex structure is anti-self-adjoint and unitary for it, with the consequences for the real and the complex adjoints; it describes the complexified operators, the type decomposition and the adjoint of a type-$(p,q)$ operator; it defines the Lefschetz operator and proves that the contraction is its adjoint, with the Lefschetz decomposition; it states the Kähler identities, the adjoints of $\partial$ and $\bar\partial$, and the resulting identity of the Laplacians; and it reads the self-adjointness of the geodesic operator and the commutation of the conjugations with the adjoint in the Hermitian setting.

The article assumes the Hermitian manifold, the complex structure $J$, the Hermitian metric and the fundamental form from *Hermitian Manifolds and the Geodesic Involution* of this category and *Hermitian Geometry and Almost Complex Structures* in a later category of this Part, where the Kähler condition, the Hodge theory and the Kähler identities are proved; the adjoint and the operator layer from *The Adjoint of the Geodesic Operator* and *Isometric Involutions on the Operator Layer*, the preceding articles of this group. The Kähler identities, the Lefschetz decomposition and the Hodge theory are quoted here and proved there, and the holomorphic side is not developed. No physics is invoked.

## The Metric Adjoint on a Hermitian Manifold

### The Hermitian Pairing

**Definition.** Let $(M, g, J)$ be a Hermitian manifold, $g$ the Riemannian metric and $J$ the complex structure with $J^2 = -\mathrm{id}$ and $g(JX, JY) = g(X, Y)$. The **Hermitian pairing** of the complexified tangent bundle is

$$
\langle X, Y\rangle_{\mathbb{C}} = g(X, \bar Y), \qquad X, Y \in T_{\mathbb{C}}M = TM\otimes\mathbb{C},
$$

where the bar is the conjugation of the complexification; it is $\mathbb{C}$-linear in the first argument, conjugate-symmetric, positive definite, and its real part is the metric extended complex-bilinearly:

$$
\langle X, Y\rangle_{\mathbb{C}} = \overline{\langle Y, X\rangle_{\mathbb{C}}}, \qquad
\operatorname{Re}\langle X, Y\rangle_{\mathbb{C}} = g_{\mathbb{C}}(X, \bar Y), \qquad
\langle X, X\rangle_{\mathbb{C}} \geq 0 .
$$

The **adjoint** $T^{*}$ of a $\mathbb{C}$-linear operator $T$ is defined by $\langle TX, Y\rangle_{\mathbb{C}} = \langle X, T^{*}Y\rangle_{\mathbb{C}}$, and the Hermitian structure is the choice of a complex structure compatible with the metric in this sense.

**Proof.** The real metric extends to a complex-bilinear form on $T_{\mathbb{C}}M$, and the pairing displayed is the composition of that form with the conjugation in the second argument; the conjugate-symmetry and the positive definiteness are immediate from the Riemannian case, and the adjoint is well defined because the pairing is nondegenerate and positive definite.

### The Adjoint of the Complex Structure

**Theorem.** The complex structure is **anti-self-adjoint** for the Riemannian metric and for the Hermitian pairing,

$$
J^{*} = -J, \qquad \langle JX, Y\rangle = -\langle X, JY\rangle, \qquad \langle JX, Y\rangle_{\mathbb{C}} = -\langle X, JY\rangle_{\mathbb{C}},
$$

and it is **unitary** for the Hermitian pairing, $\langle JX, JY\rangle_{\mathbb{C}} = \langle X, Y\rangle_{\mathbb{C}}$. Equivalently, $J$ is an orthogonal operator with $J^2 = -\mathrm{id}$, so its transpose is $-J$ and its inverse is $-J$, and the two facts together give $J^{*} = J^{-1} = -J$. The complex structure is thus a **skew-adjoint** operator of square $-1$: it is the operator-theoretic form of the almost complex structure.

**Proof.** The condition $g(JX, JY) = g(X, Y)$ says that $J$ is orthogonal, $J^{\top}J = \mathrm{id}$; from $J^2 = -\mathrm{id}$ and the orthogonality one gets $J^{\top} = -J$, which is the anti-self-adjointness for the real metric. Passing to the complexification, the conjugation in the second argument turns the real bilinear form into the Hermitian one, and the same identity gives the anti-self-adjointness for $\langle\cdot,\cdot\rangle_{\mathbb{C}}$, while the unitarity is the Hermitian condition itself. The identity $J^{*} = J^{-1} = -J$ is the combination of the two.

**Corollary.** A $\mathbb{C}$-linear operator commuting with $J$ (a **complex-linear** or **holomorphic** operator) has an adjoint commuting with $J$; a $\mathbb{C}$-linear operator anticommuting with $J$ (an **anti-linear** operator in the graded sense) has an adjoint anticommuting with $J$. Consequently the adjoint preserves the two classes, and the conjugation by the complex structure, $T\mapsto JTJ^{-1}$, is compatible with the adjoint operation.

**Proof.** If $TJ = JT$ then taking adjoints gives $J^{*}T^{*} = T^{*}J^{*}$, that is $-JT^{*} = -T^{*}J$ and hence $JT^{*} = T^{*}J$; the anticommuting case is identical with the sign. The last statement is the two cases read together.

## The Complexified Operators

### The Type Decomposition and the Adjoint

**Definition.** The complexification of the tangent bundle splits into the **holomorphic** and the **anti-holomorphic** parts, the $\pm i$-eigenspaces of $J$,

$$
T_{\mathbb{C}}M = T^{1,0}M\oplus T^{0,1}M,
$$

and an operator of **type $(p, q)$** raises the holomorphic degree by $p$ and the anti-holomorphic degree by $q$. The adjoint of an operator of type $(p,q)$ has type $(-p,-q)$ for the Hermitian pairing, because the pairing is conjugate-linear in the second argument and the type is the grading by the eigenvalues of $J$.

**Proposition.** The adjoint of a type-$(p,q)$ operator is of type $(-p,-q)$, the adjoint of the complex-linear part of a real operator is the complex-linear part of its adjoint, and the real adjoint and the complex adjoint agree on the real operators: if $T$ is real, then its $\mathbb{C}$-linear extension has the adjoint $T^{*}$ whose restriction to the real tangent bundle is the real adjoint.

**Proof.** The type is the eigenvalue of the ad $J$ action on the operators, and the adjoint reverses the eigenvalue by the corollary above, so the type changes sign; the complex-linear part is the $(p,q)$-part and the adjoint preserves it; the real statement is the uniqueness of the extension of the real adjoint to the complexification.

### The Lefschetz Operator and Its Adjoint

**Definition.** Let $\omega$ be the **fundamental form** of the Hermitian metric, $\omega(X, Y) = g(JX, Y)$, a two-form of type $(1,1)$; the **Lefschetz operator** is the wedge with $\omega$,

$$
L : \Omega^k(M) \longrightarrow \Omega^{k+2}(M), \qquad L(\alpha) = \omega\wedge\alpha,
$$

and the **contraction operator** is its metric adjoint $\Lambda = L^{*}$, the contraction of a form with the Kähler form, $\Lambda = \star^{-1}\circ L\circ\star$ up to the sign convention of the Hodge star.

**Theorem.** The contraction is the adjoint of the Lefschetz operator for the $L^2$ pairing of the forms,

$$
\Lambda = L^{*}, \qquad \langle L\alpha, \beta\rangle = \langle \alpha, \Lambda\beta\rangle,
$$

and the two operators satisfy the $\mathfrak{sl}_2$ commutation relations of the Lefschetz decomposition,

$$
[\Lambda, L] = (n - k)\,\mathrm{id} \quad \text{on}\ \Omega^k \ \text{of the complex dimension}\ n,
$$

the **Lefschetz decomposition** of the forms into the primitive parts. The metric adjoint of the exterior derivative is the codifferential $\delta = -d^{*} = \star d\star^{-1}$ up to sign, and the Laplacian is $\Delta = d\delta+\delta d$.

**Proof.** The adjoint of the wedge with a fixed form for the metric pairing is the contraction with the metric-dual form, which is the contraction operator; the $\mathfrak{sl}_2$ relations are the classical identities of the Lefschetz decomposition, proved by the computation in an orthonormal basis; the codifferential formula is the standard formula for the adjoint of the exterior derivative with the Hodge star, and the Laplacian identity is then the definition. The details are *Hermitian Geometry and Almost Complex Structures*, where the Kähler case is proved.

## The Kähler Identities

**Theorem (the Kähler identities, quoted from the Hermitian geometry).** On a Kähler manifold the adjoints of the holomorphic and the anti-holomorphic Dolbeault operators are expressed by the commutators with the contraction:

$$
[\Lambda, \partial] = i\,\bar\partial^{*}, \qquad
[\Lambda, \bar\partial] = -i\,\partial^{*},
$$

equivalently

$$
\partial^{*} = -i\,[\Lambda, \bar\partial], \qquad
\bar\partial^{*} = i\,[\Lambda, \partial],
$$

with the conventions of the Dolbeault operators $\partial$ and $\bar\partial$ and the complex structure of the forms. Consequently the Laplacians are equal up to a factor,

$$
\Delta_{\partial} = \Delta_{\bar\partial} = \tfrac12\Delta_d ,
$$

and the harmonic forms decompose by type on a Kähler manifold. The identities, their signs and the Hodge theory that uses them are proved in *Hermitian Geometry and Almost Complex Structures* in a later category of this Part; they are stated here because they are the adjoint relations of the complex structure, which is the subject of the article.

**Proof sketch.** The identities follow from the $\mathfrak{sl}_2$ relations of the Lefschetz operator together with the commutation relations of $\partial$ and $\bar\partial$ with $L$ and $\Lambda$; the equality of the Laplacians is the consequence of the identities and of $\Delta_d = 2\Delta_{\partial}$ on a Kähler manifold. The details are the Kähler theory of the later article.

**Corollary.** The adjoint of the complex structure and the adjoints of the Dolbeault operators are the operator-theoretic face of the Kähler geometry: $J^{*}=-J$ says that the complex structure is skew-adjoint, the Kähler identities say that the adjoint of $\partial$ is the commutator of $\Lambda$ with $\bar\partial$, and the Hodge theorem on a compact Kähler manifold is the spectral statement for the self-adjoint Laplacian.

## The Adjoint and the Involution

**Proposition.** The self-adjointness of the geodesic operator and the commutation of the conjugation with the adjoint of *The Adjoint of the Geodesic Operator* and *Isometric Involutions on the Operator Layer* hold in the Hermitian setting, with the Hermitian pairing replacing the real one where the fields are complexified: the covariant derivative is skew-adjoint, the curvature term is self-adjoint because the curvature operator is self-adjoint for the Hermitian pairing, and the complex structure is a skew-adjoint fixed operator of the involution when the involution commutes with $J$. The anti-self-adjointness of $J$ is the Hermitian counterpart of the skew-symmetry of the curvature, both being the anti-symmetry of an operator on the tangent space.

**Proof.** The proofs of the two preceding articles use only the metricity of the connection and the symmetry of the curvature, both of which hold for the Hermitian pairing extended complex-bilinearly; the complex structure is fixed by an involution that commutes with it, by the naturality of the constructions, and it is skew-adjoint by the first theorem. The comparison with the curvature is the observation that the curvature operator $R(X,Y)$ and the complex structure $J$ are both skew-adjoint endomorphisms, the first of rank two and the second of square $-1$.

## Examples

**Example (the flat Hermitian space).** On $\mathbb{C}^n$ with the Euclidean Hermitian metric the complex structure is the multiplication by $i$, anti-self-adjoint, $J^{*}=-J$; the Lefschetz operator is the wedge with $\omega = \frac{i}{2}\sum dz^j\wedge d\bar z^j$ and the contraction is its adjoint; the Kähler identities hold with the Laplacian the Euclidean one, and the harmonic forms are the forms with constant coefficients.

**Example (the Riemann sphere).** On $\mathbb{CP}^1$ with the Fubini–Study form the Lefschetz operator acts on the forms of the one-dimensional cohomology, the contraction is its adjoint, and the $\mathfrak{sl}_2$ relations reduce to the hard Lefschetz statement $L: H^0\to H^2$ being an isomorphism; the Hodge numbers are $h^{0,0}=h^{1,1}=1$ and the Dolbeault Laplacians agree with the de Rham one by the Kähler identities.

**Example (the complex projective space).** On $\mathbb{CP}^n$ the hard Lefschetz theorem makes $L^k : H^{n-k}\to H^{n+k}$ an isomorphism, the primitive cohomology is the kernel of $\Lambda$, and the Lefschetz decomposition is the decomposition of the cohomology into the primitive pieces; the complex structure is anti-self-adjoint and the Kähler identities make the Hodge–de Rham spectra agree. These are the algebraic consequences of the adjoint relations of the Hermitian structure, and their full development is the Hermitian geometry of the later articles of this Part.

## Summary

On a Hermitian manifold the **Hermitian pairing** is the complexification of the metric, $\langle X,Y\rangle_{\mathbb{C}} = g(X,\bar Y)$, and the **complex structure is anti-self-adjoint** for it, $J^{*} = -J$, because $J$ is orthogonal with $J^2=-\mathrm{id}$; it is unitary, $\langle JX,JY\rangle_{\mathbb{C}} = \langle X,Y\rangle_{\mathbb{C}}$, and it is the operator-theoretic form of the almost complex structure. The adjoint of a complex-linear operator commuting with $J$ commutes with $J$, and the adjoint of an operator of type $(p,q)$ has type $(-p,-q)$, so the adjoint reverses the type.

The **Lefschetz operator** $L(\alpha) = \omega\wedge\alpha$ has the **contraction** $\Lambda$ as its adjoint, $L^{*} = \Lambda$, with the $\mathfrak{sl}_2$ relations $[\Lambda, L] = (n-k)\mathrm{id}$ on the $k$-forms of the complex dimension $n$ and the Lefschetz decomposition into the primitive parts. The **Kähler identities** express the adjoints of the Dolbeault operators, $[\Lambda,\partial] = i\bar\partial^{*}$ and $[\Lambda,\bar\partial] = -i\partial^{*}$, and give the equality of the Laplacians $\Delta_{\partial} = \Delta_{\bar\partial} = \frac12\Delta_d$; they are quoted here from *Hermitian Geometry and Almost Complex Structures*, where the Kähler theory is developed, and they are the adjoint relations of the complex structure. In this language the self-adjointness of the geodesic operator, the symmetry of the curvature operator and the commutation of the conjugations with the adjoint all persist, and the anti-self-adjointness of the complex structure is the Hermitian counterpart of the skew-symmetry of the curvature.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle X,Y\rangle_{\mathbb{C}} = g(X,\bar Y)$ | Hermitian pairing of the complexified tangent bundle |
| $T^{*}$, $\langle TX,Y\rangle_{\mathbb{C}}=\langle X,T^{*}Y\rangle_{\mathbb{C}}$ | Adjoint for the Hermitian pairing |
| $J^{*}=-J$, $J^{2}=-\mathrm{id}$ | Anti-self-adjoint complex structure |
| $\langle JX,JY\rangle_{\mathbb{C}}=\langle X,Y\rangle_{\mathbb{C}}$ | Unitarity of the complex structure |
| $T^{1,0}\oplus T^{0,1}$ | Holomorphic and anti-holomorphic parts |
| Type $(p,q)$, adjoint of type $(-p,-q)$ | Holomorphic and anti-holomorphic degrees |
| $L(\alpha)=\omega\wedge\alpha$, $\Lambda=L^{*}$ | Lefschetz operator and its adjoint, the contraction |
| $[\Lambda,L]=(n-k)\mathrm{id}$ on $\Omega^k$ | $\mathfrak{sl}_2$ relations; Lefschetz decomposition |
| $[\Lambda,\partial]=i\bar\partial^{*}$, $[\Lambda,\bar\partial]=-i\partial^{*}$ | Kähler identities |
| $\Delta_{\partial}=\Delta_{\bar\partial}=\frac12\Delta_d$ | Equality of the Laplacians on a Kähler manifold |

## Further Reading

- Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry, Volume II* (Interscience, 1969), for the Hermitian and the Kähler manifolds, the Lefschetz operator and the contraction.
- Phillip Griffiths and Joseph Harris, *Principles of Algebraic Geometry* (Wiley, 1978), for the Kähler identities, the Hodge theory and the Lefschetz decomposition.
- Werner Ballmann, *Lectures on Kähler Manifolds* (European Mathematical Society, 2006), for the complex structure, the Hermitian pairing, the Dolbeault operators and the Kähler identities.
- Andrei Moroianu, *Lectures on Kähler Geometry* (Cambridge University Press, 2007), for the Kähler identities, the Lefschetz operator and the Hodge theory.
- Jean-Pierre Demailly, *Complex Analytic and Differential Geometry* (open book, Institut Fourier), for the detailed proofs of the Kähler identities and the Hodge theory.
