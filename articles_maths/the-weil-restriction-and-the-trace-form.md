
# __The Weil Restriction and the Trace Form__

## Introduction

Descent recovers a variety over $k$ from its base change to $L$, and the reverse motion — passing from an $L$-variety to a $k$-variety that records the whole $L$-structure — is the **Weil restriction of scalars**. It is the right adjoint of the base-change functor, and the form it carries is the **trace form** of the extension, $q(x,y) = \operatorname{Tr}_{L/k}(xy)$, which is nondegenerate exactly when the extension is separable and is invariant under the Galois group; its multiplicative companion is the **norm**, $N_{L/k}(\alpha) = \det(m_\alpha)$, the invariant that governs the descent of the multiplicative group. This article fixes the Weil restriction, its adjunction, the trace and the norm, the trace form as an invariant bilinear form, and the restriction of the multiplicative group as a torus, and it is the second article of the `- * Theory` group.

The article reads the real structure of *Real Structures on Varieties and Galois Descent* through the invariant form and the invariant norm. Its neighbours are *Real Algebraic Varieties* and *Real Structures on a Curve*, later in this group, which use the trace form and the norm for the real points and the classification; the involution on the cohomology, which uses the invariance of the form to pair the cohomology with itself, is *The Galois Action on the Cohomology*. The trace and the norm of an extension are Part I's field theory, and they are recalled here in their algebraic form as the trace and the determinant of the multiplication operator, keeping the article self-contained; the bilinear and quadratic forms are those of the written *Bilinear Forms* and *Quadratic Forms and Polarisation* of this Part, and the field trace and norm of the written *Algebraic Number Theory* are the arithmetic instance. The word **trace form** is used here for the form of a field extension, and it is distinct from the trace form of an algebra with an involution, which is that of the written *Hilbert Algebras*.

Throughout $L/k$ is a finite separable field extension, taken Galois with group $G$ when the invariance statements are made; $[L:k] = n$. The Weil restriction is written $R_{L/k}$ and also $R_{L/k}X$; the base change is $T_L = T\times_kL$; the trace and the norm are $\operatorname{Tr}_{L/k}$ and $N_{L/k}$.

## The Weil Restriction of Scalars

### The Functor and its Representability

**Definition.** Let $X$ be a variety over $L$. The **Weil restriction of scalars** of $X$ is the functor
$$
R_{L/k}X\ :\ \{\text{$k$-schemes}\}^{\mathrm{opp}}\longrightarrow\{\text{sets}\}, \qquad
T\longmapsto X(T\times_kL),
$$
on the $k$-schemes, evaluated on the base change of the test object to $L$. The functor $R_{L/k}X$ is **representable** when it is isomorphic to the functor of points of a $k$-variety; the representing object, unique up to unique isomorphism, is also written $R_{L/k}X$.

**Theorem (existence on an affine chart).** Let $X = \operatorname{Spec}B$ be affine over $L$. Then $R_{L/k}X$ is representable by the affine $k$-variety $\operatorname{Spec}B$, where $B$ is regarded as a $k$-algebra through the structure map $k\to L\to B$. In particular $R_{L/k}(\mathbb{A}^n_L) = \mathbb{A}^{n[L:k]}_k$, and $R_{L/k}(\mathbb{G}_{a,L}) = \mathbb{G}_{a,k}^{[L:k]}$.

*Proof.* A $k$-morphism $T\to\operatorname{Spec}B$ is a $k$-algebra map $B\to\mathcal{O}_T(T)$, and a $k$-algebra map $B\to\mathcal{O}_T(T)$ is the same as an $L$-algebra map $B\to\mathcal{O}_T(T)\otimes_kL = \mathcal{O}_{T\times_kL}(T\times_kL)$ by the universal property of the scalar extension of Part I's *Extension of Scalars*, which is exactly an $L$-morphism $T\times_kL\to\operatorname{Spec}B$. The statements about the affine space and the additive group follow from $L\otimes_kL\cong L^{n}$ as $k$-spaces, so that $\operatorname{Spec}L[x_1,\ldots,x_n]$ is $\mathbb{A}^{n[L:k]}_k$.

**Theorem (existence for quasi-projective varieties).** Let $X$ be quasi-projective over $L$. Then $R_{L/k}X$ is representable by a quasi-projective $k$-variety, of dimension $[L:k]\dim X$, and the assignment $X\mapsto R_{L/k}X$ is functorial in $X$.

*Proof.* A quasi-projective $X$ embeds as a locally closed subscheme of some $\mathbb{P}^m_L$, and $R_{L/k}\mathbb{P}^m_L = \prod_{\sigma\in G}\mathbb{P}^m_k$ by the base-change theorem below; the restriction of a closed subvariety is the inverse image under the product of the embedding, of dimension $[L:k]\dim X$ because the base change multiplies every dimension by $[L:k]$. Functoriality is the functoriality of the functor of points.

### The Base Change and the Conjugates

**Definition.** For $\sigma\in G$ the **conjugate** of $X$ by $\sigma$ is the $L$-variety
$$
{}^\sigma X = X\times_{L,\sigma}L ,
$$
the base change of $X$ along the automorphism $\sigma$ of $L$; it agrees with $X$ when $\sigma = \mathrm{id}$.

**Theorem (the base change of the restriction).** For a finite Galois extension $L/k$ with group $G$ there is a canonical isomorphism over $L$
$$
\bigl(R_{L/k}X\bigr)\times_kL\ \cong\ \prod_{\sigma\in G}{}^\sigma X ,
$$
the product of the conjugates of $X$.

*Proof.* For a test object $T$ over $L$ the universal property gives $\operatorname{Hom}_L(T,(R_{L/k}X)\times_kL) = \operatorname{Hom}_k(T,R_{L/k}X) = \operatorname{Hom}_L(T\times_kL,X)$, and $T\times_kL\cong\prod_{\sigma\in G}T$ over $L$ by the Chinese remainder theorem for the separability of $L/k$, so the right side is $\prod_\sigma\operatorname{Hom}_L(T,{}^\sigma X)$. The identification is natural in $T$ and gives the displayed isomorphism.

**Corollary (the Weil restriction is the product of the conjugates).** For the trivial descent datum, where ${}^\sigma X\cong X$ for all $\sigma$, the base change of $R_{L/k}X$ is the $n$-fold product $X^n$; in general the restriction records the twists by the conjugates, and this is why it is the reverse of the descent of *Real Structures on Varieties and Galois Descent*.

## The Adjunction

**Theorem (base change is left adjoint to the restriction).** For a $k$-scheme $T$ and an $L$-variety $X$ there is a bijection, natural in both variables,
$$
\operatorname{Hom}_k\bigl(T,\ R_{L/k}X\bigr)\ \cong\ \operatorname{Hom}_L\bigl(T\times_kL,\ X\bigr),
$$
so that the base-change functor $(-)\times_kL$ is left adjoint to the Weil restriction:
$$
(-)\times_kL\ \dashv\ R_{L/k}.
$$

*Proof.* The displayed bijection is the definition of $R_{L/k}X$; the naturality is the naturality of the functor of points, and the left-adjoint statement is the same bijection read in the pair of functors.

**Corollary (the restriction preserves limits).** The Weil restriction preserves fibre products, terminal objects and, more generally, all limits; in particular it is left exact. It preserves the product of varieties, $R_{L/k}(X\times_LY)\cong R_{L/k}X\times_kR_{L/k}Y$, and it sends the point to the point.

*Proof.* A right adjoint preserves limits; the functor $(-)\times_kL$ is left adjoint to $R_{L/k}$, so $R_{L/k}$ is a right adjoint and preserves limits. The product is a limit, and the terminal object is the empty limit.

**Corollary (the functor of points of the restriction).** The $k$-points of the restriction are the $L$-points of $X$,
$$
(R_{L/k}X)(k) = X(L),
$$
and more generally $(R_{L/k}X)(T) = X(T_L)$. In particular the Weil restriction is a machine for changing the field of definition of the points while keeping the same variety.

*Proof.* The defining bijection with $T = \operatorname{Spec}k$ gives $(R_{L/k}X)(k) = X(\operatorname{Spec}k\times_kL) = X(L)$.

## The Trace Form

### The Trace and the Norm

**Definition.** For $\alpha\in L$ let $m_\alpha : L\to L$, $x\mapsto\alpha x$, be the multiplication operator, a $k$-linear endomorphism of the $n$-dimensional $k$-space $L$. The **trace** and the **norm** of $\alpha$ are
$$
\operatorname{Tr}_{L/k}(\alpha) = \operatorname{tr}(m_\alpha), \qquad N_{L/k}(\alpha) = \det(m_\alpha),
$$
the trace and the determinant of the multiplication operator of Part I's linear algebra.

**Theorem (the elementary properties).** The trace is $k$-linear, $\operatorname{Tr}_{L/k}(\alpha+\lambda\beta) = \operatorname{Tr}_{L/k}(\alpha)+\lambda\operatorname{Tr}_{L/k}(\beta)$, and the norm is multiplicative, $N_{L/k}(\alpha\beta) = N_{L/k}(\alpha)N_{L/k}(\beta)$; on the base field both are the scalar multiplication by the degree,
$$
\operatorname{Tr}_{L/k}(\lambda) = n\lambda, \qquad N_{L/k}(\lambda) = \lambda^{n} \qquad (\lambda\in k).
$$
The norm is a group homomorphism $N_{L/k} : L^\times\to k^\times$.

*Proof.* The map $\alpha\mapsto m_\alpha$ is a $k$-algebra homomorphism from $L$ to $\operatorname{End}_k(L)$, since $m_{\alpha+\lambda\beta} = m_\alpha+\lambda m_\beta$ and $m_{\alpha\beta} = m_\alpha m_\beta$; the trace is linear and the determinant multiplicative on the algebra of endomorphisms, which gives the first two statements. For $\lambda\in k$ the operator $m_\lambda$ is the scalar $\lambda$ on the $n$-dimensional space, with trace $n\lambda$ and determinant $\lambda^n$. Finally $N_{L/k}(\alpha)\neq0$ for $\alpha\neq0$ because $m_\alpha$ is invertible when $\alpha$ is, so the norm restricts to the unit groups and is multiplicative there.

**Theorem (the Galois description).** Let $L/k$ be Galois with group $G$. Then for all $\alpha\in L$
$$
\operatorname{Tr}_{L/k}(\alpha) = \sum_{\sigma\in G}\sigma(\alpha), \qquad
N_{L/k}(\alpha) = \prod_{\sigma\in G}\sigma(\alpha) ,
$$
and in particular the trace and the norm take values in $k$ and are invariant under $G$.

*Proof.* The conjugates $\sigma(\alpha)$, $\sigma\in G$, are the eigenvalues of the multiplication operator $m_\alpha$ on the $k$-space $L$, each occurring once when $L/k$ is Galois: a basis of $L$ over $k$ diagonalises $m_\alpha$ over the normal closure because the minimal polynomial of $\alpha$ splits and is separable, and the eigenvalues are the conjugates. Hence the trace is their sum and the determinant their product. Each is fixed by every $\sigma$, so both lie in $L^G = k$.

**Example ($\mathbb{C}/\mathbb{R}$).** For $z = a+bi$ one has $\operatorname{Tr}_{\mathbb{C}/\mathbb{R}}(z) = z+\bar z = 2a$ and $N_{\mathbb{C}/\mathbb{R}}(z) = z\bar z = a^2+b^2$; the norm is the square of the modulus of *Complex Norm and Invertibility*, and the multiplicative group of norm one is the kernel $N^{-1}(1)$.

### The Trace Form as an Invariant Form

**Definition.** The **trace form** of the extension $L/k$ is the symmetric $k$-bilinear form
$$
q : L\times L\longrightarrow k, \qquad q(x,y) = \operatorname{Tr}_{L/k}(xy).
$$
Its polar quadratic form is $\alpha\mapsto\operatorname{Tr}_{L/k}(\alpha^2)$, and its discriminant is the determinant of the Gram matrix in a $k$-basis of $L$.

**Theorem (nondegeneracy and invariance).** The trace form is nondegenerate exactly when $L/k$ is separable, and when $L/k$ is Galois it is invariant under the action,
$$
q(\sigma x,\sigma y) = q(x,y) \qquad (\sigma\in G),
$$
so that the Galois group preserves the trace form. The multiplication operator $m_\alpha$ is self-adjoint with respect to $q$, $q(\alpha x,y) = q(x,\alpha y)$.

*Proof.* Since $G$ is the group of the $k$-embeddings of $L$ into an algebraic closure, the Gram matrix in a $k$-basis $(b_i)$ of $L$ is
$$
M_{ij} = \operatorname{Tr}_{L/k}(b_ib_j) = \sum_{\sigma\in G}b_i^{(\sigma)}b_j^{(\sigma)} = (B^{t}B)_{ij},
$$
where $B = (b_i^{(\sigma)})$ is the matrix of the conjugates. Hence $\det M = \det(B)^2$, and $\det B\neq0$ exactly when the conjugates are linearly independent over the closure, which is exactly the separability of $L/k$ by the theorem of the primitive element and the linear independence of the distinct embeddings. So the form is nondegenerate if and only if the extension is separable, and the discriminant $\det M$ is a square in $k$. Invariance is $\operatorname{Tr}(\sigma x\,\sigma y) = \operatorname{Tr}(\sigma(xy)) = \operatorname{Tr}(xy)$, the trace taking values in $k$. The self-adjointness is the commutativity of $L$: $q(\alpha x,y) = \operatorname{Tr}(\alpha xy) = \operatorname{Tr}(x\alpha y) = q(x,\alpha y)$.

**Theorem (the norm and the trace of a product of conjugates, and transitivity).** For a tower $M/L/k$ one has
$$
\operatorname{Tr}_{M/k} = \operatorname{Tr}_{L/k}\circ\operatorname{Tr}_{M/L}, \qquad N_{M/k} = N_{L/k}\circ N_{M/L},
$$
and the norm is the unique multiplicative map whose restriction to $L$ is the power $N_{L/k}$. In particular the norm is multiplicative on the tower and the trace additive.

*Proof.* The multiplication operator on $M$ over $k$ is the composite of multiplication on $M$ over $L$ with multiplication on $L$ over $k$; the trace of a composite of $k$-linear maps is the trace of their product in the tensor description, and the determinant multiplies, giving the two identities. The uniqueness is the multiplicativity together with the degree.

## The Norm and the Torus

**Theorem (the Weil restriction of the multiplicative group).** The Weil restriction $T = R_{L/k}\mathbb{G}_m$ is a $k$-torus of dimension $n$, called the **norm torus** of the extension. Its character and cocharacter lattices are
$$
X^*(T) = \mathbb{Z},\qquad X_*(T) = \mathbb{Z}[G] ,
$$
the cocharacter lattice being the group ring with the $G$-action by permutation. The norm is the character
$$
N_{L/k} : R_{L/k}\mathbb{G}_m\longrightarrow\mathbb{G}_m
$$
corresponding to the augmentation $\mathbb{Z}[G]\to\mathbb{Z}$ on the cocharacters, and its kernel is the **norm-one torus** $T^1 = \ker N_{L/k}$.

*Proof.* The functor of points is $T(R) = (R\otimes_kL)^\times$; on a $k$-algebra $R$ this is the unit group of $R\otimes_kL$, whose character group is $\mathbb{Z}$ by the rank-one units and whose cocharacter group is the free abelian group on the idempotents of $L\otimes_kL$, identified with $\mathbb{Z}[G]$ by the Chinese remainder theorem. The norm is the determinant of multiplication on $R\otimes_kL$ and is the product of the permutation of the idempotents without fixed points, which is the augmentation; the kernel is the norm-one torus by definition. The dimension of a torus is the rank of its cocharacter lattice, here $n$.

**Example ($\mathbb{C}/\mathbb{R}$ and the norm-one group).** For $L = \mathbb{C}$, $k = \mathbb{R}$ the norm torus is the anisotropic torus of dimension two whose $\mathbb{R}$-points are $\mathbb{C}^\times$, and the norm-one torus has $\mathbb{R}$-points the group $N^{-1}(1) = \{z : z\bar z = 1\}$. On $\mathbb{C}\cong\mathbb{R}^2$ the bilinear trace form is $q(z,w) = 2\,\mathrm{Re}(zw)$, of signature $(1,1)$ in the basis $1,i$, while the associated Hermitian form $h(z,w) = q(z,\bar w) = 2\,\mathrm{Re}(z\bar w)$ is positive definite; the Galois group acts by the conjugation, which preserves both forms. This torus is the formal model of the real structure on the multiplicative group; the restriction of the additive group is $\mathbb{G}_{a,\mathbb{R}}^2$ with the same trace form.

**Example ($\mathbb{Q}(\sqrt d)/\mathbb{Q}$).** For $L = \mathbb{Q}(\sqrt d)$ with $d$ square-free, the conjugate is $\sqrt d\mapsto-\sqrt d$ and
$$
\operatorname{Tr}(a+b\sqrt d) = 2a, \qquad N(a+b\sqrt d) = a^2-db^2 ,
$$
so the norm-one torus has the rational points $a^2-db^2 = 1$; the norm torus is the two-dimensional torus with rational points the units of the quadratic field, and the norm-one torus is its one-dimensional subtorus. The trace form is $\operatorname{diag}(2, 2d)$ in the basis $1,\sqrt d$, of signature $(2,0)$ for $d>0$ and $(1,1)$ for $d<0$.

## Summary

The **Weil restriction of scalars** $R_{L/k}$ sends an $L$-variety $X$ to the $k$-variety that represents the functor $T\mapsto X(T\times_kL)$. It exists for affine and for quasi-projective $X$, sending $\mathbb{A}^n_L$ to $\mathbb{A}^{n[L:k]}_k$, it is the **right adjoint** of the base change,
$$
\operatorname{Hom}_k(T,R_{L/k}X)\cong\operatorname{Hom}_L(T\times_kL,X),
$$
so it preserves limits and its points are the points of $X$ over $L$, and its own base change is the product of the conjugates, $(R_{L/k}X)\times_kL\cong\prod_{\sigma\in G}{}^\sigma X$. The **trace** and the **norm** of the extension are the trace and the determinant of the multiplication operator, $\operatorname{Tr}_{L/k}(\alpha) = \operatorname{tr}(m_\alpha)$ and $N_{L/k}(\alpha) = \det(m_\alpha)$; for a Galois extension they are the sum and the product of the conjugates, they take values in $k$, they are $G$-invariant, and they are the elementary symmetric functions of the eigenvalues of multiplication. The **trace form** $q(x,y) = \operatorname{Tr}_{L/k}(xy)$ is symmetric and is nondegenerate exactly when $L/k$ is separable; it is invariant under the Galois group, so the group preserves the form, and every multiplication is self-adjoint for it. The **norm torus** $R_{L/k}\mathbb{G}_m$ is an $n$-dimensional torus with cocharacter lattice $\mathbb{Z}[G]$ and the norm as its augmentation character, and its kernel is the norm-one torus, the invariant that classifies the forms of the multiplicative group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R_{L/k}X$, $(R_{L/k}X)(T)=X(T\times_kL)$ | Weil restriction of scalars; right adjoint of base change |
| $(-)\times_kL\dashv R_{L/k}$ | the adjunction |
| $R_{L/k}(\mathbb{A}^n_L)=\mathbb{A}^{n[L:k]}_k$ | the restriction of the affine space |
| ${}^\sigma X=X\times_{L,\sigma}L$, $(R_{L/k}X)_L\cong\prod_\sigma{}^\sigma X$ | conjugates and the base change of the restriction |
| $m_\alpha$, $x\mapsto\alpha x$ | multiplication operator by $\alpha$ on the $k$-space $L$ |
| $\operatorname{Tr}_{L/k}(\alpha)=\operatorname{tr}(m_\alpha)=\sum_\sigma\sigma(\alpha)$ | the trace |
| $N_{L/k}(\alpha)=\det(m_\alpha)=\prod_\sigma\sigma(\alpha)$ | the norm, multiplicative $L^\times\to k^\times$ |
| $\operatorname{Tr}(\lambda)=n\lambda$, $N(\lambda)=\lambda^n$ | the trace and the norm on the base field |
| $q(x,y)=\operatorname{Tr}_{L/k}(xy)$ | the trace form; nondegenerate iff separable |
| $q(\sigma x,\sigma y)=q(x,y)$ | invariance under the Galois group |
| $q(\alpha x,y)=q(x,\alpha y)$ | multiplication is self-adjoint for the trace form |
| $\operatorname{Tr}_{M/k}=\operatorname{Tr}_{L/k}\circ\operatorname{Tr}_{M/L}$, $N_{M/k}=N_{L/k}\circ N_{M/L}$ | transitivity in a tower |
| $T=R_{L/k}\mathbb{G}_m$ | the norm torus; $\dim T=n$ |
| $X^*(T)=\mathbb{Z}$, $X_*(T)=\mathbb{Z}[G]$ | characters and cocharacters of the norm torus |
| $T^1=\ker N_{L/k}$ | the norm-one torus |
| $(R_{L/k}X)(k)=X(L)$ | the $k$-points are the $L$-points |

## Further Reading

- André Weil, *Adeles and Algebraic Groups* (Birkhäuser, 1982), for the restriction of scalars and its use in the arithmetic of algebraic groups.
- Serge Lang, *Algebra* (Springer, Graduate Texts in Mathematics 211, third edition, 2002), for the trace, the norm and the discriminant of a separable field extension and the trace form of a tower.
- Jean-Pierre Serre, *Local Fields* (Springer, Graduate Texts in Mathematics 67, 1979), for the trace form, the discriminant and the norm of a separable extension.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for the trace form of an algebra with involution and the norm torus.
- Igor R. Shafarevich, *Basic Algebraic Geometry 1* (Springer, third edition, 2013), for the restriction of scalars of a variety and its dimension.
- Tonny A. Springer, *Linear Algebraic Groups* (Birkhäuser, second edition, 1998), for the norm torus, its characters and the classification of the forms of a torus.
