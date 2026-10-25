# __The Krein Isometry Group and Its Cartan Decomposition__

## Introduction

The isometries of the general quaternionic sesquilinear form make up the **Krein isometry group** $U_{J}(\mathbb{B})$ of the biquaternion algebra, and its shape is the surprise of the indefinite theory: it is not compact, it is not the group $\mathrm{U}(2)$ that the two-sided structure of the algebra might suggest, and it contains the Lorentz boosts of the Lorentzian slices among its elements. The group is $\mathrm{U}(1,3)$; this article computes it on the elements and on the operators, and the two readings are the two halves of its Cartan theory. On the elements: the definition and the criterion, the algebraic isometries among the three operator families of the corpus, the spectrum, the boosts and the transitive actions. On the operators: the three adjoints of the operator algebra, the **Krein decomposition** $\mathfrak{g}=\mathfrak{k}\oplus\mathfrak{p}$ into the $J$-skew and the $J$-self-adjoint operators, the two involutions of the group, the trace form and the $J$-contractions.

The two involutions are the point of the article. The **Krein involution** $\theta_{J}(T)=(T^{\dagger})^{-1}$ is built from the indefinite adjoint $T^{\dagger}=JT^{*}J$, and its fixed group is $U_{J}(\mathbb{B})$ itself: it is not a Cartan involution, since its fixed group is non-compact. The **Cartan involution** $\theta_{0}(T)=(T^{*})^{-1}$ is built from the definite adjoint, and its restriction to $U_{J}(\mathbb{B})$ has the maximal compact group $\mathrm{U}(1)\times \mathrm{U}(3)$ for fixed group; its symmetric space is the complex hyperbolic space $\mathbb{CH}^{3}$ of *The Krein Level Sets and the Hyperbolic Structure*. The two involutions carry the same group, one as the fixed group and one as the ambient group, and the comparison of their fixed algebras is the comparison of $\mathfrak{u}(1,3)$ with $\mathfrak{u}(4)$.

The general theory of isometries is *Unitary and Isometric Operators of the Form*, which proves that the isometry monoid is the unitary group in finite dimension; the general theory of $\mathrm{U}(n,m)$, its Cartan involution and its bounded realisation is *The Unitary Group and the Hermitian Symmetric Space*; the four pairings, their Gram matrices and their isometry groups are *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*; the adjoints of the three families and the indefinite spectral data are *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra*; the form and its Gram matrix are *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*; the null set and the Krein cone are *K-Regularity and Degeneracy in the Biquaternion Algebra*; and the indefinite sandwich that uses the group is *The Indefinite Hermitian Sandwich on the General Quaternionic Sesqualgebra*.

Throughout, $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with the basis $e_t,\vec e_x,\vec e_y,\vec e_z$, the coefficient Gram matrix is $E=\operatorname{diag}(1,-1,-1,-1)$, the natural conjugation is $J={}^{\natural}=E$, and the indefinite adjoint is $T^{\dagger}=JT^{*}J$. The operator algebra is $\mathfrak{g}=\operatorname{End}_{\mathbb{C}}(\mathbb{B})\cong\mathfrak{gl}_{4}(\mathbb{C})\cong M_{4}(\mathbb{C})$, of real dimension $32$.

## The Group of Krein Isometries

**Definition.** A **Krein isometry**, or a **$J$-unitary operator**, is a $\mathbb{C}$-linear operator $T$ with

$$
\langle T\tilde Q_2,T\tilde Q_1\rangle_{\natural*}=\langle\tilde Q_2,\tilde Q_1\rangle_{\natural*}\qquad\text{for all }\tilde Q_1,\tilde Q_2\in\mathbb{B}.
$$

The **Krein isometry group** is $U_{J}(\mathbb{B})=\{T:T^{\dagger}T=\mathrm{id}\}$.

**Theorem (the group is $\mathrm{U}(1,3)$).** In the coefficient basis the Krein isometry group is

$$
\boxed{\;U_{J}(\mathbb{B})=\{T:T^{*}ET=E\}\cong\mathrm{U}(1,3)\;}
$$

the group of complex matrices preserving an indefinite Hermitian form of signature $(1,3)$. It has real dimension $16$, it is non-compact, its centre is the circle $\mathrm{U}(1)$ of scalar matrices $c\cdot\mathrm{id}$ with $\lvert c\rvert=1$, and its maximal compact subgroup is $\mathrm{U}(1)\times \mathrm{U}(3)$, the group preserving the canonical fundamental decomposition $\mathbb{B}=\mathbb{C}_{\mathbb{B}}\perp_{K}\mathbb{V}_{\mathbb{B}}$.

*Proof.* The condition $T^{*}ET=E$ is the defining equation of the isometry group of the form with matrix $E=\operatorname{diag}(1,-1,-1,-1)$, of signature $(1,3)$ over $\mathbb{C}$, so the group is $\mathrm{U}(1,3)$; its real dimension is $n^{2}+m^{2}+2pq=(n+m)^{2}=16$ for $n=1,m=3$. A group of this form is non-compact because it contains the boosts of §*The Spectrum and the Boosts*. A matrix commutes with every $\mathrm{U}(1,3)$ exactly when it is scalar, and the scalars that preserve the form are those of modulus $1$, giving the centre. The matrices preserving the two eigenspaces of the form, that is the decomposition $\mathbb{C}^{1}\oplus\mathbb{C}^{3}$, are block diagonal unitary in the two blocks, hence $\mathrm{U}(1)\times \mathrm{U}(3)$; that it is maximal compact is the Cartan theorem of §*The Cartan Involution and the Symmetric Space*.

**Theorem (the $J$-unitarity criterion).** A $\mathbb{C}$-linear operator is a Krein isometry if and only if $T^{*}JT=J$, equivalently $T^{\dagger}T=\mathrm{id}$, equivalently $T$ is invertible with $T^{-1}=T^{\dagger}$.

*Proof.* $\langle T\tilde Q_2,T\tilde Q_1\rangle_{\natural*}=\langle T\tilde Q_2,JT\tilde Q_1\rangle_{*}=\langle T^{*}JT\tilde Q_2,\tilde Q_1\rangle_{*}$ while $\langle\tilde Q_2,\tilde Q_1\rangle_{\natural*}=\langle J\tilde Q_2,\tilde Q_1\rangle_{*}$, so the preservation of the form is $T^{*}JT=J$; multiplying by $J$ on the right gives $T^{\dagger}T=\mathrm{id}$. In finite dimension an isometry is injective, hence invertible, and $T^{\dagger}=T^{-1}$.

**Remark (the monoid is the group).** In finite dimension the isometry monoid and the unitary group coincide, so the general warning of *Unitary and Isometric Operators of the Form* — that an isometry need not be unitary — has no effect here; the defect operators of that theory vanish identically.

## The Algebraic Krein Isometries

**Theorem (the isometries among the three families).** For a biquaternion $\tilde{Q}_1$,

$$
\boxed{\;
L_{\tilde{Q}_1}\ \text{is }J\text{-unitary}\iff\tilde{Q}_1\in S^{1}e_t,
\qquad
R_{\tilde{Q}_1}\ \text{is }J\text{-unitary}\iff\tilde{Q}_1\in S^{1}e_t,
\qquad
\Theta_{\tilde{Q}_1}\ \text{is }J\text{-unitary}\iff\lvert\langle\tilde{Q}_1,\tilde{Q}_1\rangle_{\natural}\rvert=1\;},
$$

where $S^{1}e_t$ is the circle of central phases.

*Proof.* $L_{\tilde{Q}_1}^{\dagger}L_{\tilde{Q}_1}=R_{\bar{\tilde{Q}_1}}L_{\tilde{Q}_1}$ is the operator $\tilde Q_2\mapsto\tilde{Q}_1\tilde Q_2\bar{\tilde{Q}_1}$, which is the identity exactly when $\tilde{Q}_1\bar{\tilde{Q}_1}=e_t$ and $\tilde{Q}_1$ is central, that is $\tilde{Q}_1\in S^{1}e_t$; the right case is symmetric. For the sandwich, write $\tilde{Q}_1=\lambda\tilde{U}$ with $\lambda^{2}=\langle\tilde{Q}_1\rangle_{\natural}$ and $\tilde{U}\in SL_2(\mathbb{C})$ when the norm is nonzero. Then $\Theta_{\tilde{Q}_1}=\lvert\lambda\rvert^{2}\Theta_{\tilde{U}}$: the sandwich depends on $\tilde{Q}_1$ only through $\tilde{U}$ and $\lvert\det\tilde{Q}_1\rvert$. A parameter $\tilde U\in SL_2(\mathbb{C})$ preserves the form, because in the matrix model $\operatorname{adj}(\Theta_{\tilde U}(X))=\operatorname{adj}(U)^{-1}\operatorname{adj}(X)\operatorname{adj}(U)$ and $(\Theta_{\tilde U}(Y))^{*}=UY^{*}U^{*}$, so the trace of $\operatorname{adj}(X)Y^{*}$ is unchanged by cyclicity; the scalar factor of $\Theta_{\tilde{Q}_1}$ is $\lvert\det\tilde{Q}_1\rvert^{2}$. Hence $\Theta_{\tilde{Q}_1}$ is an isometry exactly when $\lvert\langle\tilde{Q}_1,\tilde{Q}_1\rangle_{\natural}\rvert=1$.

**Corollary (the compact algebraic subgroup).** The central phases and the unitary sandwiches generate the compact subgroup

$$
\boxed{\;\mathrm{U}(1)\times PU(2)\cong \mathrm{U}(1)\times SO(3)\;}
$$

of real dimension $4$: the phases are the scalar isometries, and the unitary sandwiches are the inner automorphisms $\tilde{Q}_2\mapsto\tilde{Q}_1\tilde{Q}_2\tilde{Q}_1^{\dagger}$ of the algebra, which depend only on the class of $\tilde{Q}_1$ in $\mathrm{U}(2)/\mathrm{U}(1)=PU(2)\cong SO(3)$. The two families commute, and their only common element is the identity. This subgroup is far from the whole group, whose dimension is $16$.

*Proof.* On the unitary group the kernel of the map $\tilde{Q}_1\mapsto\Theta_{\tilde{Q}_1}$ is the central circle $\mathrm{U}(1)$, so its image is $\mathrm{U}(2)$ modulo its centre, which is $PU(2)\cong SO(3)$. The phases are central in the operator algebra, hence commute with the sandwiches; and $\Theta_{\tilde{Q}_1}$ is scalar only for $\tilde{Q}_1$ a scalar of modulus one, in which case $\Theta_{\tilde{Q}_1}=\mathrm{id}$.

**Remark (the norm-one slice is not a family of automorphisms).** For $\lvert\langle\tilde{Q}_1,\tilde{Q}_1\rangle_{\natural}\rvert=1$ the map $\Theta_{\tilde{Q}_1}(X)=\tilde{Q}_1X\tilde{Q}_1^{*}$ is multiplicative only when $\tilde{Q}_1^{*}\tilde{Q}_1$ is central, and inside $SL_2(\mathbb{C})$ that forces $\tilde{Q}_1$ unitary. So the non-unitary members of the norm-one slice are Krein isometries that are **not** automorphisms of the algebra, and the slice is not an enlargement of the inner automorphism group. The maps of the slice form the group $PSL_2(\mathbb{C})\cong SO^{+}(1,3)$, of real dimension $6$ and non-compact, the proper orthochronous Lorentz group of the Lorentzian slice acting on the algebra.

## The Spectrum and the Boosts

**Remark (the spectrum).** The spectrum of a Krein isometry is invariant under $\lambda\mapsto1/\bar\lambda$ with multiplicities and is not in general confined to the unit circle: $T^{*}=JT^{-1}J$ makes $T^{*}$ similar to $T^{-1}$ (*J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra*, §*The Indefinite Spectral Data*). The diagonal phases $L_{ce_t}$ with $c\in S^{1}$ have the single eigenvalue $c$ of multiplicity four; the unitary sandwiches have the eigenvalues $\lambda_i\bar\lambda_j$ of the conjugating unitary matrix; the boosts below leave the circle.

**Definition.** On the Krein-orthogonal sum $\mathbb{C}e_t\perp_{K}\mathbb{C}\vec e_x$ of a positive and a negative line, the **boost of parameter** $t\in\mathbb{R}$ is the operator

$$
T_{t}e_t=\cosh t\,e_t+\sinh t\,\vec e_x,\qquad
T_{t}\vec e_x=\sinh t\,e_t+\cosh t\,\vec e_x,\qquad
T_{t}=\mathrm{id}\ \text{on}\ \mathbb{C}\vec e_y\perp_{K}\mathbb{C}\vec e_z .
$$

**Theorem (the boosts are Krein isometries).** Each $T_{t}$ is a Krein isometry, the assignment $t\mapsto T_{t}$ is a one-parameter subgroup of $U_{J}(\mathbb{B})$, and

$$
\operatorname{spec}(T_{t})=\{\exp(t),\exp(-t),1,1\},
$$

so the boosts are the elements of the group whose spectrum is real and off the unit circle. The restriction of $T_{t}$ to the Lorentzian slice $\mathbb{H}_{\mathbb{B}}$ is the Lorentz boost of rapidity $t$ along the $\vec e_x$ direction, that is of velocity $\tanh t$; it fixes the two null lines $\mathbb{R}(e_t\pm\vec e_x)$ and translates the hyperboloid sheet of §*The Lorentzian Slices* of *The Krein Level Sets and the Hyperbolic Structure*.

*Proof.* In the plane spanned by $e_t,\vec e_x$ the form has the matrix $\operatorname{diag}(1,-1)$ and the matrix of $T_{t}$ is $\begin{pmatrix}\cosh t&\sinh t\\ \sinh t&\cosh t\end{pmatrix}$, whose columns have squares $\cosh^{2}t-\sinh^{2}t=1$, $-\cosh^{2}t+\sinh^{2}t=-1$ and scalar product $\cosh t\sinh t-\sinh t\cosh t=0$: the form is preserved, and the two remaining basis vectors are fixed in their own definite lines, so $T_{t}$ is an isometry. Additivity $T_{s}T_{t}=T_{s+t}$ is the addition formula for the hyperbolic functions, so the family is a one-parameter subgroup. The eigenvalues of the plane block are $\exp(\pm t)$ and the two fixed directions contribute $1,1$. The null vectors $e_t\pm\vec e_x$ are eigenvectors with eigenvalues $e^{\pm t}$, the spacelike directions $\vec e_y,\vec e_z$ are fixed pointwise, and there is no real timelike eigenvector.

**Corollary (the group is non-compact).** The boost family is unbounded in the operator norm as $t\to\infty$, so $U_{J}(\mathbb{B})$ is non-compact; the maximal compact subgroup $\mathrm{U}(1)\times \mathrm{U}(3)$ is exactly the part that fixes the canonical fundamental decomposition.

## The Actions of the Group

**Theorem (transitivity).** The group $U_{J}(\mathbb{B})$ acts transitively on the isotropic lines, on the positive definite lines and on the maximal totally isotropic complex subspaces, which in signature $(1,3)$ are the isotropic lines; over $\mathbb{R}$ the maximal totally isotropic subspaces are the planes of *The K-Degenerate Sector*, §*The Witt Index*. The stabiliser of the positive line $\mathbb{C}e_t$ is $\mathrm{U}(1)\times \mathrm{U}(3)$; the stabiliser of the isotropic line $\mathbb{C}(e_t+\vec e_x)$ is a parabolic subgroup, and it contains the boosts.

*Proof.* Transitivity on the isotropic lines is Witt's extension theorem (*Witt's Theorems*), and in signature $(1,3)$ a maximal complex totally isotropic subspace is a line. Transitivity on the positive lines is read from the identification with the symmetric space $\mathrm{U}(1,3)/(\mathrm{U}(1)\times \mathrm{U}(3))$ of §*The Cartan Involution and the Symmetric Space*. An isometry mapping the positive line $\mathbb{C}e_t$ onto itself preserves its Krein-orthogonal complement, hence the fundamental decomposition, so it lies in $\mathrm{U}(1)\times \mathrm{U}(3)$. The boost fixes the isotropic direction $e_t+\vec e_x$, so the stabiliser of that line contains the boosts and is not compact.

## The Three Adjoints of the Operator Algebra

**Theorem (the three involutions).** On $\mathfrak{g}$ the three pairings of *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra* define three adjoints,

$$
\langle M\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural}=\langle\tilde{Q}_1,M^{\mathsf T}\tilde{Q}_2\rangle_{\natural},
\qquad
\langle M\tilde{Q}_1,\tilde{Q}_2\rangle_{*}=\langle\tilde{Q}_1,M^{*}\tilde{Q}_2\rangle_{*},
\qquad
\langle M\tilde{Q}_1,\tilde{Q}_2\rangle_{\natural*}=\langle\tilde{Q}_1,M^{\dagger}\tilde{Q}_2\rangle_{\natural*},
$$

namely the **transpose** $M^{\mathsf T}$ for the general quaternionic bilinear form, the **Hermitian adjoint** $M^{*}$ for the general plain sesquilinear form, and the **Krein adjoint** $M^{\dagger}=JM^{*}J$ for the general quaternionic sesquilinear form; in the coefficient basis these are the transpose, the conjugate transpose and the conjugate transpose conjugated by $E$. Each gives an involution of $\mathfrak{g}$,

$$
\theta_{\mathsf T}(M)=-M^{\mathsf T},\qquad
\theta_{*}(M)=-M^{*},\qquad
\theta_{J}(M)=-M^{\dagger}=-JM^{*}J .
$$

*Proof.* The three adjoints exist because the three forms are non-degenerate with invertible Gram matrices $\mathrm{I}_4,\mathrm{I}_4,E$, and the formulas in the basis are the standard ones for a bilinear, a sesquilinear and an $E$-sesquilinear form. The maps are $\mathbb{R}$-linear involutions of $\mathfrak{g}$. The plain bilinear form is not one of the three: its Gram matrix is $E$, and its adjoint is $EM^{\mathsf T}E$, which is conjugate to $M^{\mathsf T}$ and carries the same classical algebra.

**Theorem (the three fixed algebras).** The fixed algebras of the three involutions are the classical Lie algebras

$$
\boxed{\;\mathfrak{g}^{\theta_{\mathsf T}}=\{M:M^{\mathsf T}=-M\}=\mathfrak{so}_4(\mathbb{C}),
\qquad
\mathfrak{g}^{\theta_{*}}=\{M:M^{*}=-M\}=\mathfrak{u}(4),
\qquad
\mathfrak{g}^{\theta_{J}}=\{M:M^{\dagger}=-M\}=\mathfrak{u}(1,3)\;}
$$

of real dimensions $12$, $16$ and $16$; each is closed under the commutator bracket, and the three are the Lie algebras of the isometry groups $O_4(\mathbb{C})$, $\mathrm{U}(4)$ and $\mathrm{U}(1,3)$ of the three pairings.

*Proof.* The fixed conditions are the defining equations $\mathfrak{so}_n$, $\mathfrak{u}(n)$ and $\mathfrak{u}(n,m)$; closure under the bracket is the standard fact for the fixed space of an involution that is an automorphism of the bracket. Each of the three maps is an anti-automorphism of the associative product composed with the sign, $(MN)^{\mathsf T}=N^{\mathsf T}M^{\mathsf T}$, $(MN)^{*}=N^{*}M^{*}$ and $(MN)^{\dagger}=N^{\dagger}M^{\dagger}$; the reversal cancels between the two terms of the commutator, so $\theta([M,N])=[\theta M,\theta N]$ for each of the three.

## The Krein Decomposition

**Definition.** The **Krein decomposition** of $\mathfrak{g}$ is the eigenspace decomposition of the involution $\theta_{J}$,

$$
\mathfrak{g}=\mathfrak{k}\oplus\mathfrak{p},
\qquad
\mathfrak{k}=\{M:M^{\dagger}=-M\}=\mathfrak{u}(1,3),
\qquad
\mathfrak{p}=\{M:M^{\dagger}=M\}=J\cdot\operatorname{Herm}_4 .
$$

**Theorem (the decomposition and the bracket pattern).** The decomposition is direct, $\dim_{\mathbb{R}}\mathfrak{k}=\dim_{\mathbb{R}}\mathfrak{p}=16$, the relations

$$
\boxed{\;[\mathfrak{k},\mathfrak{k}]\subseteq\mathfrak{k},
\qquad
[\mathfrak{k},\mathfrak{p}]\subseteq\mathfrak{p},
\qquad
[\mathfrak{p},\mathfrak{p}]\subseteq\mathfrak{k},
\qquad
\{\mathfrak{p},\mathfrak{p}\}\subseteq\mathfrak{p}\;}
$$

hold, with $[\cdot,\cdot]$ the commutator and $\{\cdot,\cdot\}$ the anticommutator, so $\mathfrak{k}$ is a Lie subalgebra, $\mathfrak{p}$ is a Jordan subalgebra, and the pair $(\mathfrak{k},\mathfrak{p})$ is a Lie–Jordan pair attached to the general quaternionic sesquilinear form.

*Proof.* $\mathfrak{k}$ and $\mathfrak{p}$ are the $\mp1$-eigenspaces of an involution, so they are direct and of equal dimension $32/2=16$. Write $M^{\epsilon}$ for an element with $M^{\dagger}=\epsilon M$, $\epsilon=\pm1$, and use $(AB)^{\dagger}=B^{\dagger}A^{\dagger}$. For $M,N\in\mathfrak{k}$ one has $(MN)^{\dagger}=(-N)(-M)=NM$, so $[M,N]^{\dagger}=NM-MN=-[M,N]$ and $[M,N]\in\mathfrak{k}$. For $M\in\mathfrak{k}$ and $N\in\mathfrak{p}$ one has $(MN)^{\dagger}=N^{\dagger}M^{\dagger}=N(-M)=-NM$ and $(NM)^{\dagger}=M^{\dagger}N^{\dagger}=(-M)N=-MN$, so $[M,N]^{\dagger}=(MN)^{\dagger}-(NM)^{\dagger}=MN-NM=[M,N]$ and $[M,N]\in\mathfrak{p}$. For $M,N\in\mathfrak{p}$ one has $(MN)^{\dagger}=NM$, so $[M,N]^{\dagger}=NM-MN=-[M,N]$ and $[M,N]\in\mathfrak{k}$. Finally $\{M,N\}^{\dagger}=NM+MN=\{M,N\}$ for $M,N\in\mathfrak{p}$.

**Remark (the $J$-skew algebra is $J$ times the unitary algebra).** As vector spaces

$$
\mathfrak{u}(1,3)=J\cdot\mathfrak{u}(4)=\{JM:M\in\mathfrak{u}(4)\},
$$

since $(JN)^{\dagger}=-JN$ exactly when $N$ is skew-Hermitian; the identification is not a Lie algebra isomorphism, because $J$ is not central.

## The Krein Involution of the Group

**Definition.** On the group $GL(\mathbb{B})\cong GL_4(\mathbb{C})$ of invertible operators define

$$
\theta_{J}(T)=\bigl(T^{\dagger}\bigr)^{-1}.
$$

**Theorem (the fixed group is $\mathrm{U}(1,3)$).** The map $\theta_{J}$ is an involution with fixed group exactly the Krein isometry group $U_{J}(\mathbb{B})\cong \mathrm{U}(1,3)$; its differential at the identity is the involution $\theta_{J}(M)=-M^{\dagger}$ of $\mathfrak{g}$ and its fixed algebra is $\mathfrak{k}=\mathfrak{u}(1,3)$.

*Proof.* $\theta_{J}^{2}(T)=\bigl((T^{\dagger})^{-1}\bigr)^{\dagger}{}^{-1}=(T^{\dagger\dagger})^{-1}{}^{-1}=T$, using $(S^{-1})^{\dagger}=(S^{\dagger})^{-1}$; the fixed condition $\theta_{J}(T)=T$ is $T^{\dagger}T=\mathrm{id}$, the definition of $J$-unitarity, and the group is $\mathrm{U}(1,3)$.

**Theorem (the involution is not Cartan).** The fixed group $U_{J}(\mathbb{B})\cong \mathrm{U}(1,3)$ of $\theta_{J}$ is non-compact, so $\theta_{J}$ is not a Cartan involution of $GL(\mathbb{B})$: the fixed group of a Cartan involution is compact by definition.

*Proof.* $\mathrm{U}(1,3)$ contains the boosts of §*The Spectrum and the Boosts*, which are unbounded.

## The Cartan Involution and the Symmetric Space

**Theorem (the Cartan involution).** The restriction to $U_{J}(\mathbb{B})$ of the definite involution

$$
\theta_{0}(T)=(T^{*})^{-1}
$$

is the inner automorphism $T\mapsto JTJ$ of the Krein isometry group, and it is a Cartan involution of $\mathrm{U}(1,3)$; its fixed group is the maximal compact subgroup $\mathrm{U}(1)\times \mathrm{U}(3)$, and its differential $\theta_{0}(M)=-M^{*}$ splits

$$
\boxed{\;\mathfrak{u}(1,3)=\mathfrak{k}_{0}\oplus\mathfrak{p}_{0},
\qquad
\mathfrak{k}_{0}=\mathfrak{u}(1)\oplus\mathfrak{u}(3),
\qquad
\dim_{\mathbb{R}}\mathfrak{k}_{0}=10,\quad \dim_{\mathbb{R}}\mathfrak{p}_{0}=6\;}.
$$

*Proof.* For $T\in \mathrm{U}(1,3)$, that is $T^{*}ET=E$, one has $T^{*}=ET^{-1}E$, hence $(T^{*})^{-1}=ETE=JTJ$; the map is the inner automorphism by $J$, an involution preserving the group. Its fixed elements are the isometries that are unitary for $\langle\cdot,\cdot\rangle$, i.e. $\mathrm{U}(4)\cap \mathrm{U}(1,3)$, which is the block-diagonal $\mathrm{U}(1)\times \mathrm{U}(3)$. The differential is $-M^{*}$, whose fixed algebra on $\mathfrak{u}(1,3)$ is $\mathfrak{u}(1)\oplus\mathfrak{u}(3)$ of real dimension $1+9=10$, leaving $\mathfrak{p}_{0}$ of dimension $16-10=6$; the fixed group is compact, which is the definition of a Cartan involution.

**Corollary (the symmetric space and the polar decomposition).** The quotient

$$
\mathrm{U}(1,3)\,/\,\bigl(\mathrm{U}(1)\times \mathrm{U}(3)\bigr)
$$

is a Hermitian symmetric space of real dimension $6$ and rank one, the complex hyperbolic space $\mathbb{CH}^{3}$ of *The Krein Level Sets and the Hyperbolic Structure*, realised as the space of positive lines, that is the open unit ball of $\mathbb{C}^{3}$. The group decomposes as

$$
\mathrm{U}(1,3)=\bigl(\mathrm{U}(1)\times \mathrm{U}(3)\bigr)\cdot\exp(\mathfrak{p}_{0}),
$$

the compact part followed by the hyperbolic part, whose exponentials are the boosts and their conjugates.

*Proof.* The quotient of a Lie group by the fixed group of a Cartan involution is a symmetric space of non-compact type, of dimension $\dim\mathfrak{p}_{0}=6$; the identification with the space of positive lines and with the ball is the parametrisation of §*The Positive Region and the Positive Lines* of *The Krein Level Sets and the Hyperbolic Structure*. The decomposition is the polar decomposition of the general theory of *The Unitary Group and the Hermitian Symmetric Space*.

## The Trace Form and the Jordan Algebra

**Theorem (the trace form).** The pairing $(M,N)\mapsto\operatorname{Tr}(MN)$ is a non-degenerate complex bilinear form on $\mathfrak{g}$, symmetric and invariant under conjugation. Restricted to $\mathfrak{u}(1,3)$, its real part $(M,N)\mapsto\operatorname{Re}\operatorname{Tr}(MN)$ has signature $(6,10)$ on the real vector space of dimension $16$, positive on $\mathfrak{p}_{0}$ and negative on $\mathfrak{k}_{0}$.

*Proof.* The trace form is non-degenerate on $M_4(\mathbb{C})$, and $\operatorname{Tr}(MN)=\operatorname{Tr}(NM)$ makes it symmetric and invariant under $M\mapsto QMQ^{-1}$. For $\mathfrak{u}(n,m)$ it has signature $(2pq,p^{2}+q^{2})$, which for $p=1,q=3$ is $(6,10)$; the signs are read on the diagonal blocks $\mathfrak{u}(1)\oplus\mathfrak{u}(3)$, where $M$ is skew-Hermitian and $\operatorname{Tr}(M^{2})\le0$, and on the off-diagonal block $\mathfrak{p}_{0}$, where $\operatorname{Tr}(M^{2})=2\operatorname{Tr}(Z^{*}Z)\ge0$.

**Definition.** An operator $T\in\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ is **$J$-positive** when it is $J$-self-adjoint and $\langle\tilde Q,T\tilde Q\rangle_{\natural*}\ge0$ for every $\tilde Q$. The **$J$-positive cone** is
$$
\mathcal{P}_J=\{T:T^{\dagger}=T,\ \langle\tilde Q,T\tilde Q\rangle_{\natural*}\ge0\ \forall\tilde Q\}.
$$

**Theorem (the cone as the image of the Hilbert cone).** With $J={}^{\natural}$ and $S$ ranging over the operators that are self-adjoint and positive semidefinite for the definite companion $\langle\cdot,\cdot\rangle_{*}$,
$$
\boxed{\;\mathcal{P}_J=J\cdot\{S\ge0\}=\{JS:S\ge0\}\;}.
$$
The cone $\mathcal{P}_J$ is closed and convex, contains $J$, and does not contain the identity.

*Proof.* For any $T$, $\langle\tilde Q,T\tilde Q\rangle_{\natural*}=\langle\tilde Q,JT\tilde Q\rangle_{*}$, so the positivity and the $J$-self-adjointness of $T$ are exactly the self-adjointness and positivity of $JT$ for the definite form. Hence $T\in\mathcal{P}_J$ exactly when $JT=S\ge0$, that is $T=JS$; the map $S\mapsto JS$ is linear and bijective and carries the closed convex cone $\{S\ge0\}$ onto $\mathcal{P}_J$. The identity $T=J$ gives $JT=\mathrm{id}\ge0$, so $J\in\mathcal{P}_J$; $T=\mathrm{id}$ gives $JT=J$, which has the negative eigenvalue $-1$, so $\mathrm{id}\notin\mathcal{P}_J$.

**Theorem (the Jordan algebra).** The $J$-self-adjoint part $\mathfrak{p}=J\cdot\operatorname{Herm}_4$ is a Jordan algebra under the anticommutator, and it contains the $J$-positive cone $\mathcal{P}_{J}=J\cdot\{S\ge0\}$ defined above.

*Proof.* The anticommutator of two $J$-self-adjoint operators is $J$-self-adjoint, as shown above, and the Jordan identity follows from associativity of the product in $\mathfrak{g}$. Every element of $\mathcal{P}_{J}$ is $J$-self-adjoint by definition, hence lies in $\mathfrak{p}$.

**Remark (the cone is not the cone of squares).** The cone of squares of the Jordan algebra $\mathfrak{p}$ is larger than $\mathcal{P}_{J}$: the identity is a square, $\mathrm{id}=\mathrm{id}^{2}$ with $\mathrm{id}\in\mathfrak{p}$, while $\mathrm{id}\notin\mathcal{P}_{J}$, since $\langle\tilde Q,\mathrm{id}\,\tilde Q\rangle_{\natural*}=\langle\tilde Q,\tilde Q\rangle_{\natural*}$ is indefinite. The $J$-positive cone is the image of the ordinary Hilbert cone under $J$, not the set of squares of the indefinite Jordan structure.

## The J-Contractions

**Definition.** A $\mathbb{C}$-linear operator is a **$J$-contraction** when $\mathrm{id}-T^{\dagger}T$ is in the $J$-positive cone $\mathcal{P}_{J}$; its **defect operator** is $\mathrm{id}-T^{\dagger}T$, and it is **strict** when the defect is invertible.

**Theorem (the model $J$-contraction and the invariance).** The Krein-orthogonal projection $\pi_y=\tfrac12(\mathrm{id}-J)$ onto the vector subspace is a $J$-contraction whose defect is the projection $\pi_x=\tfrac12(\mathrm{id}+J)$ onto the centre, a $J$-positive operator; and the set of $J$-contractions is invariant under $T\mapsto U^{\dagger}TU$ for $U$ a Krein isometry. The scalar multiplications are not $J$-contractions unless they are isometries.

*Proof.* $\langle\pi_y\tilde{Q}_1,\pi_y\tilde{Q}_1\rangle_{\natural*}=-\lVert v\rVert_E^{2}$ while $\langle\tilde{Q}_1,\tilde{Q}_1\rangle_{\natural*}=\lVert c\rVert_E^{2}-\lVert v\rVert_E^{2}$, so the defect form is $\lVert c\rVert_E^{2}\ge0$ and $\pi_y$ is a contraction; $\pi_y^{\dagger}=\pi_y$ and $\pi_y^{2}=\pi_y$, so the defect is $\mathrm{id}-\pi_y=\pi_x$, which is $J$-positive because $\pi_x=J\pi_x$ with $\pi_x\ge0$ for $\langle\cdot,\cdot\rangle_{*}$. For the invariance, if $U$ is a Krein isometry then $(U^{\dagger}TU)^{\dagger}(U^{\dagger}TU)=U^{\dagger}T^{\dagger}TU$, and $U^{\dagger}$ conjugates $\mathcal{P}_{J}$ to itself because $(U^{\dagger}PU)^{\dagger}=U^{\dagger}P^{\dagger}U$ and $\langle\tilde{Q}_1,U^{\dagger}PU\tilde{Q}_1\rangle_{\natural*}=\langle U\tilde{Q}_1,PU\tilde{Q}_1\rangle_{\natural*}$. For a real scalar $\tilde{Q}_1=re_t$ the defect is $(1-r^{2})\mathrm{id}$ and $J(1-r^{2})\mathrm{id}=(1-r^{2})J$ is positive semidefinite only for $r^{2}=1$, so the scalar multiplications are contractions only in the isometry case.

## Worked Examples

**The identity.** $\mathrm{id}=L_{e_t}$ is a $J$-unitary operator, in $\mathrm{U}(1)\times \mathrm{U}(3)$.

**$J$ itself.** $J={}^{\natural}$ is a Krein isometry, of spectrum $\{+1,-1\}$; it is the fundamental symmetry of the canonical decomposition.

**A phase and a sandwich.** $L_{ce_t}$ with $\lvert c\rvert=1$ is a Krein isometry with the single eigenvalue $c$; $\Theta_{\vec e_x}$ has $\lvert\langle \vec e_x,\vec e_x\rangle_{\natural}\rvert=1$, is a Krein isometry and an inner automorphism, of spectrum $\{+1,-1\}$.

**A boost.** $T_{t}$ with $t=1$ is a Krein isometry of spectrum $\{e,e^{-1},1,1\}$, off the unit circle, realising the Lorentz boost of the Lorentzian slice.

**A contraction.** $\pi_y=\tfrac12(\mathrm{id}-J)$, the projection onto the vector subspace, is a $J$-contraction with defect $\pi_x$, the projection onto the centre.

**A non-isometry that is not a contraction.** $L_{2e_t}$ has $\mathrm{id}-L^{\dagger}L=-3\,\mathrm{id}$, whose image under $J$ is $-3J$, not in the definite positive cone, so $L_{2e_t}$ is neither a contraction nor an isometry.

**The three involutions of the identity.** For $M=\mathrm{id}$ one has $M^{\mathsf T}=M^{*}=M^{\dagger}=\mathrm{id}$ and $\theta(\mathrm{id})=-\mathrm{id}$ for each of the three involutions of §*The Three Adjoints of the Operator Algebra*.

**A $J$-skew element.** $M=JL$ with $L$ definite-skew has $M^{\dagger}=-M$, so $M\in\mathfrak{k}=\mathfrak{u}(1,3)$.

## Summary

The Krein isometry group $U_{J}(\mathbb{B})=\{T:T^{*}ET=E\}$ is $\mathrm{U}(1,3)$: real dimension $16$, non-compact, centre the scalar phases $\mathrm{U}(1)$, maximal compact subgroup $\mathrm{U}(1)\times \mathrm{U}(3)$. A Krein isometry is characterised by $T^{*}JT=J$, equivalently $T^{-1}=T^{\dagger}$. Inside the algebra's families the Krein isometries are the central phases $L_{\tilde{Q}_1}$, $\tilde{Q}_1\in S^{1}e_t$, and the unitary sandwiches $\Theta_{\tilde{Q}_1}$, $\tilde{Q}_1\in\mathrm{U}(2)$; together they form the compact subgroup $\mathrm{U}(1)\times PU(2)\cong \mathrm{U}(1)\times SO(3)$ of dimension $4$, the sandwiches acting as the inner automorphisms of the algebra. The sandwiches with $\lvert\langle\tilde{Q}_1,\tilde{Q}_1\rangle_{\natural}\rvert=1$ are isometries too, but the non-unitary ones are not automorphisms of the algebra, and the slice forms the non-compact group $PSL_2(\mathbb{C})\cong SO^{+}(1,3)$. The spectrum of a Krein isometry is invariant under $\lambda\mapsto1/\bar\lambda$ and is not confined to the unit circle: the boosts $T_{t}$ have $\exp(\pm t),1,1$ and are the one-parameter subgroups realising the Lorentz boosts. The group acts transitively on the isotropic lines, on the positive lines and on the maximal totally isotropic complex subspaces.

On the operators, the three pairings give the transpose, the Hermitian adjoint and the Krein adjoint $M^{\dagger}=JM^{*}J$, whose involutions $M\mapsto-M^{\sigma}$ have the fixed algebras $\mathfrak{so}_4(\mathbb{C})$, $\mathfrak{u}(4)$ and $\mathfrak{u}(1,3)$, of real dimensions $12$, $16$ and $16$. The Krein involution splits $\mathfrak{g}=\mathfrak{k}\oplus\mathfrak{p}$ into the $J$-skew operators $\mathfrak{k}=\mathfrak{u}(1,3)$ and the $J$-self-adjoint operators $\mathfrak{p}=J\cdot\operatorname{Herm}_4$, each of dimension $16$; $\mathfrak{k}$ is a Lie algebra, $\mathfrak{p}$ a Jordan algebra, and the bracket of $\mathfrak{k}$ with $\mathfrak{p}$ stays in $\mathfrak{p}$. On the group the involution $T\mapsto(T^{\dagger})^{-1}$ has fixed group the non-compact $\mathrm{U}(1,3)$, so it is not a Cartan involution; the Cartan involution is the restriction of $T\mapsto(T^{*})^{-1}$, whose fixed group is the maximal compact $\mathrm{U}(1)\times \mathrm{U}(3)$, with $\dim\mathfrak{k}_{0}=10$ and $\dim\mathfrak{p}_{0}=6$, and whose symmetric space is the complex hyperbolic space $\mathbb{CH}^{3}$ of real dimension $6$. The trace form of $\mathfrak{u}(1,3)$ has signature $(6,10)$, positive on the hyperbolic part and negative on the compact part; the $J$-positive cone sits inside the Jordan algebra $\mathfrak{p}$ but is not its cone of squares. Finally the $J$-contractions, defined by the $J$-positivity of their defect, are invariant under conjugation by the group; their model is the projection onto the vector subspace, whose defect is the projection onto the centre, while a scalar multiplication is a contraction only when it is an isometry.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $U_{J}(\mathbb{B})=\{T:T^{*}ET=E\}$ | The Krein isometry group, $\cong \mathrm{U}(1,3)$ |
| $\dim_{\mathbb{R}}U_{J}(\mathbb{B})=16$ | The real dimension; the group is non-compact |
| $\mathrm{U}(1)$ | Its centre, the scalar phases |
| $\mathrm{U}(1)\times \mathrm{U}(3)$ | Its maximal compact subgroup; fixed group of $\theta_{0}$ |
| $\mathrm{U}(1)\times PU(2)\cong \mathrm{U}(1)\times SO(3)$ | The Krein isometries among the algebra's families |
| $PSL_2(\mathbb{C})\cong SO^{+}(1,3)$ | The norm-one sandwiches; non-compact, dimension $6$ |
| $\lambda\leftrightarrow1/\bar\lambda$ | The symmetry of the spectrum of a Krein isometry |
| $T_{t}$, $\operatorname{spec}=\{\exp(t),\exp(-t),1,1\}$ | The boosts; non-compactness; the Lorentz boosts |
| $\mathfrak{g}=\operatorname{End}_{\mathbb{C}}(\mathbb{B})\cong\mathfrak{gl}_4(\mathbb{C})$ | The operator algebra; real dimension $32$ |
| $M^{\mathsf T}$, $M^{*}$, $M^{\dagger}=JM^{*}J$ | The three adjoints |
| $\theta_{\mathsf T},\theta_{*},\theta_{J}$ | The three involutions $M\mapsto-M^{\sigma}$ |
| $\mathfrak{so}_4(\mathbb{C})$, $\mathfrak{u}(4)$, $\mathfrak{u}(1,3)$ | The three fixed algebras; dimensions $12$, $16$, $16$ |
| $\mathfrak{g}=\mathfrak{k}\oplus\mathfrak{p}$ | The Krein decomposition |
| $\mathfrak{k}=\mathfrak{u}(1,3)$, $\mathfrak{p}=J\cdot\operatorname{Herm}_4$ | The $J$-skew and $J$-self-adjoint parts |
| $\theta_{J}(T)=(T^{\dagger})^{-1}$ | The group involution; fixed group $\mathrm{U}(1,3)$, non-compact |
| $\theta_{0}(T)=(T^{*})^{-1}$, $\mathrm{U}(1)\times \mathrm{U}(3)$ | The Cartan involution and its fixed group |
| $\mathrm{U}(1,3)/(\mathrm{U}(1)\times \mathrm{U}(3))\cong\mathbb{CH}^{3}$ | The symmetric space of real dimension $6$ |
| $(6,10)$ | The signature of the trace form of $\mathfrak{u}(1,3)$ |
| $\mathrm{id}-T^{\dagger}T\in\mathcal{P}_{J}$ | $J$-contraction and defect |

## Further Reading

- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the three pairings, their isometry groups and their signatures
- [J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra](j-self-adjoint-and-j-unitary-operators-on-the-general-quaternionic-sesqualgebra.html), for the adjoints of the algebra's families and the indefinite spectral data
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the form and its Gram matrix.
- [K-Regularity and Degeneracy in the Biquaternion Algebra](krein-norm-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the null set and the positive cone.
- [The Krein Level Sets and the Hyperbolic Structure](the-krein-level-sets-and-the-hyperbolic-structure.html), for the level sets and the complex hyperbolic space as the space of positive lines
- [The Indefinite Hermitian Sandwich on the General Quaternionic Sesqualgebra](the-indefinite-hermitian-sandwich-on-the-general-quaternionic-sesqualgebra.html), for the sandwich by a $J$-unitary parameter
- [Unitary and Isometric Operators of the Form](unitary-and-isometric-operators-of-the-form.html), for the general isometry monoid and its group of units
- [The Unitary Group and the Hermitian Symmetric Space](the-unitary-group-and-the-hermitian-symmetric-space.html), for the general $\mathrm{U}(n,m)$, its Cartan involution and the bounded realisation
- [Biquaternion Rotations and Lorentz Transformations](biquaternion-rotations-and-lorentz-transformations.html), for the Lorentz transformations realised by the boosts
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (Academic Press, 1978), for Cartan involutions, Cartan decompositions and symmetric spaces of non-compact type
- Israel Gohberg, Peter Lancaster and Leiba Rodman, *Indefinite Linear Algebra and Applications* (Birkhäuser, 2005), for the unitary group of an indefinite form, its maximal compact part and the contractions
