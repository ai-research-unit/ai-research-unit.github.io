# __Unitary and Isometric Operators of the Form__

## Introduction

An operator of a space with a form can preserve the form, $h(Tx,Ty) = h(x,y)$, and it can have the adjoint for its inverse, $T^{\dagger}T = TT^{\dagger} = 1$. The two properties look alike and are not: the first is a geometric condition read on pairs, the second an algebraic one read on the composition of $T$ with its adjoint, and in a complete definite space the first defines a monoid that properly contains the group defined by the second. This article reads the **isometry monoid** and the **unitary group** of the Hermitian form of *Topological Sesqualgebras with a Form*, proves that the two coincide exactly when every isometry is invertible — always in finite dimension, never in the complete infinite-dimensional definite case — and relates both to the unitary elements of the algebra: the left multiplication by $u$ is an isometry when $u^{*}u = 1$, a unitary operator when $u$ is unitary, and the inner automorphism by a unitary element is a unitary operator with kernel the central unitaries. The indefinite case is included, and the conjugation by the fundamental symmetry of *The Fundamental Symmetry of the Form* converts the unitary group of the form into the $J$-unitary group of the definite companion, so the indefinite isometry group is the one of *The Krein Isometry Group and Its $J$-Contractions*.

Three facts organise the article. The **unitary group** $U(A,h)$ is a group, the group of units of the isometry monoid, and the map $u \mapsto u^{\dagger}$ restricted to it is inversion: the adjoint operation of *The Adjoint under a Hermitian Form* is a $\varsigma$-semilinear anti-automorphism of order two, and on the group-theoretic side it is the anti-automorphism $u \mapsto u^{-1}$. The **isometries that are not unitary** are the phenomenon of the incomplete or the infinite-dimensional definite case: an isometry is injective on a nonsingular space, but injectivity and surjectivity separate in infinite dimension, and the unilateral shift of a Hilbert space is isometric without being unitary. And the **operators of the elements** are the bridge between the group of the algebra and the group of the form: $m_{u}$ is an isometry exactly when $u$ is left-unitary and a unitary operator exactly when $u$ is unitary, the assignment $u \mapsto m_{u}$ is injective on a unital object, and the assignment $u \mapsto \alpha_{u}$ of the inner automorphism has the central unitaries for kernel.

The article defines the isometry monoid and the unitary group, proves the equivalences and the group laws, identifies inversion with the adjoint, separates isometries from unitaries, treats the multiplications and the inner automorphisms, and works the field, the matrices and the biquaternion algebra. The adjoint is *The Adjoint under a Hermitian Form*; the unitary elements are *Units and the Unitary Elements*; the operator-theoretic unitary operators without a form are *The Unitary Operators of a Sesqualgebra*; the topological group is *The Unitary Group as a Topological Group*; the bilinear counterpart is *Isometries and Orthogonal Transformations*. Throughout, $A$ is a sesqualgebra with a nonsingular Hermitian form $h$ over a base $(R,\varsigma)$ of one of the two classical kinds of *The Norm Defined by a Form*, with fixed field $k = R^{\varsigma}$, the adjoint is the one of *The Adjoint under a Hermitian Form*, and $U(A) = \{u : uu^{*} = u^{*}u = 1\}$ is the group of the unitary elements.

## Isometries and Unitaries

### The Definitions

**Definition.** Let $T \in B(A)$. Then $T$ is an **isometry of the form**, or a **form isometry**, when

$$
h(Tx,Ty) = h(x,y) \qquad \text{for all } x, y \in A ,
$$

and $T$ is a **unitary operator of the form** when

$$
T^{\dagger}T = TT^{\dagger} = 1 .
$$

The set of form isometries is the **isometry monoid** $\mathrm{Iso}(A,h)$, and the set of unitary operators is the **unitary group** $U(A,h)$.

The name is justified by the two theorems of the next subsection: the isometries are closed under composition and contain the identity, hence form a monoid, and the unitary operators are exactly the invertible elements of that monoid, hence form its group of units. Both are subsets of $B(A)$, and the definite complete case shows that the inclusion can be proper.

### The Equivalences

**Theorem (the isometry criterion).** Let $h$ be nonsingular. Then for $T \in B(A)$ the following are equivalent:

$$
\text{(i) } h(Tx,Ty) = h(x,y) \quad \text{for all } x,y ; \qquad \text{(ii) } T^{\dagger}T = 1 .
$$

Every isometry is injective, and $T$ is unitary exactly when it is an invertible isometry, equivalently exactly when $T^{\dagger} = T^{-1}$.

*Proof.* (i) implies (ii) by rewriting $h(Tx,Ty) = h(x,T^{\dagger}Ty)$ and using the nondegeneracy of $h$: $h(x,T^{\dagger}Ty) = h(x,y)$ for all $x,y$ gives $T^{\dagger}T = 1$. (ii) implies (i) by $h(Tx,Ty) = h(x,T^{\dagger}Ty) = h(x,y)$. Injectivity is the implication (ii) $\Rightarrow$ ($Tx = 0 \Rightarrow x = 0$): from $0 = h(Tx,Ty) = h(x,y)$ for all $y$ and the nondegeneracy of $h$. If $T$ is an invertible isometry then $T^{\dagger} = T^{\dagger}TT^{-1} = T^{-1}$ and $TT^{\dagger} = 1$; conversely $T^{\dagger} = T^{-1}$ gives $T^{\dagger}T = TT^{\dagger} = 1$. $\square$

**Remark (the companion form is a different condition).** The isometry of a definite companion, $\langle Tx,Ty\rangle = \langle x,y\rangle$ for a companion with fundamental symmetry $J$, is **not** equivalent to (i). By *The Fundamental Symmetry of the Form*, §*The Adjoints under the Two Forms*, the $h$-isometry is the identity $T^{*}JT = J$ while the companion isometry is $T^{*}T = 1$, and the two differ as soon as $J \neq \pm\mathrm{id}$: on the plane of signature $(1,1)$ the Lorentz boost $T_{t}$ satisfies $h(T_{t}x,T_{t}y) = h(x,y)$ and $\langle T_{t}x,T_{t}y\rangle \neq \langle x,y\rangle$ for the Euclidean companion. The isometry criterion is therefore a statement about the given form, and its indefinite reading is the theorem of §*The Indefinite Case* below.

**Corollary (the monoid and its group of units).** The isometries are closed under composition and contain $\mathrm{id}$, and the unitary operators are exactly the invertible isometries; hence $\mathrm{Iso}(A,h)$ is a monoid and $U(A,h)$ is its group of units. Moreover $U(A,h)$ is a group under composition, and $U(A,h) \subseteq \mathrm{Iso}(A,h)$.

*Proof.* If $S, T$ are isometries then $h(STx,STy) = h(Tx,Ty) = h(x,y)$, so $ST$ is an isometry, and $\mathrm{id}$ is one. That the unitary operators are the invertible isometries is the theorem; a monoid's invertible elements form its group of units. $\square$

### Inversion Is the Adjoint

**Theorem (inversion on the unitary group).** Let $h$ be nonsingular. Then the restriction to $U(A,h)$ of the adjoint operation is inversion,

$$
T^{\dagger} = T^{-1} \qquad \text{for } T \in U(A,h) ,
$$

and it is an involutive anti-automorphism of the group: $(ST)^{\dagger} = T^{\dagger}S^{\dagger}$, $(T^{\dagger})^{\dagger} = T$, $1^{\dagger} = 1$. So the group $U(A,h)$ is stable under the adjoint, and the adjoint operation is the inversion of the group together with the $\varsigma$-semilinear action on the scalars.

*Proof.* The formula is the characterization of the unitary operators; the anti-automorphism laws are those of *The Adjoint under a Hermitian Form*, §*The Anti-Automorphism*, restricted to the group, and the restriction makes sense because the adjoint of a unitary operator is again unitary, $(T^{\dagger})^{\dagger} = T$ and $T^{\dagger}(T^{\dagger})^{\dagger} = T^{\dagger}T = 1$. $\square$

**Remark (an anti-automorphism that is an inversion).** The theorem is a small but consequential coincidence: on the unitary group the two operations of the ambient algebra, the adjoint $T \mapsto T^{\dagger}$ and the inverse $T \mapsto T^{-1}$, coincide, so an anti-automorphism of $B(A)$ restricts to the inversion of $U(A,h)$. This is the form-layer statement of the coincidence of the adjoint with the inverse on the unitary elements, and it is what makes $U(A,h)$ a group under composition and not only under the opposite operation.

## Isometries That Are Not Unitary

### Finite Dimension

**Theorem (finite dimension).** Let $A$ be finite dimensional over $R$ and $h$ nonsingular. Then every isometry is unitary, so $\mathrm{Iso}(A,h) = U(A,h)$.

*Proof.* An isometry is injective on a finite-dimensional space, hence bijective; by the theorem it is then unitary. $\square$

**Remark (the finite models).** On $\mathbb{C}^{n}$ with a nondegenerate Hermitian form the isometry group is therefore the full indefinite unitary group of the signature, and on the matrices of the examples it is a compact or an indefinite unitary group according to the sign; the equality of the two sets is the reason the definite finite-dimensional theory never has to distinguish them.

### The Definite Complete Case

**Theorem (the shift; the inclusion can be proper).** Let $H$ be a complex Hilbert space of infinite dimension, identifiable with $\ell^{2}$, and let $S$ be the unilateral shift, $S(x_{0},x_{1},\dots) = (0,x_{0},x_{1},\dots)$. Then $S$ is an isometry, $S^{*}S = 1$, but $SS^{*} = 1 - P_{0}$ where $P_{0}$ is the projection onto the first coordinate, so $S$ is not surjective and not unitary. The unitary operators are exactly the surjective isometries; in the definite complete case they are not all the isometries, and $U(H) \subsetneq \mathrm{Iso}(H)$ strictly.

*Proof.* The shift is isometric because $\lVert Sx\rVert = \lVert x\rVert$, and its adjoint is the backward shift, $S^{*}(x_{0},x_{1},\dots) = (x_{1},x_{2},\dots)$, so $S^{*}S = 1$ and $SS^{*}$ kills the first coordinate. A surjective isometry is invertible with $T^{-1} = T^{\dagger}$, hence unitary; $S$ is injective but not surjective. The example is the standard one of the Hilbert-space theory of isometries. $\square$

**Remark (why the two conditions separate).** A form isometry is a geometric condition, $h(Tx,Ty) = h(x,y)$, and the nondegeneracy of the form makes it injective; surjectivity is a completeness and dimension condition independent of the form, and in infinite dimension an isometry can miss a topologically complementable subspace. The defect $1 - TT^{\dagger}$ of an isometry is the projection onto the orthogonal complement of its range, the object of the **defect operators** of the isometry theory, and it vanishes exactly on the unitary operators.

### The Indefinite Case

**Theorem (the indefinite isometry group is the $J$-unitary group).** Let $h$ be indefinite with fundamental decomposition of symmetry $J$ and companion form $\langle\cdot,\cdot\rangle$, both nonsingular. Then

$$
T \in U(A,h) \iff T^{*}JT = J \iff T \in U(J) ,
$$

where $T^{*}$ is the companion adjoint and $U(J)$ is the group of the companion operators preserving $J$. On a finite-dimensional space the conditions reduce to $h(Tx,Ty) = h(x,y)$ for all $x,y$.

*Proof.* The equivalence is the theorem of *The Fundamental Symmetry of the Form*, §*The Adjoints under the Two Forms*: $T^{\dagger}T = 1$ reads $JT^{*}JT = 1$, that is $T^{*}JT = J$ after applying $J$; the reverse reading is the same computation. In finite dimension the injectivity gives invertibility, so the isometry condition and the unitary condition coincide. $\square$

**Remark (the boosts).** The theorem is the reason the indefinite isometry group is not the unitary group of the companion: an operator can be $h$-unitary and not companion-unitary, and the Lorentz boosts of the signature $(1,1)$ plane are the smallest examples, $T_{t} = \begin{pmatrix}\cosh t & \sinh t \\ \sinh t & \cosh t\end{pmatrix}$, which satisfies $T_{t}^{T}JT_{t} = J$ and $T_{t}^{T}T_{t} \neq I$. The group $U(J)$ is the **Krein isometry group** of the indefinite form, non-compact and containing the boosts, and the concrete case is *The Krein Isometry Group and Its $J$-Contractions*; the operator theory of its elements is *J-Self-Adjoint and J-Unitary Operators* and, for the biquaternion algebra, *J-Self-Adjoint and J-Unitary Operators on the Biquaternion Algebra*.

## The Operators of the Elements

### The Multiplications

**Theorem (the multiplications by the elements).** Let $h$ be compatible and nonsingular, let $m_{u}(z) = uz$ be the left multiplication by $u \in A$. Then

$$
m_{u} \in \mathrm{Iso}(A,h) \iff u^{*}u = 1 , \qquad m_{u} \in U(A,h) \iff u \in U(A) ,
$$

and the assignment $u \mapsto m_{u}$ is an injective homomorphism on a unital object, with $m_{u}^{\dagger} = m_{u^{*}}$.

*Proof.* By the adjointness of the multiplications, $m_{u}^{\dagger} = m_{u^{*}}$, so $m_{u}^{\dagger}m_{u} = m_{u^{*}u}$; this is the identity exactly when $u^{*}u = 1$, by the injectivity of $m$ on a unital object, and the isometry criterion gives the first equivalence. For the second, $m_{u}$ is invertible exactly when $u$ is a unit, with $m_{u}^{-1} = m_{u^{-1}}$, and it is unitary exactly when $u^{*}u = uu^{*} = 1$. Injectivity is $m_{u} = \mathrm{id} \Rightarrow u = u\cdot 1 = 1$ on a unital object. $\square$

**Remark (what the theorem says).** The unitary group of the algebra embeds in the unitary group of the form as the group of the left multiplications, and the whole isometry monoid of the form contains the image of the **left-unitary** elements, those with $u^{*}u = 1$ alone. The embedding is the source of the containment of $U(A)$ in $U(A,h)$ that makes the operator group carry the algebra's own group, and it is the form-layer analogue of *The Unitary Operators of a Sesqualgebra*, where the same assignment is read without the form on the operator-theoretic unitary condition.

### The Inner Automorphisms

**Theorem (the inner automorphisms are unitary operators).** Let $u \in U(A)$ and let $\alpha_{u}(x) = uxu^{*}$. Then $\alpha_{u} \in U(A,h)$, with $\alpha_{u}^{\dagger} = \alpha_{u}^{-1} = \alpha_{u^{*}}$, so the assignment $u \mapsto \alpha_{u}$ is a group homomorphism $U(A) \to U(A,h)$ whose kernel is the group of the **central unitary elements**, $U(A)\cap Z(A)$, and whose image is the group of the inner $\ast$-automorphisms.

*Proof.* The isometry and adjoint formulas are the theorem of *The Adjoint under a Hermitian Form*, §*The Inner Automorphisms*; a homomorphism of groups lands in the unitary group, and $\alpha_{u} = \mathrm{id}$ exactly when $uxu^{*} = x$ for all $x$, that is when $u$ is central, the standard computation of *Units and the Unitary Elements*, §*Inner $*$-Automorphisms*. $\square$

**Remark (two containments).** The algebra's unitary group thus sits in the form's unitary group in two ways: injectively through the left multiplications, $u \mapsto m_{u}$, and with the centre for kernel through the inner automorphisms, $u \mapsto \alpha_{u}$. On the matrices both are visible, $U(n) \hookrightarrow U(n^{2})$ in the first case and $PU(n) \hookrightarrow U(n^{2})$ in the second.

## Worked Cases

### The Field

**Example (the field).** Let $A = \mathbb{C}$ with $h(z,w) = z\overline{w}$. The operators are the multiplications $T_{\lambda}$, the adjoint is $T_{\lambda}^{\dagger} = T_{\overline{\lambda}}$, and

$$
T_{\lambda} \in \mathrm{Iso}(\mathbb{C},h) \iff T_{\lambda} \in U(\mathbb{C},h) \iff \lvert\lambda\rvert = 1 .
$$

So the isometry monoid is the unit circle $U(1)$, and it coincides with the unitary group because the space is one-dimensional and every isometry is invertible. The example is the smallest in which the two groups agree, and the scalar case of the containment $U(A) \subseteq U(A,h)$, which is an equality there.

### The Matrices

**Example (the matrices).** Let $A = M_{n}(\mathbb{C})$ with $h(X,Y) = \operatorname{tr}(XY^{*})$, identifiable with $\mathbb{C}^{n^{2}}$ as a Hilbert space. Then

$$
U(A,h) = U(n^{2}) , \qquad \mathrm{Iso}(A,h) = U(n^{2}) ,
$$

the definite form being complete and finite dimensional; the left multiplications embed $U(n)$ in $U(n^{2})$ by $u \mapsto m_{u}$, and the inner automorphisms embed $PU(n) = U(n)/U(1)$ in $U(n^{2})$ by $u \mapsto \alpha_{u}$, the kernel being the scalar unitaries. The example realizes both containments concretely and shows that the isometry monoid and the unitary group coincide exactly in finite dimension.

### The Biquaternion Algebra

**Example (the biquaternion algebra, definite and indefinite).** On $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ the definite complex sesquilinear form $h_{*}(P,Q) = \operatorname{Sc}(PQ^{*}) = \tilde P\tilde Q^{*}$, of signature $(8,0)$ over $\mathbb{R}$, has unitary group $U(4)$; the indefinite quaternion sesquilinear form $h_{\natural*}(P,Q) = \sum_{\mu}\varepsilon_{\mu}P_{\mu}\overline{Q_{\mu}}$, of signature $(2,6)$ over $\mathbb{R}$ and $(1,3)$ over $\mathbb{C}$, has isometry group the indefinite unitary group $U(1,3)$ of the same complex dimension, the **Krein isometry group** $U_{J}(\mathbb{B})$; and $U(1,3)$ is non-compact, contains the Lorentz boosts, and is related to $U(4)$ by $T^{\dagger} = JT^{*}J$ with $J = \operatorname{diag}(1,-1,-1,-1)$. The signature and the form are *The Biquaternion Krein Form and Its Signature*; the group is *The Krein Isometry Group and Its $J$-Contractions*; the unitary elements of the algebra and their group are *The Unitary Group of the Biquaternion Algebra* and *The Biquaternion Unit Group as a Topological Group*. The example is the finite-dimensional indefinite model in which the isometry group and the unitary group coincide, the space being finite dimensional, while the group itself is the indefinite one.

## The Collapse at the Trivial Involution

**Theorem (the collapse).** Let $\varsigma = \mathrm{id}$. Then the form is symmetric and bilinear, the criterion $T^{\dagger}T = 1$ is the criterion $h(Tx,Ty) = h(x,y)$ of an isometry of a symmetric form, the isometry monoid is the **orthogonal group** of the form, and the construction is that of *Isometries and Orthogonal Transformations*; at $* = \mathrm{id}$ as well the left multiplication is self-adjoint and every unitary element is self-adjoint, so $U(A)$ is the group of the involutive units and the containment $U(A) \subseteq U(A,h)$ is read for the orthogonal group of the form.

*Proof.* At $\varsigma = \mathrm{id}$ the twist vanishes, the form is symmetric, and the two criteria coincide; the identification with the bilinear isometry theory is *The Sesquilinear Adjoint Operator*, §*The Comparison with the Bilinear Case* and *Isometries and Orthogonal Transformations*. The statement for $U(A)$ at $* = \mathrm{id}$ is $u^{*}u = u^{2} = 1$. $\square$

**Remark (what the collapse preserves and what it drops).** The collapse preserves the isometry monoid, the unitary group, the containment of the algebra's group and the distinction of isometries from unitaries; it drops the twist of the scalar action, through which the adjoint operation is $\varsigma$-semilinear on the linear operators, and its companion, indefinite or not, becomes a symmetric bilinear form. The sesquilinear content of the article is therefore in the slot rules of the form that the operators preserve and in the two groups of the algebra that the operator groups contain.

## Summary

The **isometry monoid** of a Hermitian form is the set of operators with $h(Tx,Ty) = h(x,y)$, equivalently $T^{\dagger}T = 1$, and the **unitary group** $U(A,h)$ is the set with $T^{\dagger}T = TT^{\dagger} = 1$, equivalently the invertible isometries, equivalently the operators with $T^{\dagger} = T^{-1}$. On it the adjoint operation is inversion, so the $\varsigma$-semilinear anti-automorphism $T \mapsto T^{\dagger}$ of *The Adjoint under a Hermitian Form* restricts to the inversion of the group. Isometries are always injective but need not be surjective: in finite dimension the two sets **coincide**, in the complete infinite-dimensional definite case the unilateral shift is an isometry that is not unitary, and in the indefinite case the unitary group is the **$J$-unitary group** $U(J) = \{T : T^{*}JT = J\}$ of the companion, which is non-compact and contains the boosts. The **operators of the elements** tie the group of the form to the group of the algebra: the left multiplication $m_{u}$ is an isometry exactly when $u^{*}u = 1$ and a unitary operator exactly when $u$ is unitary, the assignment $u \mapsto m_{u}$ being injective on a unital object, and the inner automorphism $\alpha_{u}$ is unitary with the central unitaries for kernel, so that $U(A)$ sits in $U(A,h)$ in the two ways. The worked cases are the field, where the group is the unit circle and the two sets agree; the matrices, where they are $U(n^{2})$ and the containments are $U(n) \hookrightarrow U(n^{2})$ and $PU(n) \hookrightarrow U(n^{2})$; and the biquaternion algebra, where they are $U(4)$ for the definite form and $U(1,3)$ for the indefinite one. At $\varsigma = \mathrm{id}$ the construction is the one of the **orthogonal group** of a symmetric bilinear form.

## Summary of Notation

| symbol | meaning |
|---|---|
| $h(Tx,Ty) = h(x,y)$ | the defining property of a form isometry |
| $T^{\dagger}T = TT^{\dagger} = 1$ | the defining property of a unitary operator |
| $\mathrm{Iso}(A,h)$ | the isometry monoid of the form |
| $U(A,h)$ | the unitary group of the form, its group of units |
| $T^{\dagger} = T^{-1}$ on $U(A,h)$ | inversion is the restriction of the adjoint |
| $m_{u}^{\dagger} = m_{u^{*}}$, $m_{u} \in U(A,h) \iff u \in U(A)$ | the left multiplications and the unitary elements |
| $\alpha_{u} = uxu^{*}$, $\alpha_{u}^{\dagger} = \alpha_{u}^{-1}$ | the inner automorphisms are unitary operators |
| $\ker(u \mapsto \alpha_{u}) = U(A)\cap Z(A)$ | the central unitaries |
| $S^{*}S = 1$, $SS^{*} = 1-P_{0}$ | the unilateral shift, an isometry that is not unitary |
| $T^{*}JT = J$ | the defining property of a $J$-unitary operator, the indefinite isometry |
| $(1,1)$, $(8,0)$, $(2,6)$ | the signatures of the worked examples |

## Further Reading

- John B. Conway, *A Course in Functional Analysis* (2nd ed., Springer, 1990), for isometries, the unilateral shift, the defect operators and the unitary group of a Hilbert space.
- Paul R. Halmos, *A Hilbert Space Problem Book*, 2nd ed. (Springer, 1982), for isometries that are not unitary, the Wold decomposition and the unitary invariants.
- János Bognár, *Indefinite Inner Product Spaces* (Springer, 1974), for the isometry group of an indefinite inner product and the fundamental symmetry of an isometry.
- Israel Gohberg, Peter Lancaster and Leiba Rodman, *Indefinite Linear Algebra and Applications* (Birkhäuser, 2005), for the $J$-unitary group, the indefinite unitary groups $U(p,q)$ and the Lorentz boosts.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras I* (Academic Press, 1983), for the unitary group of an operator algebra, the inner automorphisms and the central unitaries.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the unitary groups of a module with a Hermitian form and the orthogonal groups of a symmetric form.
