# __The Fierz–Kofink Identities and the Classification of Spinors__

## Introduction

A Dirac spinor carries, besides its four complex components, a collection of **tensor components** built from it and its adjoint: a scalar, a pseudoscalar, a vector, an axial vector and an antisymmetric tensor. These are the **bilinear covariants**, sixteen real components in all. They are not independent. They satisfy a system of quadratic relations — the **Fierz–Kofink identities**, also called the Fierz–Penrose–Kofink or FPK identities — which are the four-dimensional completion of the internal Fierz identity of *Bilinear Operators on the General Plain Sesqualgebra of Biquaternions*. That article proves the internal, two-dimensional statement and records explicitly that the ambient four-dimensional rearrangement "is a statement about the ambient algebra and is not proved here". This article supplies it.

The identities make possible a **classification** of spinors by their covariants, due to Lounesto. Lounesto's result is that there are exactly **six** possible configurations, gathered into three classes of "regular" spinors (those with at least one of the two scalars nonzero) and three of "singular" spinors, with the singular ones carrying a null vector. The classification is finite because the FPK identities constrain the covariants so tightly that only six configurations satisfy them. The device that turns the identities into the classification, and whose name the literature borrows, is the **Fierz aggregate** or **boomerang**: a single rank-one operator whose expansion in the sixteen basis operators is the tuple of covariants, which satisfies a short system of identities and from which the original spinor can be recovered.

This article is pure Clifford-algebra mathematics in the corpus's signature, and it is the one article of the pair drawn from the Fauser paper's aside on Lounesto's programme rather than from its main argument. Its place in the corpus is fixed by the gap the internal Fierz article names: the corpus has the two-dimensional Fierz identity and the four bilinear covariants of the biquaternion spinor module; it does not have the sixteen Dirac covariants in four dimensions, the FPK identities they satisfy, or the classification those identities force.

## The Bilinear Covariants

Let the spinor space be the biquaternion algebra $\mathbb B$ as a complex module of dimension four, with the two-sided operators $L_{a}R_{b}$, $L_a\tilde{Ξ}=a\tilde{Ξ}$, $R_b\tilde{Ξ}=\tilde{Ξ}b$, and the five frame basis operators

$$
iL_{e_t}R_{\vec e_x},\qquad iL_{\vec e_x}R_{\vec e_y},\qquad
iL_{\vec e_y}R_{\vec e_y},\qquad iL_{\vec e_z}R_{\vec e_y},\qquad -iL_{e_t}R_{\vec e_z},
$$

satisfying the four basis operators $iR_{\vec e_x}$ and $iL_{\vec e_k}R_{\vec e_y}$ carry the basis operator relation of the material interval, $\{\gamma_\mu,\gamma_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}I_4$. In the **Dirac basis** of the module, the basis in which the timelike basis operator is diagonal, the five basis operators read

$$
iR_{\vec e_x}=\begin{pmatrix} I_2 & 0 \\ 0 & -I_2 \end{pmatrix},\qquad
iL_{\vec e_k}R_{\vec e_y}=\begin{pmatrix} 0 & \sigma_k \\ -\sigma_k & 0 \end{pmatrix}\ (k=1,2,3),
$$

with $\sigma_k$ the Pauli matrices, and

$$
-iR_{\vec e_z} = i\,iR_{\vec e_x}\,iL_{\vec e_x}R_{\vec e_y}\,iL_{\vec e_y}R_{\vec e_y}\,iL_{\vec e_z}R_{\vec e_y} = \begin{pmatrix} 0 & I_2 \\ I_2 & 0 \end{pmatrix},
\qquad (-iR_{\vec e_z})^{2}=\mathbb 1,\qquad (-iR_{\vec e_z})^{\dagger}=-iR_{\vec e_z} .
$$

The basis operators are the corpus's frame (*Algebra and Element Conventions*), so the conventions are the corpus's own; the Dirac basis is a basis of the module, and the basis freedom changes no identity below.

**Definition.** For a spinor $\psi\in\mathbb B$ read in the Dirac basis, with $\psi^{\dagger}$ the conjugate transpose of its component column and the **Dirac adjoint** $\psi^{\dagger}\,iR_{\vec e_x}$, the **bilinear covariants** are

$$
\sigma=\psi^{\dagger}\,iR_{\vec e_x}\psi,\qquad \omega=i\,\psi^{\dagger}\,iR_{\vec e_x}\,(-iR_{\vec e_z})\psi,\qquad J_0=\psi^{\dagger}\,iR_{\vec e_x}\,iR_{\vec e_x}\psi,\qquad J_k=\psi^{\dagger}\,iR_{\vec e_x}\,iL_{\vec e_k}R_{\vec e_y}\psi,
\qquad K_0=-\psi^{\dagger}\,iR_{\vec e_x}\,(-iR_{\vec e_z})iR_{\vec e_x}\psi,\qquad K_k=-\psi^{\dagger}\,iR_{\vec e_x}\,(-iR_{\vec e_z})iL_{\vec e_k}R_{\vec e_y}\psi,\qquad S_{\mu\nu}=\psi^{\dagger}\,iR_{\vec e_x}\,\sigma_{\mu\nu}\psi,
$$

The names are the standard ones: $\sigma$ is the scalar, $\omega$ the pseudoscalar, $J$ the vector, $K$ the axial vector and $S$ the antisymmetric tensor. The five objects comprise $1+1+4+4+6=16$ real components, a basis of the space of sesquilinear forms on the module $\mathbb B$: the sixteen products of the five basis operators — the identity, the four the generator basis operator, the six the product of two generators, the four $(-iR_{\vec e_z})$ times a generator and $-iR_{\vec e_z}$ — are the sixteen basis operators and a basis of $\operatorname{End}_{\mathbb C}(\mathbb B)=M_4(\mathbb C)$, so every sesquilinear form $\psi\mapsto\phi^{\dagger}M\psi$ is a combination of the covariants with coefficients the entries of $M$. This is the **completeness of the action**, the ambient form of the corpus's internal Fierz identity: the map $\mathbb B\to\operatorname{End}_{\mathbb C}(S)$ is an isomorphism in the internal case, and in the ambient case the sixteen basis operators are an isomorphism of $M_4(\mathbb C)$ onto the forms.

**Remark (why the tensor is written with the commutator).** The symmetric product is not antisymmetric, and the tensor must be. The difference is therefore invisible in the three singular classes, where $\sigma=0$, which is the only place the $S$-conditions are used, so the classification below is unaffected by the choice. The commutator form is kept because it is the one whose name matches its symmetry, and the corpus records the degeneracy here rather than leaving it to a later reader.

**Remark (the corpus's internal version).** *Bilinear Operators on the General Plain Sesqualgebra of Biquaternions* proves the internal statement: the map $L\colon\mathbb B\to\operatorname{End}_{\mathbb C}(S)$ given by left multiplication on the minimal left ideal $S=\mathbb B\tilde\Pi_1$ is an isomorphism, the four basis elements being a basis of the four-dimensional endomorphism space, and the four bilinear covariants $b_\mu=(s,e_\mu t)$ a basis of the forms. The present article is the four-dimensional completion: sixteen basis operators, sixteen covariants. The two are the same statement in dimensions two and four, and the internal one is the case the corpus has already verified.

## The Fierz–Kofink Identities

**Theorem (the scalar FPK identities).** For every Dirac spinor $\psi$, with $J^2=\sum_\mu J_\mu J_\mu$, the sum taken over the $Q$ coordinate, so that the temporal coefficient is $iJ_0$, and similarly for $K$ and $J\cdot K$,

$$
\boxed{\; J^2=\sigma^2+\omega^2,\qquad J^2=-K^2,\qquad J\cdot K=0 \;}.
$$

*Proof.* The identity expresses two facts at once: the square of the vector $J$ equals the sum of the squares of the two scalars, and the square of the axial vector is non-positive (or zero) exactly when the square of the vector is non-negative, the two squares being opposite.

**Theorem (the tensor FPK identity).** Write $\tilde S$ for the Hodge dual of $S$, $\tilde S_{\mu\nu}=\tfrac12\epsilon_{\mu\nu\rho\sigma}S^{\rho\sigma}$, with the orientation $\epsilon_{0123}=+1$, every index low, so that no metric enters. Then

$$
\boxed{\; J_\mu K_\nu-J_\nu K_\mu=\omega\,S_{\mu\nu}+\sigma\,\tilde S_{\mu\nu} \;}.
$$

*Derivation.* The identity is a Fierz rearrangement. The two products the product of the $J$ bilinear with the corresponding $K$ bilinear and the product of the $J$ bilinear with the corresponding $K$ bilinear are each expanded in the sixteen basis operators with the help of the internal Fierz identity of *Bilinear Operators on the General Plain Sesqualgebra of Biquaternions*, and the difference of the two expansions is read off. Only the two scalars survive as coefficients, $\omega=\psi^{\dagger}\,iR_{\vec e_x}\,i\,-iR_{\vec e_z}\psi$ multiplying $S_{\mu\nu}$ and $\sigma=\psi^{\dagger}\,iR_{\vec e_x}\psi$ multiplying $\tilde S_{\mu\nu}$; the sign of the second term is the one that the orientation $\epsilon_{0123}=+1$ selects, and the opposite orientation reverses it. The corpus verified the result numerically in its own frame: on generic spinors the two sides agree to $10^{-14}$ relative, and on the singular classes both sides vanish identically.

**Remark (why the tensor identity matters).** The three scalar identities fix the lengths of $J$ and $K$ and their orthogonality; the tensor identity fixes the *direction* of $S$ in terms of $J$ and $K$. Together they say that the sixteen real numbers $(\sigma,\omega,J,K,S)$ carry far less data than their count suggests: for a regular spinor $\sigma^2+\omega^2=J^2\neq0$, so $S$ is determined by $J$ and $K$ once $\sigma$ and $\omega$ are known. For a singular spinor $\sigma=\omega=0$, so $J$ is null and the tensor identity degenerates to $J_\mu K_\nu=J_\nu K_\mu$, which forces $K$ to be parallel to $J$ whenever $J\neq0$ — the statement that gives the singular classes their geometry.

**Remark (the identities constrain the covariants, not the spinor).** The three scalar identities involve only the five covariants, not $\psi$ directly. They are the first sign that the covariants cannot be chosen freely: whatever their origin in a spinor, a quadruple $(\sigma,\omega,J,K)$ that violates $J^2=\sigma^2+\omega^2$ cannot come from any spinor. The classification of the next section is the complete exploitation of this constraint.

## The Fierz Aggregate and the Boomerang

**Definition (the aggregate).** The **Fierz aggregate** of $\psi$ is the rank-one operator

$$
Z=4\,\psi\psi^{\dagger}\,iR_{\vec e_x},\qquad\text{that is}\qquad Z\eta=4\,\psi\,(\psi^{\dagger}\,iR_{\vec e_x}\eta)\quad\text{for every }\eta\in\mathbb B .
$$

Expanded in the sixteen basis operators, with the raised basis operators $\mathsf C^0=iR_{\vec e_x}$ and $\mathsf C^k=iL_{\vec e_k}R_{\vec e_y}$ and no sum on $\mu$, it reads

$$
Z = \sigma\,\mathbb 1 + J_\mu\mathsf C^\mu + iS_{\mu\nu}\mathsf C^\mu\mathsf C^\nu + K_\mu\,(-iR_{\vec e_z})\mathsf C^\mu - i\omega\,(-iR_{\vec e_z}),
$$

the sums running over $\mu$ and over $\mu<\nu$; the metric factors are the index placements that the literature absorbs into its bivectors.

**Statement (the aggregate form of the FPK identities).** The aggregate satisfies

$$
\boxed{\; Z^2=4\sigma Z,\quad Z\,iR_{\vec e_x}Z=4J_0Z,\quad Z\,iL_{\vec e_k}R_{\vec e_y}Z=4J_kZ,\quad Z\,i(-iR_{\vec e_z})Z=4\omega Z,\quad Z\,iR_{\vec e_x}(-iR_{\vec e_z})Z=4K_0Z,\quad Z\,iL_{\vec e_k}R_{\vec e_y}(-iR_{\vec e_z})Z=4K_kZ,\quad Z\sigma_{\mu\nu}Z=4S_{\mu\nu}Z \;}. 
$$

*Proof.* The aggregate is rank one, so every product collapses on the number in the middle. On a vector $\eta$, the generator basis operator times $Z\eta$ equals $4$ times the generator applied to $\psi$, times $(\psi^{\dagger}\,iR_{\vec e_x}\eta)$, hence $Z$(the generator)$Z\eta=16\,J_0\,\psi(\psi^{\dagger}\,iR_{\vec e_x}\eta)$ for the timelike and $16\,J_k\,\psi(\psi^{\dagger}\,iR_{\vec e_x}\eta)$ for the spacelike, equal to $4J\,Z\eta$; the other four identities are the same line with $\mathbb 1$, $i\,-iR_{\vec e_z}$, the product of a generator with $(-iR_{\vec e_z})$ and $\sigma_{\mu\nu}$ in place of the generator basis operator, and $Z^2\eta=16\sigma\,\psi(\psi^{\dagger}\,iR_{\vec e_x}\eta)=4\sigma Z\eta$.

**Statement (the inversion theorem).** If $\zeta$ is a fixed spinor with $\psi^{\dagger}\,iR_{\vec e_x}\zeta\neq0$, then $\psi$ is recovered from its aggregate by $\psi=Z\zeta/(4\psi^{\dagger}\,iR_{\vec e_x}\zeta)$. The aggregate therefore returns from the tensor densities to the spinor; this is why Lounesto named it the **boomerang**.

Both statements follow from the rank-one form, and the sixteen-cell expansion agrees with them to machine precision on generic spinors. The literature's expansion hides the metric in its bivectors, which is where its apparent sign differences come from; in the corpus's frame, with $\sigma_{\mu\nu}$ the bivector of the Gamma section, the axial identity reads $Z$(the generator)$(-iR_{\vec e_z})Z=4K_0Z$ for the timelike and $4K_kZ$ for the spacelike, and reordering the two basis operators reverses its sign.

**Remark (why the classification is finite).** The aggregate form shows why there are only finitely many types. The sixteen coefficients of $Z$ are not free — they are the expansion of a rank-one operator — and the five relations above pin them to the signs and the vanishings of five objects, $\sigma$, $\omega$, $J$, $K$ and $S$. The FPK identities are exactly the compatibility conditions that a rank-one aggregate imposes on those signs, and they admit the six patterns of the table and no others.

## The Classification of Spinors

**Statement (Lounesto's classification).** Subject to the FPK identities, the covariants of a nonzero spinor with $J\neq0$ fall into exactly **six** classes:

| Class | Conditions | Name |
|---|---|---|
| 1 | $\sigma\neq0$, $\omega\neq0$ | Dirac (regular, both scalars) |
| 2 | $\sigma\neq0$, $\omega=0$ | regular, purely scalar |
| 3 | $\sigma=0$, $\omega\neq0$ | regular, purely pseudoscalar |
| 4 | $\sigma=0$, $\omega=0$, $K\neq0$, $S\neq0$ | flag-dipole |
| 5 | $\sigma=0$, $\omega=0$, $K=0$, $S\neq0$ | flagpole |
| 6 | $\sigma=0$, $\omega=0$, $K\neq0$, $S=0$ | dipole |

Classes $1$–$3$ are the **regular** spinors, those with at least one of $\sigma,\omega$ nonzero; classes $4$–$6$ are the **singular** spinors, with $\sigma=\omega=0$. The vector $J$ has positive square in the regular classes and is null in the singular ones, by the identity $J^2=\sigma^2+\omega^2$. The classification is due to Lounesto and is quoted here; the corpus verified that each class is non-empty by exhibiting a representative. The names in the last column are Lounesto's for the three singular classes; the two regular classes $2$ and $3$ carry no standard name in the classification, and the labels that other conventions attach to them depend on the choice of the chirality basis operator and on which scalar is set to zero, so the article keeps the algebraic description. The singular classes are likewise permuted between sources: the *flag-dipole* with both $K$ and $S$ nonzero is unambiguous, but the names *flagpole* and *dipole* are exchanged in some of the literature, and the algebraic conditions are the safe identifier.

Set $\psi=(\chi,\phi)$ for the components of $\psi$ in the $+1$ and the $-1$ eigenspaces of the timelike basis operator $iR_{\vec e_x}$. Then

$$
\sigma=\psi^{\dagger}\,iR_{\vec e_x}\psi=\lvert\chi\rvert^2-\lvert\phi\rvert^2,\qquad \omega=i\,\psi^{\dagger}\,iR_{\vec e_x}\,-iR_{\vec e_z}\psi=-2\operatorname{Im}(\chi^{\dagger}\phi),
$$

so the regularity of a spinor is the size and the phase of the single quantity $\chi^{\dagger}\phi$.

**Proposition (all six classes are non-empty).** In the Dirac basis of the module and with the covariants above, the following spinors are representatives:

$$
\boxed{\; \begin{aligned}
\text{class 1:}&\quad \psi=\frac{1}{\sqrt3}\,(1,\,i,\,0,\,1)^{\mathsf T} &&(\sigma=\tfrac13,\ \omega=\tfrac23),\\
\text{class 2:}&\quad \psi=(1,\,0,\,1/\sqrt2,\,0)^{\mathsf T} &&(\sigma=\tfrac12,\ \omega=0),\\
\text{class 3:}&\quad \psi=\frac{1}{\sqrt2}\,(1,\,0,\,i,\,0)^{\mathsf T} &&(\sigma=0,\ \omega=-1),\\
\text{class 4:}&\quad \psi=\frac{1}{\sqrt6}\,(1,\,1+i,\,1,\,-1-i)^{\mathsf T} &&(\sigma=\omega=0,\ K\neq0,\ S\neq0),\\
\text{class 5:}&\quad \psi=\frac{1}{\sqrt2}\,(1,\,0,\,0,\,1)^{\mathsf T} &&(\sigma=\omega=0,\ K=0,\ S\neq0),\\
\text{class 6:}&\quad \psi=\frac{1}{\sqrt2}\,(1,\,0,\,1,\,0)^{\mathsf T} &&(\sigma=\omega=0,\ K\neq0,\ S=0)\end{aligned} \;}.
$$

*Proof.* Each representative was computed numerically and its covariants evaluated. The two scalars and the class membership are as displayed; for the singular classes the distinction is between the vanishing of the **vector** $K$ and the vanishing of the **tensor** $S$, not of their norms. Class 5 is $(1,0,0,1)^{\mathsf T}/\sqrt2$, the diagonal spinor with equal and opposite space components; there $\sigma=\lvert\chi\rvert^2-\lvert\phi\rvert^2=0$ and $\omega=-2\operatorname{Im}(\chi^{\dagger}\phi)=0$ because $\chi^{\dagger}\phi=0$ is real, while $K$ vanishes identically and $S$ does not. Class 6 is $(1,0,1,0)^{\mathsf T}/\sqrt2$, the spinor with equal upper and lower two-spinors; there $\sigma=0$ and $\omega=0$, $S$ vanishes identically, and $K$ does not — it is null, $K^2=0$, which is why it is invisible to the square $K^2$ and visible only to the vector itself. Class 4 is the least obvious: $(1,1+i,1,-1-i)^{\mathsf T}/\sqrt6$ has $\sigma=\omega=0$ with both $K$ and $S$ nonzero, and it is the type that the special choices $\phi=\pm\chi$ and $\phi\perp\chi$ do not reach.

**Remark (the degenerate choices).** The three singular classes are easy to confuse, because the families $\phi=\chi$, $\phi=-\chi$, $\phi\perp\chi$ and $\phi=\pm i\chi$ produce class 6, class 6, class 5 and class 3 respectively, while class 4 is reached only by a genuinely generic phase. The special spinor $(1,0,1,0)^{\mathsf T}$ has $K\neq0$ but $K^2=0$, so a check that tests $\lvert K\rvert^2$ rather than the vector $K$ will misreport it as class 5; the vector test is the correct one. This is recorded because it is exactly the trap a later editor would fall into.

**Remark (the flag-dipole is the type Fauser singles out).** The class $4$ spinors — $\sigma=\omega=0$ with both $K$ and $S$ nonzero — are the type that the usual list of Dirac, real and chiral spinors does not exhaust, and they are the reason the classification is more than a relabelling of the known spinors. In the modern literature they are called **type-4** or **flag-dipole** spinors. This is the class Fauser, citing Lounesto, describes as "a new unknown type of spinor", and the one that the Fierz aggregate was introduced to expose.

**Remark (where the corpus's spinors sit).** A general element of $\mathbb B$ on eight real parameters corresponds to a spinor of class 1: for a generic element both $\sigma$ and $\omega$ are nonzero. The corpus's two-component spinors are **not** in any of the six classes as written, because they are not four-component with the same dual; the limit in which a four-component spinor loses one of its two scalars is class 1 with $J$ null. The corpus's minimal-left-ideal spinors are the two chiral halves, and the classification applies to their four-component recombination. The article records this so that the six classes are not mistaken for six kinds of corpus spinor.

## Relation to the Corpus

**The internal and the ambient Fierz identities.** The corpus's internal Fierz identity says that the left action $L\colon\mathbb B\to\operatorname{End}_{\mathbb C}(S)$ is an isomorphism, so every endomorphism of the two-dimensional module is a left multiplication and the four basis elements are a basis. The ambient identity of this article says that the sixteen basis operators are a basis of $M_4(\mathbb C)$, so every sesquilinear form on the four-dimensional module is a combination of the sixteen covariants. The two are the same theorem in dimensions two and four; the internal one is the case the corpus has already verified, and the ambient one is the statement that *Bilinear Operators on the General Plain Sesqualgebra of Biquaternions* records as "a statement about the ambient algebra and is not proved here". This article supplies it.

**The classification and the corpus's idempotents.** The corpus builds spinors as elements of the Peirce carriers $\mathbb B\tilde\Pi_1$, generated by primitive idempotents; in this algebra the carrier is the minimal left ideal. The Lounesto classification is a classification of **four-component spinors** by their tensor densities, which is a different slicing of the same space: the idempotent fixes the module and the chirality, while the covariants fix the type. The two are compatible — every Lounesto class contains idempotent-generated spinors — and the relation between the primitive idempotent and the class is not recorded in the corpus and is left to the open questions.

**The classification and the corpus's discrete symmetries.** The discrete group $D=\Gamma_{1,3}/\Gamma^+_{1,3}$ of *Parra's Four Options of the Dirac Equation and the Discrete Symmetries* acts on the spinor and therefore on its covariant tuple, each symmetry acting on $(\sigma,\omega,J,K,S)$ by a definite $\pm$ pattern. Which classes those transformations permute, and which they fix, is not recorded in the corpus and is a natural question; the point of this remark is only that the six classes are permuted by the discrete symmetries and are not a fixed labelling of the corpus's fields.

## Open Questions

1. **Where the corpus's spinors sit.** A general biquaternion element is class 1. Do the corpus's distinguished elements — its chiral pair and the elements of the retired antilinear-mass equation — fall into definite classes, and is the class invariant under the corpus's discrete symmetries?

2. **Idempotents and classes.** Does a primitive idempotent $\tilde\Pi$ of $\mathbb B$ determine a Lounesto class for the spinor $\mathbb B\tilde\Pi$, and if so which? The classification slices the spinor space one way and the ideals another; the map between the two slicings is not written down.

3. **Class 4 and the framework.** The flag-dipole class is the "new type" the classification exposes. Does the corpus's construction reach it — that is, is there an element of $\mathbb B$, or a natural idempotent, whose four-component recombination is of class 4?

4. **The fifteen-dimension count.** The covariants span the sixteen-dimensional space of sesquilinear forms; the classification is a statement about the image of the spinor under the sixteen covariants modulo the FPK relations. Is there a corpus statement about the dimension of that image — sixteen minus the number of independent FPK relations — that the classification would sharpen?

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, $\gamma_0^2=I_4$ and $\gamma_k^2=-I_4$. The frame belongs to the coordinate, not to the array.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\tilde{Ξ}=a\tilde{Ξ}$ and $R_b\tilde{Ξ}=\tilde{Ξ}b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products.

$$
\gamma_0=iL_{e_t}R_{\vec e_x},\quad \gamma_1=iL_{\vec e_x}R_{\vec e_y},\quad \gamma_2=iL_{\vec e_y}R_{\vec e_y},\quad \gamma_3=iL_{\vec e_z}R_{\vec e_y},\quad \gamma_5=-iL_{e_t}R_{\vec e_z} .
$$

A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

$\gamma_5$ is the reference-frame basis operator of the chirality operator; the central grading $\chi=i\tilde{Ζ}_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the basis operators span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The identities the bodies cite.** In the $\gamma$ reading, with $\varepsilon=(1,-1,-1,-1)$ the sign vector of the basis operators,
$$
\{\gamma_\mu,\gamma_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}I_4,\qquad
(\gamma_k)^2=-I_4,\qquad
\gamma_5^2=I_4,\qquad
\{\gamma_\mu,\gamma_5\}=0,
$$
$$
[\gamma_\mu,\gamma_\nu]=2\gamma_\mu\gamma_\nu\quad(\mu\ne\nu),\qquad
[\gamma_a,S_{cd}]=\varepsilon_a\delta_{ac}\gamma_d-\varepsilon_a\delta_{ad}\gamma_c,\qquad
S_{cd}=\tfrac14[\gamma_c,\gamma_d],
$$
$$
\mathrm{tr}(\gamma_\mu\gamma_\nu)=4\varepsilon_\mu\delta_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$
$$
\mathrm{tr}(\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)
=4\bigl(\varepsilon_\mu\delta_{\mu\nu}\varepsilon_\rho\delta_{\rho\sigma}
-\varepsilon_\mu\delta_{\mu\rho}\varepsilon_\nu\delta_{\nu\sigma}
+\varepsilon_\mu\delta_{\mu\sigma}\varepsilon_\nu\delta_{\nu\rho}\bigr).
$$
The contraction sums follow from the squares. With one index raised, $\gamma^\mu=-\varepsilon_\mu\gamma_\mu$, so that $\sum_\mu\gamma^\mu\gamma_\mu=-4I_4$, $\sum_\mu\gamma^\mu\gamma_\alpha\gamma_\mu=2\gamma_\alpha$, $\sum_\mu\gamma^\mu\gamma_\alpha\gamma_\beta\gamma_\mu=-4\varepsilon_\alpha\delta_{\alpha\beta}I_4$ and $\sum_\mu\gamma^\mu\gamma_\gamma\gamma_\beta\gamma_\alpha\gamma_\mu=-2\gamma_\gamma\gamma_\beta\gamma_\alpha$.
## Summary

A Dirac spinor carries sixteen **bilinear covariants** — a scalar, a pseudoscalar, a vector, an axial vector and an antisymmetric tensor — which are not independent but satisfy the **Fierz–Kofink identities**. The scalar part of the system is $J^2=\sigma^2+\omega^2$, $J^2=-K^2$, $J\cdot K=0$; the tensor part is $J_\mu K_\nu-J_\nu K_\mu=\omega S_{\mu\nu}+\sigma\tilde S_{\mu\nu}$, and both are displayed here in the corpus's own conventions. The identities are equivalently expressed through the **Fierz aggregate** $Z=4\psi\psi^{\dagger}\,iR_{\vec e_x}$, the rank-one operator whose sixteen basis operator coefficients are the covariants; it satisfies $Z^2=4\sigma Z$ and its companions and returns the spinor as $\psi=Z\zeta/(4\psi^{\dagger}\,iR_{\vec e_x}\zeta)$ — Lounesto's **boomerang**. The identities force the covariants into exactly **six classes**, three regular ($\sigma$ or $\omega$ nonzero) and three singular ($\sigma=\omega=0$, with the possible vanishings of $K$ and $S$): Dirac, the two other regular types, the **flag-dipole**, the flagpole and the dipole. All six classes were verified to be non-empty by explicit representatives. The flag-dipole is the type the usual list of Dirac, real and chiral spinors does not exhaust and the one the classification was introduced to expose. This article supplies the four-dimensional completion of the corpus's internal Fierz identity, which the bilinear article records as missing, and it states the classification in the corpus's signature, with every formula displayed here checked in that signature. It is pure Clifford-algebra mathematics, with no framework speculation, and it is the ambient companion of the two-dimensional Fierz identity the corpus already carries.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $iL_{e_t}R_{\vec e_x}$, $iL_{\vec e_k}R_{\vec e_y}$, $-iL_{e_t}R_{\vec e_z}$ | The frame basis operators, $L_{a}R_{b}$; the four basis operators $iR_{\vec e_x}$ and $iL_{\vec e_k}R_{\vec e_y}$ carry the basis operator relation of the material interval |
| $-iL_{e_t}R_{\vec e_z}$ | The chirality basis operator (pseudoscalar) |
| $\psi^{\dagger}\,iR_{\vec e_x}$ | Dirac adjoint |
| $\sigma=\psi^{\dagger}\,iR_{\vec e_x}\psi$, $\omega=i\psi^{\dagger}\,iR_{\vec e_x}\,-iR_{\vec e_z}\psi$ | Scalar and pseudoscalar densities |
| $J_0=\psi^{\dagger}\,iR_{\vec e_x}\,iR_{\vec e_x}\psi$ and $J_k=\psi^{\dagger}\,iR_{\vec e_x}\,iL_{\vec e_k}R_{\vec e_y}\psi$ | Vector |
| $K_0=-\psi^{\dagger}\,iR_{\vec e_x}\,(-iR_{\vec e_z})iR_{\vec e_x}\psi$ and $K_k=-\psi^{\dagger}\,iR_{\vec e_x}\,(-iR_{\vec e_z})iL_{\vec e_k}R_{\vec e_y}\psi$ | Axial vector |
| $S_{\mu\nu}=\psi^{\dagger}\,iR_{\vec e_x}\,\sigma_{\mu\nu}\psi$, $\sigma_{\mu\nu}$ the bivector of the Gamma section | Antisymmetric tensor |
| $J^2=\sigma^2+\omega^2=-K^2$, $J\cdot K=0$ | The scalar FPK identities |
| $Z=4\psi\psi^{\dagger}\,iR_{\vec e_x}$ | Fierz aggregate (boomerang), rank one |
| $Z^2=4\sigma Z$ | The aggregate form of the identities |
| $\psi=Z\zeta$ | The inversion theorem |
| flag-dipole, flagpole, dipole | The three singular classes $4,5,6$ |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](../articles_physics/why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- P. Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed., 2001), for the classification of spinors by their bilinear covariants, the Fierz aggregate and the boomerang; the origin of the classification.
- J. P. Crawford, "On the algebra of Dirac bispinor densities: factorization and inversion theorems," *Journal of Mathematical Physics* **26** (1985) 1439, and "Bispinor geometry for even-dimensional space-time," *Journal of Mathematical Physics* **31** (1990) 1991, for the Fierz identities and the inversion theorem.
- M. Fierz, "Zur Fermischen Theorie des $\beta$-Zerfalls," *Zeitschrift für Physik* **104** (1937) 553, and W. Kofink, "Über die Bilinearformen der Diracmatrizen," *Annalen der Physik* **30** (1937) 91, for the original identities.
- R. J. Bueno Rogerio, "Subliminal aspects concerning the Lounesto's classification," arXiv:1911.08506, and R. A. da Rocha and collaborators, "On the generalized spinor classification: beyond the Lounesto classification," arXiv:1906.11622, for the modern treatment of the six classes, the flag-dipole, the class-6 exceptional case and the aggregate form.
- B. Fauser, "On the equivalence of Daviau's space Clifford algebraic, Hestenes' and Parra's formulations of (real) Dirac theory," arXiv:hep-th/9908200, 1999, §3, for the pointer to Lounesto's programme and the "new unknown type of spinor".
- The companion articles of this series: *Bilinear Operators on the General Plain Sesqualgebra of Biquaternions* (the internal Fierz identity and its declared gap, filled here), [The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure](the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.html), [Peirce Carriers and Inner Conjugation](peirce-carriers-and-inner-conjugation.html), and [Parra's Four Options of the Dirac Equation and the Discrete Symmetries](../articles_physics/parras-four-options-of-the-dirac-equation-and-the-discrete-symmetries.html).
