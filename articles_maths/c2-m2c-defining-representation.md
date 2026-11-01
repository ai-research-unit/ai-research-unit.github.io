# __$M_2(\mathbb{C})$ Defining Representation__

## Introduction

**The model is shared and the subject is not.** The algebra $M_2(\mathbb{C})$ is the algebra of complex-linear endomorphisms of $\mathbb{C}^2$, and this article is about $\mathbb{C}^2$ and not about the algebra. The article fixes the space, the three structures it carries and the four readings those structures produce: the bilinear cone, the Hermitian cone, the spinor of the Lorentz group and the state space of the qubit. Every invariant of the algebra — its trace, its determinant, its Peirce decomposition, its conjugations — belongs to the biquaternion pair *$M_2(\mathbb{C})_{\mathbb{H}}$ Standard Representation*, and is cited here and never recomputed.

**Why one algebra carries two articles.** The duo-complex category is the only one whose matrix model is an algebra another category already owns. The collision is at the level of the model and not of the subject. There, the objects are the frame, the product, the trace, the determinant, the projectors and the norms **of the algebra**; here, they are the column, the real structure $J$, the three forms, the lines, the flags and the spinor **of the module**. After that division no section and no object is shared: one pair reads $\mathbb{B}\cong M_2(\mathbb{C})$ as a set of matrices, the other reads $\mathbb{C}^2$ as a space acted on. The name of the pair keeps the algebra in the title because the algebra is what provides the language, and the qualifier *defining* records that the subject is the defining module.

**Why the space matters.** The physics corpus is written against this carrier: the Weyl spinor of the Lorentz group, the pure state of the qubit and the null direction of a light ray are three readings of the same point set, distinguished only by the form that is used on it. The mathematics corpus had the space, the forms and the endomorphisms, but read none of the three readings. This article supplies the reading, and the operator face is the companion article *$M_2(\mathbb{C})$ Defining Representation : Operators*.

**The four readings at a glance.** No one of them is the others, and the table is the plan of the article.

| Reading | Structure used | Object | Dimension |
|---|---|---|---|
| the bilinear cone | the symmetric form $B$ and the dual space | the rank-one operators $u\phi^{\mathsf T}$, a quadric in $\mathbb{P}^3$ | complex $3$ |
| the Hermitian cone | the Hermitian form $H$ and the conjugation | the rank-one $uu^{\dagger}$, the future light cone | real $3$ |
| the spinor | the alternating form $\omega$ and the action of $\mathrm{SL}_2(\mathbb{C})$ | the Weyl spinor and its null vector | complex $2$ |
| the qubit | the definite $H$ and the action of $\mathrm{SU}(2)$ | the state space, the Bloch ball and its sphere | real $3$ |

**Boundaries.** The space, its two scalar structures, the complex structure $J$ and the norm are *Duo-Complex Numbers*; the three forms with their Gram matrices, their signatures and their isotropic sets are *The Three Canonical Forms on $\mathbb{C}^2$*; the realification and the real and imaginary parts are *The Realification of $\mathbb{C}^2$*; the lattice of subspaces, the dual and the incidence are *The Subspaces of $\mathbb{C}^2$*; the endomorphism algebra, the conjugate-linear maps, $\mathrm{GL}_2(\mathbb{C})$, $\mathrm{PGL}_2(\mathbb{C})$ and the centraliser of $J$ are *The Endomorphisms of $\mathbb{C}^2$*; the Hopf fibration is *The Unit Sphere and the Hopf Fibration*, the Grassmannians are *Grassmannians and Stiefel Manifolds*, and the general theory of holomorphic functions of two variables is *Several Complex Variables*. The operators $T_{u,\phi}$, their composition, their length and their adjoints are the companion article. Nothing of the algebra's own structure theory is repeated: the Peirce frame, the determinant of an element and the four norms are the biquaternion pair.

**Conventions.** The space is $V=\mathbb{C}^2$ with the complex basis $e_1,e_2$ and the coordinates
$$
u=u_{\blacktriangle}e_1+u_{\blacktriangledown}e_2,\qquad u_{\blacktriangle},u_{\blacktriangledown}\in\mathbb{C},
$$
written with the triangles of the category (*Duo-Complex Numbers*). The dual space is $V^{*}$ with the dual basis $\epsilon^{1},\epsilon^{2}$ and the row $\phi=\phi_{\blacktriangle}\epsilon^{1}+\phi_{\blacktriangledown}\epsilon^{2}$, so that the pairing is
$$
\phi(u)=\phi_{\blacktriangle}u_{\blacktriangle}+\phi_{\blacktriangledown}u_{\blacktriangledown},
$$
with **no conjugation**: the duality is complex bilinear. The three forms are
$$
H(u,v)=u_{\blacktriangle}\overline{v_{\blacktriangle}}+u_{\blacktriangledown}\overline{v_{\blacktriangledown}},\qquad
B(u,v)=u_{\blacktriangle}v_{\blacktriangle}+u_{\blacktriangledown}v_{\blacktriangledown},\qquad
\omega(u,v)=u_{\blacktriangle}v_{\blacktriangledown}-u_{\blacktriangledown}v_{\blacktriangle},
$$
so that $H$ is **linear in the first slot and conjugate-linear in the second**, the convention of the whole corpus and the opposite of the physicists' one. The dagger is $M^{\dagger}=\overline{M}^{\mathsf T}$, the transpose is $M^{\mathsf T}$, and the matrix units are $E_{jk}=e_je_k^{\mathsf T}$. A rank-one operator with a column in the left slot and a row in the right is written
$$
T_{u,\phi}=u\phi^{\mathsf T},\qquad T_{u,\phi}(v)=\phi(v)\,u .
$$

## The Column, the Dual and the Three Structures

**The space, its dual and the three forms are four objects on one carrier, and the article never uses one for another.**

### The Column and the Row

**Definition.** The **column** is the element $u\in V$ read as a list of two complex numbers, and the **row** is the element $\phi\in V^{*}$ read as a list of two complex numbers. The pairing $\phi(u)=\phi^{\mathsf T}u$ is the product of a row by a column and returns a scalar.

**The dual is not the space, and the identification is a choice.** There is no canonical isomorphism $V\cong V^{*}$ for a complex vector space: an isomorphism is the same thing as a nondegenerate bilinear or sesquilinear form, and $V$ carries three of them. Each gives its own identification, and the three are different maps.

| Form | Map $V\to V^{*}$ | Linearity | Image of $u$ |
|---|---|---|---|
| $B$ | $u\mapsto B(u,\cdot)$ | $\mathbb{C}$-linear | the row $u^{\mathsf T}$ |
| $\omega$ | $u\mapsto \omega(u,\cdot)$ | $\mathbb{C}$-linear | the row $u^{\mathsf T}J_2=(-u_{\blacktriangledown},u_{\blacktriangle})$, with $J_2=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$ |
| $H$ | $u\mapsto H(u,\cdot)$ | conjugate-linear | the row $u^{\dagger}$ |

**The three identifications differ, and the differences are the subject.** The first two are complex-linear and the third is not. The first is symmetric, the second alternating, and the rows they produce are $u^{\mathsf T}$ and a quarter turn of it. **A statement about "the dual vector" is incomplete until the form is named**, and the commonest confusion in the readings below is between the row $\bar u^{\mathsf T}$, which is the conjugate of $u$, and the row $u^{\mathsf T}$, which is $u$ itself.

### The Complex Structure

**Definition.** The **complex structure** is the real operator $J$ of multiplication by $i$, $J(u)=iu$ (*Duo-Complex Numbers*). On $V$ it is the scalar $iI_2$; on the realification $\mathbb{R}^4$ it is the block matrix with two copies of $\begin{pmatrix}0&-1\\1&0\end{pmatrix}$, and it satisfies
$$
J^{2}=-I_4 .
$$

**Proposition (the $\mathbb{C}$-linear maps are the maps that commute with $J$).** A real-linear $T:\mathbb{R}^4\to\mathbb{R}^4$ is complex-linear exactly when $TJ=JT$.

*Proof.* If $T$ is complex-linear then $T(iu)=iT(u)$, which is $TJ=JT$. Conversely, if $TJ=JT$ then $T((\alpha+i\beta)u)=\alpha T(u)+\beta T(Ju)=\alpha T(u)+\beta J T(u)=(\alpha+i\beta)T(u)$ for real $\alpha,\beta$, which is the complex linearity.

**The centraliser of $J$ in the real algebra is therefore the complex algebra.** The real endomorphism algebra of dimension sixteen splits as $\operatorname{End}_{\mathbb{C}}(V)\oplus\operatorname{Hom}_{\bar{\mathbb{C}}}(V,V)$, of dimensions $8+8$, and the centraliser of $J$ is the first summand (*The Endomorphisms of $\mathbb{C}^2$*, and *The Realification of $\mathbb{C}^2$*). **The operator $J$ is the single datum that makes the real reading complex, and it is invisible to every complex-linear statement.**

### The Three Structures

**Definition.** The three canonical forms of the carrier are $H$, $B$ and $\omega$ above. Their properties are proved in *The Three Canonical Forms on $\mathbb{C}^2$*; the table collects them with the two entries this article needs, the isometry group and the isotropic set.

| Form | Kind | Signature, realified | Isotropic set | Isometry group |
|---|---|---|---|---|
| $H$ | Hermitian, definite | $(4,0)$ | $\{0\}$ | $\mathrm{U}(2)$ |
| $B$ | symmetric bilinear | $(2,2)$ | two complex lines | $\mathrm{O}_2(\mathbb{C})$ |
| $\omega$ | alternating bilinear | symplectic | every complex line | $\mathrm{SL}_2(\mathbb{C})$ |

**Proposition (the isometry group of $\omega$ is the special linear group).** For every $A\in M_2(\mathbb{C})$,
$$
A^{\mathsf T}J_2A=\det(A)\,J_2 ,
$$
so $\omega(Au,Av)=\det(A)\,\omega(u,v)$, and $A$ preserves $\omega$ exactly when $\det A=1$.

*Proof.* Both sides are alternating bilinear forms in two variables, and such a form is a scalar multiple of $J_2$; the scalar is read at the pair $(e_1,e_2)$ and equals $e_1^{\mathsf T}A^{\mathsf T}J_2Ae_2=(Ae_1)^{\mathsf T}J_2(Ae_2)=\omega(Ae_1,Ae_2)=\det(A)$, by the multiplicativity of the determinant in the two columns. The invariance $\omega(Au,Av)=\det(A)\omega(u,v)$ follows by applying the identity to $u$ and $v$, and $\det(A)=1$ is then the condition.

**Remark (the readings and their forms).** The spinor reading uses $\omega$ and the real structure; the qubit reading uses the definite $H$; the two readings put the same matrices on the same carrier and **differ only in the form that is used**. The bilinear cone uses $B$ and the dual, the Hermitian cone uses $H$ and the dagger, and no reading uses two forms at once.

**Remark (three forms, three groups, three geometries).** The isometry group of $H$ is compact, that of $B$ is the complex orthogonal group of the split plane, and that of $\omega$ is the special linear group, which is the double cover of the Lorentz group developed below. **The same carrier carries a compact geometry, a split orthogonal geometry and a Lorentz geometry, and the choice of the form is the choice of the geometry.** No statement of this article is allowed to leave the form implicit.

### The Real and the Imaginary Parts

**The three complex forms produce six real forms, and the six are not new objects: they are the real and imaginary parts of the three.**

| Real form | Kind | Role |
|---|---|---|
| $\operatorname{Re}H$ | symmetric, positive definite | the Euclidean metric of $\mathbb{R}^4$ |
| $\operatorname{Im}H$ | alternating, of type $(1,1)$ | the Kähler form |
| $\operatorname{Re}B$ | symmetric, signature $(2,2)$ | the split metric |
| $\operatorname{Im}B$ | symmetric, signature $(2,2)$ | the second split metric |
| $\operatorname{Re}\omega$ | symplectic | the real symplectic form |
| $\operatorname{Im}\omega$ | symplectic | the second real symplectic form |

**The form $\operatorname{Im}H$ is not $\omega$.** The first is invariant under $J$ and the second changes sign, $\omega(Ju,Jv)=-\omega(u,v)$; the Kähler form of the space is $-\operatorname{Im}H$ and not $\omega$ (*The Three Canonical Forms on $\mathbb{C}^2$*). The distinction matters here because the two cones below are cut by $\operatorname{Re}H$ and by $\det$, and not by the alternating forms.

## The Lines, the Flags and the Projective Line

**A line is a point of the projective line, a rank-one Hermitian projector and a pure state, and the three descriptions are one object.**

### The Lines and Their Projectors

**Definition.** A **line** is a complex subspace $\ell\subset V$ of dimension one, that is $\ell=\mathbb{C}u$ for $u\neq0$. The **projector** of the line is
$$
\pi_{u}=\frac{uu^{\dagger}}{u^{\dagger}u},
$$
where $u^{\dagger}u=\lvert u_{\blacktriangle}\rvert^{2}+\lvert u_{\blacktriangledown}\rvert^{2}$ is the square of the norm.

**Proposition (the projector characterises the line).** The matrix $\pi_u$ is Hermitian, idempotent, of rank one and of trace one; its image is $\ell$ and its kernel is $\ell^{\perp}$, the orthogonal of $\ell$ for $H$. Conversely every Hermitian idempotent of rank one is $\pi_u$ for a unique line.

*Proof.* Hermitian: $(uu^{\dagger})^{\dagger}=uu^{\dagger}$. Idempotent: $uu^{\dagger}uu^{\dagger}=u(u^{\dagger}u)u^{\dagger}=(u^{\dagger}u)\,uu^{\dagger}$. Rank and trace: the image is $\ell$, so the rank is one and the trace is the sum of the eigenvalues, $1+0$. The kernel is $\{v:u^{\dagger}v=0\}=\ell^{\perp}$ because $H$ is definite. Conversely, a Hermitian idempotent of rank one has a one-dimensional image $\ell=\mathbb{C}u$ and acts as the identity there, so it is the orthogonal projector onto $\ell$, which is $\pi_u$.

**The projector is a point, a state and a line, and the three names are three readings of one matrix.** In the quantum reading of §*The Qubit and the Bloch Vector* the same matrix is the density matrix of a pure state; in the geometric reading of §*The Phase, the Hopf Fibration and the Flag* it is the point of $\mathbb{P}^1$; in the operator reading of the companion article it is the Hermitian member of the bilinear cone. **One matrix, three names, and no fourth object behind them.**

### The Projective Line

**Definition.** The **projective line** is $\mathbb{P}^{1}=(V\setminus\{0\})/\mathbb{C}^{\times}$, the set of lines. A point is written $[u]$, and a line is described in the affine chart $u_{\blacktriangle}\neq0$ by the coordinate
$$
\zeta=\frac{u_{\blacktriangledown}}{u_{\blacktriangle}},
$$
with the point at infinity for $u_{\blacktriangle}=0$.

**Proposition (the projective line is a sphere).** $\mathbb{P}^{1}$ is homeomorphic to $S^{2}$, and the homeomorphism is the Hopf map restricted to the unit sphere.

*Proof.* A line meets the unit sphere $S^{3}=\{\lVert u\rVert=1\}$ in a circle $u\mapsto e^{i\theta}u$, so $\mathbb{P}^{1}=S^{3}/S^{1}$, which is the Hopf fibration; the base is $S^{2}$ (*The Unit Sphere and the Hopf Fibration*). The affine coordinate $\zeta$ is the stereographic coordinate of the sphere, and the point at infinity is the north pole.

**The dual point and the incidence.** A nonzero row $\phi\in V^{*}$ defines the hyperplane $\{\phi=0\}$, which is a point $[\phi]$ of the dual projective line $(\mathbb{P}^{1})^{*}$. The pair $(u,\phi)$ is **incident** when $\phi(u)=0$, that is when the line $[u]$ lies in the hyperplane $\phi=0$, which in one projective dimension says that the point $[u]$ is exactly the kernel of $\phi$, that is the point of $\mathbb{P}^{1}$ dual to $[\phi]$. **The incidence is a single complex number and its vanishing is the only incidence relation of the line**: the two objects are a point and a dual point, and the incidence is the evaluation.

### The Flags

**Definition.** A **flag** is a pair $(\ell,r)$ of a line and a ray $r\subset\ell$, that is a half-line through the origin inside the line.

**Proposition (the flags are the unit sphere).** The set of flags is $S^{3}$, and the map flag $\mapsto$ line is the Hopf fibration, with fibre $S^{1}$.

*Proof.* A ray in $\ell$ meets the unit circle of $\ell$ in exactly one point, so a flag is the same thing as a unit vector $u$, the ray being $\mathbb{R}_{\ge0}u$. The map $u\mapsto[u]$ is the quotient by the phase, whose fibres are circles.

**The residual phase is the rotation of the half-plane.** Given the line, the flag is the choice of a ray inside it, and the circle of choices is the phase of $u$. **The phase is therefore not a redundancy of the description: it is the half-plane of the flag**, and the two readings of the same quotient — geometric and quantum — differ in what they call the fibre. This is developed in §*The Phase, the Hopf Fibration and the Flag*.

### The Dictionary

| Object | Description | Where it is used |
|---|---|---|
| $[u]$ | a line, a point of $\mathbb{P}^{1}$ | the projective geometry |
| $\pi_u$ | the Hermitian projector of rank one | the state of a system |
| $S^{3}\ni u$ | a unit column | the spinor, the flag |
| $u\phi^{\mathsf T}$ | a pair of a line and a dual line | a point of the bilinear cone |
| $uu^{\dagger}$ | a line with its conjugate row | a point of the Hermitian cone |

**Every row of the table is a point set, and no row is a vector space.** The cone is a cone, the sphere is a sphere and the ball of the qubit is a ball: **the carrier is a vector space and every one of its readings is not**, which is the structural reason the operator article of this pair has no identity and no inverses.

## The Bilinear Cone and the Segre Quadric

**The rank-one operators form a cone in the four-dimensional operator space, and its projectivisation is a quadric with two rulings.**

### The Cone

**Definition.** The **rank-one cone** of the carrier is
$$
\mathcal{C}=\{u\phi^{\mathsf T}:u\in V,\ \phi\in V^{*}\}\subset M_2(\mathbb{C}).
$$
It is the set of operators of rank at most one, and it is a cone: $\lambda\mathcal{C}=\mathcal{C}$ for every $\lambda\in\mathbb{C}$.

**Proposition (the criterion).** For $M\in M_2(\mathbb{C})$ the following are equivalent: $M\in\mathcal{C}$; $\operatorname{rank}M\le1$; $\det M=0$.

*Proof.* The rank is at most one exactly when the two columns are dependent, which is the existence of $\phi$ with $M=u\phi^{\mathsf T}$; for a matrix of size two the vanishing of the determinant is the same dependence. **The determinant is the special form the criterion takes at this size**, and the general statement is the rank inequality (*$M_4(\mathbb{C})$ Standard Peirce Representation* for the general size).

**Proposition (the cone is not a subspace, and its span is everything).** The four matrix units $E_{jk}$ are in $\mathcal{C}$, so the linear span of the cone is $M_2(\mathbb{C})$; the identity $I_2$ is not in $\mathcal{C}$, and it is the sum of two of its members.

*Proof.* $E_{jk}=e_je_k^{\mathsf T}$ is rank one. The identity has rank two and determinant one. And $I_2=E_{11}+E_{22}$.

**The failure of additivity is what the operator article turns on.** The cone is closed under multiplication and under scaling, and it is not closed under addition; the missing sums are exactly the matrices of rank two, and the identity is the smallest of them.

### The Segre Quadric

**Proposition (the projectivisation is a product of two lines).** The projectivisation of $\mathcal{C}$ is the **Segre quadric**
$$
\mathbb{P}^{1}\times\mathbb{P}^{1}\subset\mathbb{P}^{3},\qquad ([u],[\phi])\longmapsto[u\phi^{\mathsf T}],
$$
and the map is injective.

*Proof.* The matrix $u\phi^{\mathsf T}$ determines its image line $[u]$ and its kernel $\{\phi=0\}$, hence the pair; conversely the pair determines the matrix up to a scalar, which is the projectivisation. Two rank-one matrices with the same image and the same kernel are proportional, because both act as a scalar on the image.

**The two rulings.** For a fixed $[\phi]$ the family $[u\phi^{\mathsf T}]$ is a line in $\mathbb{P}^{3}$, and for a fixed $[u]$ the family is another line. **The quadric is thus ruled in two ways, and the two rulings are the two factors of the product.** A point of the quadric is a point of each ruling, and the pair of rulings is the pair (line, dual line).

**The equation of the quadric.** In the coordinates $(w_{11},w_{12},w_{21},w_{22})$ of the matrix-unit basis the quadric is
$$
\det M=w_{11}w_{22}-w_{12}w_{21}=0 .
$$

**Proposition (the determinant is a quadratic form of signature $(2,2)$).** The polar form of $\det$ is
$$
\langle M,N\rangle=\tfrac12\bigl(w_{11}z_{22}+z_{11}w_{22}-w_{12}z_{21}-z_{12}w_{21}\bigr),
$$
whose Gram matrix has the eigenvalues $\pm\tfrac12$, each twice; the cone $\mathcal{C}$ is the isotropic cone of the form.

*Proof.* The polar form is computed from $\det(M+N)-\det M-\det N$ and is symmetric and bilinear. In the basis $(E_{11},E_{12},E_{21},E_{22})$ its Gram matrix has $\tfrac12$ in the entries $(1,4)$ and $(4,1)$, $-\tfrac12$ in the entries $(2,3)$ and $(3,2)$, and zero elsewhere; with the ordering $(E_{11},E_{22},E_{12},E_{21})$ it is block diagonal, with the blocks $\tfrac12\begin{pmatrix}0&1\\1&0\end{pmatrix}$ and $-\tfrac12\begin{pmatrix}0&1\\1&0\end{pmatrix}$, so its eigenvalues are $\pm\tfrac12$ twice each and the signature is $(2,2)$. The isotropic set of the form is $\det M=0$.

### The Isotropic Lines

**The alternating form has no isotropic line and the symmetric form has two, and the two are visible on the cone.**

**Remark (the automatic vanishing of $\omega$).** Because $\omega$ is alternating, $u^{\mathsf T}J_2u=0$ for every $u$. **The identity $u^{\mathsf T}J_2u=0$ is therefore not a condition and defines no subset**: the isotropic lines that cut the cone are those of the symmetric form $B$, and they are the solutions of $u^{\mathsf T}u=u_{\blacktriangle}^{2}+u_{\blacktriangledown}^{2}=0$.

**Definition.** The **isotropic lines** of $B$ are $\ell_{\pm}=\mathbb{C}(e_1\pm ie_2)$, and they are the only two: $u_{\blacktriangledown}^{2}=-u_{\blacktriangle}^{2}$ forces $u_{\blacktriangledown}=\pm iu_{\blacktriangle}$.

**Proposition (the isotropic columns and the transpose square).** For $T=T_{u,\phi}=u\phi^{\mathsf T}$ and $\sigma=u^{\mathsf T}u$,
$$
T^{\mathsf T}T=\sigma\,\phi\phi^{\mathsf T},\qquad TT^{\mathsf T}=\tau\,uu^{\mathsf T},\quad \tau=\phi^{\mathsf T}\phi ,
$$
so $T^{\mathsf T}T=0$ exactly when the column $u$ lies on one of the two isotropic lines, and $TT^{\mathsf T}=0$ exactly when the row $\phi$ lies on one of the two isotropic lines of the dual.

*Proof.* $T^{\mathsf T}=\phi u^{\mathsf T}$, so $T^{\mathsf T}T=\phi\,(u^{\mathsf T}u)\,\phi^{\mathsf T}=\sigma\,\phi\phi^{\mathsf T}$, the scalar commuting with the two columns. The matrix $\phi\phi^{\mathsf T}$ is nonzero for $\phi\neq0$, so the vanishing is exactly $\sigma=0$, which is the isotropy of the column; the second statement is the same computation with the two slots exchanged.

**The isotropic columns are the null directions of the operator.** A member of the cone with an isotropic column has $T^{\mathsf T}T=0$, hence is **isotropic** for the transpose form of the operator space, $\langle T,T\rangle=\operatorname{tr}(T^{\mathsf T}T)=0$. **This is isotropy and not nilpotence**: $T^{2}=\phi(u)T$ vanishes only when $\phi(u)=0$, which is a second condition on the row and not on the column, so a member with an isotropic column and $\phi(u)\neq0$ is a rank-one matrix that is null without being nilpotent. **The two isotropic lines of $B$ are therefore the two directions on which the operator becomes null for the transpose form**, and this is the only place where the isotropy of $B$ is visible as a property of an operator rather than as a property of a vector.

**Remark (the same signature, and no natural identification).** The signature is the one of $\operatorname{Re}B$ on $V$, and the coincidence is not an accident of arithmetic: both are the split form in four real dimensions. **It is not an identification of the two spaces**, because $\det$ is a form on the operator space and $B$ is a form on the carrier, and no canonical map exchanges them beyond the rank-one correspondence itself.

## The Hermitian Cone and the Light Cone

**The Hermitian rank-one matrices form a second cone in the same operator space, of real dimension three, and it is the future light cone read through the Pauli basis.**

### The Cone

**Definition.** The **Hermitian cone** is
$$
\mathcal{C}_{H}=\{uu^{\dagger}:u\in V\}\subset M_2(\mathbb{C}).
$$
Its members are the positive semidefinite matrices of rank at most one.

**Proposition (the two invariants).** For every $u$,
$$
\det(uu^{\dagger})=0,\qquad \operatorname{tr}(uu^{\dagger})=u^{\dagger}u=\lVert u\rVert^{2}.
$$

*Proof.* The determinant of a rank-one matrix is zero. The trace of $uu^{\dagger}$ is $\sum_{j,k}u_ju_k^{\dagger}\delta_{jk}=\sum_j\lvert u_j\rvert^{2}$.

**Proposition (the cone is the fixed locus of the dagger inside the bilinear cone).** Let $T_{u,\phi}=u\phi^{\mathsf T}$ be a nonzero member of $\mathcal{C}$. Then
$$
T_{u,\phi}^{\dagger}=T_{u,\phi}\iff \phi=c\,\bar u\ \text{ with }c\in\mathbb{R},
$$
and in that case $T_{u,\phi}=c\,uu^{\dagger}$. The fixed locus is therefore the real line through the Hermitian cone.

*Proof.* The adjoint is $\bar\phi u^{\mathsf T}$. Two rank-one matrices are equal exactly when their columns are proportional and their rows are proportional with the reciprocal scalar; the equality $u\phi^{\mathsf T}=\bar\phi u^{\mathsf T}$ gives $\phi=c\bar u$ and $\bar\phi=\alpha u$ for scalars $c,\alpha$, and the two displays $u\phi^{\mathsf T}=c\,u\bar u^{\mathsf T}$ and $\bar\phi u^{\mathsf T}=\alpha\,u\bar u^{\mathsf T}$ force $\alpha=c$, while conjugating $\phi=c\bar u$ gives $\alpha=\bar c$, so $c=\bar c$. Conversely, $c$ real gives $u(c\bar u)^{\mathsf T}=c\,u\bar u^{\mathsf T}=c\,uu^{\dagger}$, which is Hermitian.

**The fixed locus is a real line through the cone.** The Hermitian cone itself is the positive part of the fixed locus, and the negative part is the cone of the negative semidefinite matrices of rank one. **The dagger is conjugate-linear, and that is why the second cone exists at all**: the bilinear cone is the cone of a complex-bilinear object and the Hermitian cone is the cone of a sesquilinear one, the adjoint is the only structure of the space that mixes the two, and the mixing produces a real locus.

### The Pauli Coordinates

**Definition.** The **Pauli matrices** are
$$
\sigma_0=I_2,\qquad
\sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
\sigma_2=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\qquad
\sigma_3=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
$$
They are Hermitian, $\sigma_1^{2}=\sigma_2^{2}=\sigma_3^{2}=I_2$, they anticommute in pairs, and $\sigma_1\sigma_2=i\sigma_3$ with the cyclic permutations.

**Proposition (the coordinates).** Every Hermitian $M$ is
$$
M=t\,\sigma_0+x\,\sigma_1+y\,\sigma_2+z\,\sigma_3,\qquad
t=\tfrac12\operatorname{tr}M,\quad x=\tfrac12\operatorname{tr}(\sigma_1M),\quad y=\tfrac12\operatorname{tr}(\sigma_2M),\quad z=\tfrac12\operatorname{tr}(\sigma_3M),
$$
with the four coefficients real, and
$$
\det M=t^{2}-x^{2}-y^{2}-z^{2},\qquad \operatorname{tr}M=2t .
$$

*Proof.* The four matrices form a real basis of the four-dimensional real space of Hermitian matrices, being Hermitian, independent and four in number. The determinant identity is the computation of $\det(t\sigma_0+\vec x\cdot\vec\sigma)$ using $\sigma_j^{2}=I$, the pairwise anticommutation and $\operatorname{tr}\sigma_j=0$, which gives the quadratic form of signature $(1,3)$; the trace is $2t$ because the three Pauli matrices are traceless.

**Theorem (the Hermitian cone is the future light cone).** The map
$$
u\longmapsto\bigl(t,x,y,z\bigr)=\tfrac12\bigl(\operatorname{tr}(uu^{\dagger}),\operatorname{tr}(\sigma_1uu^{\dagger}),\operatorname{tr}(\sigma_2uu^{\dagger}),\operatorname{tr}(\sigma_3uu^{\dagger})\bigr)
$$
takes values in the closed future cone
$$
t^{2}-x^{2}-y^{2}-z^{2}=0,\qquad t\ge0,
$$
and it is onto that cone; the trace is $\lVert u\rVert^{2}=2t$.

*Proof.* The determinant identity gives the equation, and the trace gives $2t=\lVert u\rVert^{2}\ge0$. Surjectivity: a nonzero point of the cone has $t>0$ and $\lvert\vec x\rvert=t$, and a column of norm $\sqrt{2t}$ whose Bloch direction is $\vec x/t$ realizes it, as §*The Qubit and the Bloch Vector* shows.

**The dimension count.** The cone is a cone over $S^{2}$, of real dimension three, and it sits inside the four-dimensional real space of Hermitian matrices as a hypersurface: the determinant is one real equation. **The bilinear cone is of complex dimension three, that is real dimension six, and the two cones are of different sizes although both are cut by a determinant.**

### The Two Cones Compared

| | bilinear cone $\mathcal{C}$ | Hermitian cone $\mathcal{C}_{H}$ |
|---|---|---|
| members | $u\phi^{\mathsf T}$ | $uu^{\dagger}$, positive semidefinite |
| ambient | $M_2(\mathbb{C})$, real dimension $8$ | the Hermitian subspace, real dimension $4$ |
| equation | $\det M=0$ | $\det M=0$ on the Hermitian subspace |
| dimension | complex $3$, real $6$ | real $3$ |
| projectivisation | $\mathbb{P}^{1}\times\mathbb{P}^{1}$ | $\mathbb{P}^{1}$ |
| rulings | two, independent | one, the diagonal |
| parameter | $(u,\phi)$ modulo the scaling | $u$ modulo the phase |
| fixed by | nothing | the dagger |
| adjoint family | $T_{\phi,u}$ | itself |

**The collapse of the two rulings to one is the phase quotient.** In the bilinear cone the line of the column and the line of the row are independent, so the projectivisation has two factors. In the Hermitian cone the row is the conjugate of the column, $\phi=\bar u$, so the second factor is determined by the first up to the phase, and the diagonal $[\phi]=[\bar u]$ is a single $\mathbb{P}^{1}$. **The conjugation is what identifies the two rulings, and there is no other identification.**

## The Spinor and the Two Actions

**The space is the defining module of $\mathrm{SL}_2(\mathbb{C})$, the spinor of the Lorentz group and the state space of $\mathrm{SU}(2)$; the two cones are the two projective homogeneous spaces, $\mathbb{P}^{1}\times\mathbb{P}^{1}$ for the complex group and $\mathbb{P}^{1}$ for the compact one.**

### The Two Modules

**Definition.** The group $\mathrm{SL}_2(\mathbb{C})$ acts on $V$ by $u\mapsto Au$. The **conjugate module** $\bar V$ is the same real space with the conjugate complex structure, $\lambda\cdot u=\bar\lambda u$, and it carries the action $u\mapsto\bar A u$.

**Proposition (the two modules are not isomorphic as complex modules).** There is no complex-linear isomorphism $V\to\bar V$ commuting with $\mathrm{SL}_2(\mathbb{C})$, although the two are isomorphic as real spaces.

*Proof.* Compare the weights of the diagonal torus. An element $A=\operatorname{diag}(\lambda,\lambda^{-1})$ acts on $V$ with the eigenvalues $\lambda,\lambda^{-1}$ and on $\bar V$ with $\bar\lambda,\bar\lambda^{-1}$. An intertwiner would preserve the eigenvalue set, so $\{\lambda,\lambda^{-1}\}=\{\bar\lambda,\bar\lambda^{-1}\}$ for every $\lambda\in\mathbb{C}^{\times}$, which already fails for $\lambda=2i$, where the two sets are $\{2i,-\tfrac{i}{2}\}$ and $\{-2i,\tfrac{i}{2}\}$. **The spinor and its conjugate are two different modules over the same group**, and the difference is the reality of the coefficients and not the dimension.

**The self-duality through $\omega$.** Because $\omega$ is nondegenerate and $\mathrm{SL}_2(\mathbb{C})$ preserves it, the map $u\mapsto\omega(u,\cdot)$ is an isomorphism of modules $V\to V^{*}$. **The dual module is the module**, and this is why a spinor can be contracted with a spinor without a conjugate: the pairing $\omega(u,v)$ is the invariant scalar, and it is alternating.

### The Types

**Definition.** The module $V$ is the **Weyl spinor** of type $(\tfrac12,0)$ and the conjugate module $\bar V$ is of type $(0,\tfrac12)$; the pair $(V,\bar V)$ is a single Dirac spinor read in the chiral basis.

**A spinor is a pair of conjugate scalars and not two independent scalars.** The statement is the substance of the difference between this category and the algebra $\mathbb{C}\times\mathbb{C}$: an element of $\mathbb{C}\times\mathbb{C}$ is two independent complex numbers, and an element of $V$ is two complex numbers that transform under $A$, with the conjugate module transforming under $\bar A$. **The two components are tied by the reality of the Lorentz vector they produce**, which is the content of the next proposition.

### The Null Vector of a Spinor

**Theorem (the spinor produces a null vector).** For $A\in\mathrm{SL}_2(\mathbb{C})$ and $u\in V$,
$$
(Au)(Au)^{\dagger}=A\,uu^{\dagger}\,A^{\dagger},
$$
and there is a unique proper orthochronous Lorentz transformation $\Lambda(A)$ with
$$
\Lambda(A)\cdot\bigl(t,\vec x\bigr)=\bigl(t',\vec x'\bigr)
$$
where $(t',\vec x')$ are the Pauli coordinates of $Auu^{\dagger}A^{\dagger}$. The map $A\mapsto\Lambda(A)$ is a surjective homomorphism of kernel $\{\pm I_2\}$.

*Proof.* The identity is the multiplicativity of the dagger. Put $\Lambda(M)=AMA^{\dagger}$; it is a real-linear map of the Hermitian space into itself, and
$$
\det\Lambda(M)=\lvert\det A\rvert^{2}\det M=\det M,
$$
so $\Lambda$ preserves the quadratic form $Q(M)=t^{2}-\lvert\vec x\rvert^{2}$ of the Pauli coordinates; as $Q$ is nondegenerate, $\Lambda$ is in $\mathrm{O}(1,3)$. It preserves the future cone as well, because $t(\Lambda M)=\tfrac12\operatorname{tr}(AMA^{\dagger})=\tfrac12\operatorname{tr}(A^{\dagger}AM)>0$ for every nonzero positive semidefinite $M$, the product $A^{\dagger}A$ being positive definite; and $\mathrm{SL}_2(\mathbb{C})$ is connected, so the image lies in the identity component $\mathrm{SO}^{+}(1,3)$ and not in a component that could reverse the time orientation. The kernel is $\{\pm I_2\}$: the equality $Au u^{\dagger}A^{\dagger}=uu^{\dagger}$ for every $u$ restricts to $u=e_1,e_2$ and forces the columns of $A$ to be of modulus one on their own support, hence forces $A$ to be diagonal with unimodular entries, and $u=e_1+e_2$ forces the two phases to be equal, so $A=\lambda I_2$ with $\lvert\lambda\rvert=1$ and $\lambda^{2}=\det A=1$. Surjectivity on $\mathrm{SO}^{+}(1,3)$ is the classical statement of the double cover (*Biquaternion Rotations and Lorentz Transformations*, and *$M_2(\mathbb{C})_{\mathbb{H}}$ Standard Representation* for the biquaternion side).

**The phase quotients and the sign covers.** The null vector of $u$ depends only on the line $[u]$, so the map from the sphere of unit columns to the set of null rays is the Hopf fibration, of fibre the phase circle $S^{1}$, and the sign $\pm1$ is one point of that circle. The double cover of the Lorentz group is a statement about the group and not about the sphere: $A$ and $-A$ produce the same $\Lambda$, and correspondingly $u$ and $-u$ produce the same null vector. **The ambiguity of the spinor and the kernel of the covering are therefore the same $\mathbb{Z}_2$, and both sit inside the phase circle that the null vector quotients.**

### The Four Actions

| Group | Preserves | Acts on | Kernel on $\mathbb{P}^{1}$ | Real dimension |
|---|---|---|---|---|
| $\mathrm{GL}_2(\mathbb{C})$ | the bilinear cone, all of it | $V$ and $V^{*}$ | $\mathbb{C}^{\times}$ | $8$ |
| $\mathrm{SL}_2(\mathbb{C})$ | $\omega$, the bilinear cone | $V$ | $\{\pm I_2\}$ | $6$ |
| $\mathrm{U}(2)$ | $H$ and the Hermitian cone | $V$ | $\mathrm{U}(1)$ | $4$ |
| $\mathrm{SU}(2)$ | $H$, $\det$, the Hermitian cone | $V$ | $\{\pm I_2\}$ | $3$ |

**Proposition (the invariance of the two cones).** For $A\in\mathrm{GL}_2(\mathbb{C})$ and $T\in\mathcal{C}$, the conjugate $ATA^{-1}$ is in $\mathcal{C}$; for $B\in\mathrm{GL}_2(\mathbb{C})$ and $M\in\mathcal{C}_{H}$, the matrix $BMB^{\dagger}$ is in $\mathcal{C}_{H}$.

*Proof.* $Au\phi^{\mathsf T}A^{-1}=(Au)(\phi^{\mathsf T}A^{-1})$ is rank one, and $Buu^{\dagger}B^{\dagger}=(Bu)(Bu)^{\dagger}$ is positive semidefinite of rank one.

**Two invariance statements and two groups.** The bilinear cone is invariant under conjugation, which is an action of the group on the operator space, and the Hermitian cone is invariant under congruence, which is another action of the same group. **The two actions differ, and the difference is again the dagger**: one uses $A^{-1}$ and the other $A^{\dagger}$.

## The Qubit and the Bloch Vector

**The trace-one slice of the positive cone is a closed ball, its boundary is the Bloch sphere, and the pure states are the boundary.**

### The States

**Definition.** A **state** is a Hermitian positive semidefinite matrix $\rho$ of trace one. A state is **pure** when its rank is one and **mixed** otherwise.

**Proposition (the pure states are the lines).** The pure states are exactly the projectors $\pi_u$ of §*The Lines and Their Projectors*, and two columns give the same state exactly when they differ by a phase.

*Proof.* A positive semidefinite matrix of trace one and rank one has the single eigenvalue one, hence is the orthogonal projector onto its image, which is $\pi_u$; and $\pi_{\lambda u}=\pi_u$ because the phase cancels between the numerator and the denominator.

### The Bloch Ball

**Proposition (the trace-one slice is the ball).** With the Pauli coordinates $(t,\vec x)$ of a Hermitian matrix, the state condition is
$$
t=\tfrac12,\qquad \lvert\vec x\rvert\le\tfrac12 ,
$$
so the states are the closed ball of radius $\tfrac12$ in the affine hyperplane $t=\tfrac12$, and the pure states are its boundary sphere of radius $\tfrac12$.

*Proof.* Positivity of $t\sigma_0+\vec x\cdot\vec\sigma$ with $t=\tfrac12$ is the pair of conditions $\tfrac12\ge0$ and $\det\ge0$, that is $\tfrac14-\lvert\vec x\rvert^{2}\ge0$; the rank is one exactly on the boundary, where the determinant vanishes and the trace is nonzero.

**Definition.** The **Bloch vector** is $\vec r=2\vec x$, so that
$$
\rho=\tfrac12\bigl(\sigma_0+\vec r\cdot\vec\sigma\bigr),\qquad \lvert\vec r\rvert\le1 .
$$

**Proposition (purity is the unit sphere).** For every state,
$$
\operatorname{tr}\rho^{2}=\tfrac12\bigl(1+\lvert\vec r\rvert^{2}\bigr),
$$
so $\rho$ is pure exactly when $\lvert\vec r\rvert=1$ and maximally mixed exactly when $\vec r=0$.

*Proof.* The square of $\rho$ is $\tfrac14(\sigma_0+2\vec r\cdot\vec\sigma+\lvert\vec r\rvert^{2}\sigma_0)$ using the anticommutation and $\operatorname{tr}\sigma_j=0$ for the cross terms, and the trace of $\sigma_0$ is two; the result follows.

**Theorem (the Bloch sphere is the projective line).** The boundary of the ball is $S^{2}=\mathbb{P}^{1}$, and the identification is the one of §*The Projective Line*: a pure state is a line, the line is a point of $\mathbb{P}^{1}$, and $\mathbb{P}^{1}$ is a sphere.

*Proof.* The boundary is the projectivised Hermitian cone, which is $\mathbb{P}^{1}$ by §*The Two Cones Compared*, and $\mathbb{P}^{1}\cong S^{2}$ by the Hopf map.

### The Dictionary of the Reading

| Mathematics | Quantum reading |
|---|---|
| a line $\ell\subset V$ | a pure state |
| the projector $\pi_u$ | the density matrix of a pure state |
| a general state $\rho$ | a mixed state |
| $\operatorname{tr}\rho^{2}$ | the purity |
| $1-\operatorname{tr}\rho^{2}$ | the linear entropy |
| the boundary of the ball | the pure states |
| the interior of the ball | the mixed states |
| the centre $\rho=\tfrac12\sigma_0$ | the maximally mixed state |
| $\mathbb{P}^{1}\cong S^{2}$ | the Bloch sphere |
| $\mathrm{SU}(2)$ modulo $\pm I_2$ | the rotation group of the sphere |

**The reading adds nothing to the mathematics and it changes the emphasis.** The mathematics has the cone, the slice and the projector; the reading names the slice a state space and the boundary a sphere of states. **What it does not have, and what the reading supplies, is the reason the sphere is the right picture**: a state is a line, the lines are a sphere, and the mixed states are the interior because they are the convex combinations of the pure ones.

## The Phase, the Hopf Fibration and the Flag

**The unit sphere of the carrier fibres over the projective line, and the fibre is the flag's half-plane.**

### The Fibration

**Theorem (Hopf).** The map
$$
\pi:S^{3}\longrightarrow S^{2},\qquad u\longmapsto[u],
$$
is a fibre bundle with fibre $S^{1}$, and its fibres are the phase circles $u\mapsto e^{i\theta}u$.

*Proof.* The quotient of $S^{3}$ by the free action of $S^{1}$ by phase is $\mathbb{P}^{1}$, which is $S^{2}$; local triviality is the standard statement, and the explicit trivialisation is the stereographic chart of the projective line (*The Unit Sphere and the Hopf Fibration*).

**The three descriptions of a point of $S^{3}$.** A unit column is a flag: a line and a ray inside it. It is also a normalized spinor, and also a point of the total space of the fibration. **The three descriptions are one object, and the fibration says how the descriptions are related**: the base is the line, the fibre is the rotation of the half-plane inside the line.

### The Effect on the Two Cones

**Proposition (the phase quotient acts differently on the two cones).** The scaling $u\mapsto\lambda u$ with $\lvert\lambda\rvert=1$, together with the compensating $\phi\mapsto\lambda^{-1}\phi$, fixes every point of the bilinear cone; the scaling $u\mapsto\lambda u$ alone fixes every point of the Hermitian cone, without any compensation.

*Proof.* $(\lambda u)(\lambda^{-1}\phi)^{\mathsf T}=u\phi^{\mathsf T}$; and $(\lambda u)(\lambda u)^{\dagger}=\lvert\lambda\rvert^{2}uu^{\dagger}=uu^{\dagger}$.

**The two statements look alike and are not.** In the first the phase acts on the two slots with opposite exponents, so the phase is a symmetry of the parametrisation and the two rulings stay independent. In the second the phase acts on the single slot and cancels against its own conjugate, so **the second ruling is not a ruling at all**: the row is the conjugate of the column, the phase is quotiented, and the projectivised cone is one $\mathbb{P}^{1}$ and not a product.

**Remark (the flag and the collapse).** In the Hermitian reading the second ruling is the conjugate of the first, so the phase is quotiented and the flag disappears from the description; in the bilinear reading the phase is compensated in the second slot and survives as the half-plane of the column. **The same circle is a gauge in one reading and a flag in the other.**

## Summary

The carrier of this pair is the module $V=\mathbb{C}^{2}$, of complex dimension two and real dimension four, and the article reads it through the three canonical forms. The Hermitian form $H$ is definite, of realified signature $(4,0)$, with isometry group $\mathrm{U}(2)$; the symmetric form $B$ is indefinite of signature $(2,2)$, with isometry group $\mathrm{O}_2(\mathbb{C})$ and isotropic set two complex lines; the alternating form $\omega$ is nondegenerate, with isometry group $\mathrm{SL}_2(\mathbb{C})$ because $A^{\mathsf T}J_2A=\det(A)J_2$, and every complex line is isotropic for it. Each of the three gives its own identification $V\to V^{*}$, and the third is the one that differs in linearity: $B$ and $\omega$ are complex bilinear and $H$ is sesquilinear.

A line is a point of $\mathbb{P}^{1}$, a rank-one Hermitian projector $\pi_u=uu^{\dagger}/(u^{\dagger}u)$, and a pure state; the projective line is $S^{2}$; a flag is a line with a ray, that is a unit column, and the flags are $S^{3}$ with the Hopf fibration over the lines. The rank-one operators $u\phi^{\mathsf T}$ form a cone of complex dimension three whose projectivisation is the Segre quadric $\mathbb{P}^{1}\times\mathbb{P}^{1}$, with the determinant as its equation and as a quadratic form of signature $(2,2)$; the cone spans the operator space although the identity is not in it. The Hermitian rank-one matrices $uu^{\dagger}$ form a cone of real dimension three which is the fixed locus of the dagger inside the bilinear cone up to a real scale, with $\det=0$ and $\operatorname{tr}=\lVert u\rVert^{2}$, and which the Pauli coordinates identify with the future light cone $t^{2}-\lvert\vec x\rvert^{2}=0$, $t\ge0$. The two cones differ in dimension, in projectivisation and in their rulings, and the collapse of the two rulings to one is the phase quotient.

The space is the defining module of $\mathrm{SL}_2(\mathbb{C})$, the Weyl spinor of type $(\tfrac12,0)$, and its conjugate is the second module of the pair; the duality through $\omega$ makes the dual module the module itself, and a spinor produces a null vector by $u\mapsto uu^{\dagger}$, with the double cover of the Lorentz group of kernel $\{\pm I_2\}$ and the two signs of the spinor giving the same vector. On the trace-one slice the positive cone is the Bloch ball, the Bloch vector is $\vec r=2\vec x$, the purity is $\operatorname{tr}\rho^{2}=\tfrac12(1+\lvert\vec r\rvert^{2})$, and the pure states are the unit sphere, which is the projective line. The operators of the carrier, one-sided and two-sided, their composition, their length and their adjoints, are the companion article *$M_2(\mathbb{C})$ Defining Representation : Operators*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $V=\mathbb{C}^{2}$ | the carrier, of complex dimension $2$ and real dimension $4$ |
| $e_1,e_2$ | the complex basis |
| $u_{\blacktriangle},u_{\blacktriangledown}$ | the two complex coordinates |
| $V^{*}$, $\phi$ | the dual and the row |
| $\phi(u)=\phi^{\mathsf T}u$ | the pairing, complex bilinear |
| $J$, $J_2$ | multiplication by $i$; the alternating matrix $\begin{pmatrix}0&1\\-1&0\end{pmatrix}$ |
| $H$, $B$, $\omega$ | the Hermitian, the symmetric bilinear and the alternating forms |
| $M^{\dagger}$, $M^{\mathsf T}$ | the conjugate transpose and the transpose |
| $E_{jk}$ | the matrix units $e_je_k^{\mathsf T}$ |
| $T_{u,\phi}=u\phi^{\mathsf T}$ | the rank-one operator with column $u$ and row $\phi$ |
| $\mathcal{C}$ | the bilinear rank-one cone |
| $\mathcal{C}_{H}$ | the Hermitian rank-one cone |
| $\pi_u$ | the projector $uu^{\dagger}/(u^{\dagger}u)$ |
| $\mathbb{P}^{1}$ | the projective line, the set of complex lines |
| $\zeta$ | the affine coordinate $u_{\blacktriangledown}/u_{\blacktriangle}$ |
| $\sigma_0,\sigma_1,\sigma_2,\sigma_3$ | the Pauli basis of the Hermitian matrices |
| $t,x,y,z$ | the Pauli coordinates, $t=\tfrac12\operatorname{tr}M$ |
| $\vec r=2\vec x$ | the Bloch vector |
| $\rho$ | a state, Hermitian positive semidefinite of trace one |
| $\Lambda(A)$ | the Lorentz transformation of $A\in\mathrm{SL}_2(\mathbb{C})$ |
| $\ell$, $r$ | a line and a ray, that is a flag |

## Further Reading

*Duo-Complex Numbers* fixes the space, its two scalar structures, the complex structure and the norm, and is the entry point of the category. *The Three Canonical Forms on $\mathbb{C}^2$* proves the properties of $H$, $B$ and $\omega$, their Gram matrices, their signatures and their isotropic sets. *The Realification of $\mathbb{C}^2$* gives the real picture, the six real forms and the decomposition of the real endomorphism algebra. *The Subspaces of $\mathbb{C}^2$* carries the lattice, the flag, the dual, the Grassmannians and the isotropic and Lagrangian subspaces. *The Endomorphisms of $\mathbb{C}^2$* carries the algebra $M_2(\mathbb{C})$, the conjugate-linear maps, $\mathrm{GL}_2(\mathbb{C})$, $\mathrm{PGL}_2(\mathbb{C})$, the centraliser of $J$ and the biquaternion identification. *The Unit Sphere and the Hopf Fibration* carries the fibration, and *Grassmannians and Stiefel Manifolds* the general Grassmannian picture of which $\mathbb{P}^{1}$ is the first case.

On the algebra side, *$M_2(\mathbb{C})_{\mathbb{H}}$ Standard Representation* and its operators companion read $\mathbb{B}\cong M_2(\mathbb{C})$ as a set of matrices, with the frame, the Peirce decomposition, the trace, the determinant, the projectors, the adjugate and the norms. The companion of this article is *$M_2(\mathbb{C})$ Defining Representation : Operators*, which treats $T_{u,\phi}$ as an operator, its composition, its length, its adjoints and the two cones as sets of operators. For the general size, *$M_4(\mathbb{C})$ Standard Peirce Representation* gives the rank criterion and the determinantal variety, of which §*The Bilinear Cone and the Segre Quadric* is the two-dimensional case. For the analysis of the space, *Several Complex Variables* is the general theory and *Analysis on $\mathbb{C}^2$* its two-variable case.
