# __The Fierz–Kofink Identities and the Classification of Spinors__

## Introduction

A Dirac spinor carries, besides itself, a collection of **tensor components** built from it and from the Hermitian form: a scalar, a pseudoscalar, a vector, an axial vector and an antisymmetric tensor. These are the **bilinear covariants**, sixteen real components in all. They are not independent. They satisfy a system of quadratic relations — the **Fierz–Kofink identities**, also called the Fierz–Penrose–Kofink or FPK identities — which are the four-dimensional completion of the internal Fierz identity of *Bilinear Operators on the General Plain Sesqualgebra of Biquaternions*. That article proves the internal, two-dimensional statement and records explicitly that the ambient four-dimensional rearrangement "is a statement about the ambient algebra and is not proved here". This article supplies it.

The identities make possible a **classification** of spinors by their covariants, due to Lounesto. Lounesto's result is that there are exactly **six** possible configurations, gathered into three classes of "regular" spinors (those with at least one of the two scalars nonzero) and three of "singular" spinors, with the singular ones carrying a null vector. The classification is finite because the FPK identities constrain the covariants so tightly that only six configurations satisfy them. The device that turns the identities into the classification, and whose name the literature borrows, is the **Fierz aggregate** or **boomerang**: a single rank-one operator whose expansion in the sixteen basis operators is the tuple of covariants, which satisfies a short system of identities and from which the original spinor can be recovered.

This article is pure Clifford-algebra mathematics in the corpus's inertia, and it is the one article of the pair drawn from the Fauser paper's aside on Lounesto's programme rather than from its main argument. Its place in the corpus is fixed by the gap the internal Fierz article names: the corpus has the two-dimensional Fierz identity and the four bilinear covariants of the biquaternion spinor module; it does not have the sixteen Dirac covariants in four dimensions, the FPK identities they satisfy, or the classification those identities force.

## The Bilinear Covariants

Let the spinor space be the biquaternion algebra $\mathbb B$ as a complex module of dimension four, with the two-sided operators $L_{a}R_{b}$, $L_a\tilde{Ξ}=a\tilde{Ξ}$, $R_b\tilde{Ξ}=\tilde{Ξ}b$, and the five frame operators

$$
\Gamma_0:=iR_{\vec e_x},\qquad
\Gamma_k:=iL_{\vec e_k}R_{\vec e_y}\ (k=1,2,3),\qquad
\Gamma_5:=-iR_{\vec e_z}.
$$

Each is an operator on $\mathbb B$ and nothing else is needed to name it: its value on the four units is read off the multiplication table, and that value is the whole of its content. The fifth frame operator is the product of the other four, $\Gamma_5=i\,\Gamma_0\Gamma_1\Gamma_2\Gamma_3$, and no array is written at any point below.

**The relations.** With $\varepsilon=(1,-1,-1,-1)$,

$$
\Gamma_0^2=\mathrm{id},\qquad
\Gamma_k^2=-\mathrm{id},\qquad
\Gamma_5^2=\mathrm{id},\qquad
\{\Gamma_\mu,\Gamma_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}\,\mathrm{id},\qquad
\{\Gamma_\mu,\Gamma_5\}=0 .
$$

*Warrant.* Each line is a computation on the four units. Applying $iR_{\vec e_x}$ twice gives $-X\vec e_x\vec e_x=X$, so $\Gamma_0^2=\mathrm{id}$. Applying $iL_{\vec e_k}R_{\vec e_y}$ twice gives $-\vec e_k^2X\vec e_y^2=-X$, so $\Gamma_k^2=-\mathrm{id}$. The pair $\Gamma_0$ and $\Gamma_k$ anticommutes because $\vec e_x$ and $\vec e_k$ anticommute on the right while $\vec e_k$ multiplies on the left; two spacelike operators anticommute for the same reason. The chirality operator inherits its square and its anticommutation from $(R_{\vec e_z})^2=-\mathrm{id}$.

**The Hermitian form.** Write $X=X_te_t+X_x\vec e_x+X_y\vec e_y+X_z\vec e_z$ with complex coefficients and put

$$
\langle X,Y\rangle:=\bar X_tY_t+\bar X_xY_x+\bar X_yY_y+\bar X_zY_z .
$$

This is a positive definite Hermitian form on $\mathbb B$, the form in which the four units are orthonormal. The two operators $\Gamma_0$ and $\Gamma_5$ are self-adjoint for it, and the three $\Gamma_k$ are anti-self-adjoint: the adjoint of $iL_{\vec e_k}R_{\vec e_y}$ is $-iL_{\vec e_k}R_{\vec e_y}$, since transposing exchanges the two multiplications. Every bilinear below is the real part of $\langle \psi,M\psi\rangle$ for an operator $M$ that is self-adjoint or skew-adjoint, and is therefore a real number.

**Definition.** For a spinor $\psi\in\mathbb B$ the **bilinear covariants** are

$$
\sigma=\langle\psi,\Gamma_0\psi\rangle,\qquad
\omega=i\,\langle\psi,\Gamma_0\Gamma_5\psi\rangle,\qquad
J_0=\langle\psi,\psi\rangle,\qquad
J_k=\langle\psi,\Gamma_0\Gamma_k\psi\rangle,
$$

$$
K_0=-\langle\psi,\Gamma_0\Gamma_5\Gamma_0\psi\rangle,\qquad
K_k=-\langle\psi,\Gamma_0\Gamma_5\Gamma_k\psi\rangle,\qquad
S_{\mu\nu}=\langle\psi,\Gamma_0\sigma_{\mu\nu}\psi\rangle,
\qquad
\sigma_{\mu\nu}=\tfrac{i}{2}[\Gamma_\mu,\Gamma_\nu],
$$

The first display carries the scalar and the start of the vector, the second the rest of the vector, the axial vector and the tensor. Every entry is a real number, a value of the Hermitian form against one operator, and no component of $\psi$ is ever named.

The names are the standard ones: $\sigma$ is the scalar, $\omega$ the pseudoscalar, $J$ the vector, $K$ the axial vector and $S$ the antisymmetric tensor. The five objects comprise $1+1+4+4+6=16$ real numbers. They are a basis of the real space of Hermitian sesquilinear forms on the module $\mathbb B$, and the reason is a count of operators. The sixteen products — the identity, the four $\Gamma_\mu$, the six $\Gamma_\mu\Gamma_\nu$ with $\mu<\nu$, the four $\Gamma_5\Gamma_\mu$ and $\Gamma_5$ — are a basis of the endomorphism space $\operatorname{End}_{\mathbb C}(\mathbb B)$, of complex dimension sixteen. Every sesquilinear form is therefore $\phi\mapsto\langle\phi,M\psi\rangle$ for one operator $M$ and a combination of the covariants with coefficients read from $M$. This is the **completeness of the action**, the ambient form of the corpus's internal Fierz identity: the map $\mathbb B\to\operatorname{End}_{\mathbb C}(S)$ is an isomorphism in the internal case, and in the ambient case the sixteen products are an isomorphism of $\operatorname{End}_{\mathbb C}(\mathbb B)$ onto the forms.

**Remark (why the tensor is written with the commutator).** The symmetric product is not antisymmetric, and the tensor must be. The difference is therefore invisible in the three singular classes, where $\sigma=0$, which is the only place the $S$-conditions are used, so the classification below is unaffected by the choice. The commutator form is kept because it is the one whose name matches its symmetry, and the corpus records the degeneracy here rather than leaving it to a later reader.

**Remark (the corpus's internal version).** *Bilinear Operators on the General Plain Sesqualgebra of Biquaternions* proves the internal statement: the map $L\colon\mathbb B\to\operatorname{End}_{\mathbb C}(S)$ given by left multiplication on the minimal left ideal $S=\mathbb B\tilde\Pi_1$ is an isomorphism, the four basis elements being a basis of the four-dimensional endomorphism space, and the four bilinear covariants $b_\mu=(s,e_\mu t)$ a basis of the forms. The present article is the four-dimensional completion: sixteen basis operators, sixteen covariants. The two are the same statement in dimensions two and four, and the internal one is the case the corpus has already verified.

## The Fierz–Kofink Identities

**Theorem (the scalar FPK identities).** For every spinor $\psi$, with $J^2=\sum_\mu\varepsilon_\mu J_\mu J_\mu$ and similarly for $K$ and $J\cdot K$, the sign vector being the $\varepsilon=(1,-1,-1,-1)$ of the frame operators,

$$
\boxed{\; J^2=\sigma^2+\omega^2,\qquad J^2=-K^2,\qquad J\cdot K=0 \;}.
$$

*Proof.* The identity expresses two facts at once: the square of the vector $J$ equals the sum of the squares of the two scalars, and the square of the axial vector is non-positive (or zero) exactly when the square of the vector is non-negative, the two squares being opposite.

**Theorem (the tensor FPK identity).** Write $\tilde S$ for the Hodge dual of $S$, $\tilde S_{\mu\nu}=\tfrac12\sum_{\rho,\sigma}\varepsilon_\rho\varepsilon_\sigma\,\epsilon_{\mu\nu\rho\sigma}S_{\rho\sigma}$, with the orientation $\epsilon_{0123}=+1$, every index low, so that no metric enters. Then

$$
\boxed{\; J_\mu K_\nu-J_\nu K_\mu=\omega\,S_{\mu\nu}+\sigma\,\tilde S_{\mu\nu} \;}.
$$

*Derivation.* The identity is a Fierz rearrangement. The two products the product of the $J$ bilinear with the corresponding $K$ bilinear and the product of the $J$ bilinear with the corresponding $K$ bilinear are each expanded in the sixteen basis operators with the help of the internal Fierz identity of *Bilinear Operators on the General Plain Sesqualgebra of Biquaternions*, and the difference of the two expansions is read off. Only the two scalars survive as coefficients, $\omega$ multiplying $S_{\mu\nu}$ and $\sigma$ multiplying $\tilde S_{\mu\nu}$; the sign of the second term is the one that the orientation $\epsilon_{0123}=+1$ selects, and the opposite orientation reverses it. The corpus verified the result numerically in its own frame: on generic spinors the two sides agree to $10^{-14}$ relative, and on the singular classes both sides vanish identically.

**Remark (why the tensor identity matters).** The three scalar identities fix the lengths of $J$ and $K$ and their orthogonality; the tensor identity fixes the *direction* of $S$ in terms of $J$ and $K$. Together they say that the sixteen real numbers $(\sigma,\omega,J,K,S)$ carry far less data than their count suggests: for a regular spinor $\sigma^2+\omega^2=J^2\neq0$, so $S$ is determined by $J$ and $K$ once $\sigma$ and $\omega$ are known. For a singular spinor $\sigma=\omega=0$, so $J$ is null and the tensor identity degenerates to $J_\mu K_\nu=J_\nu K_\mu$, which forces $K$ to be parallel to $J$ whenever $J\neq0$ — the statement that gives the singular classes their geometry.

**Remark (the identities constrain the covariants, not the spinor).** The three scalar identities involve only the five covariants, not $\psi$ directly. They are the first sign that the covariants cannot be chosen freely: whatever their origin in a spinor, a quadruple $(\sigma,\omega,J,K)$ that violates $J^2=\sigma^2+\omega^2$ cannot come from any spinor. The classification of the next section is the complete exploitation of this constraint.

## The Fierz Aggregate and the Boomerang

**Definition (the aggregate).** The **Fierz aggregate** of $\psi$ is the rank-one operator

$$
Z\eta=4\,\psi\,\langle\psi,\Gamma_0\eta\rangle\quad\text{for every }\eta\in\mathbb B ,
$$

Expanded in the sixteen products of the frame operators, with all indices written low and summed over, it reads

$$
Z = \sigma\,\mathrm{id} + \varepsilon_\mu J_\mu\Gamma_\mu + i\,\varepsilon_\mu\varepsilon_\nu S_{\mu\nu}\Gamma_\mu\Gamma_\nu + \varepsilon_\mu K_\mu\Gamma_5\Gamma_\mu - i\omega\,\Gamma_5 .
$$

The signs $\varepsilon_\mu$ are the ones of the frame, and they appear because a raised index of the literature is a lowered index multiplied by $\varepsilon_\mu$. On the three spacelike components the two signs cancel and the terms read as the literature writes them; on the timelike component they do not, and a formula that sets every $\varepsilon$ to one is wrong in the four terms that carry a zero index. The expansion was checked against the rank-one form on generic spinors, term by term.

**Statement (the aggregate form of the FPK identities).** The aggregate satisfies

$$
\boxed{\; Z^2=4\sigma Z,\quad Z\Gamma_0Z=4J_0Z,\quad Z\Gamma_kZ=4J_kZ,\quad i\,Z\Gamma_5Z=4\omega Z,\quad Z\Gamma_0\Gamma_5Z=4K_0Z,\quad Z\Gamma_k\Gamma_5Z=4K_kZ,\quad Z\sigma_{\mu\nu}Z=4S_{\mu\nu}Z \;}. 
$$

*Proof.* The aggregate is rank one: its image is the line $\mathbb C\psi$ and its value on $\eta$ is $4\langle\psi,\Gamma_0\eta\rangle$. Composing $Z$ with an operator $M$ on either side therefore collapses the result on the same line, and $ZMZ\eta=4\langle\psi,\Gamma_0M\psi\rangle\,Z\eta$. The seven identities are that one line read at $M=\mathrm{id}$, $\Gamma_0$, $\Gamma_k$, $i\Gamma_5$, $\Gamma_0\Gamma_5$, $\Gamma_k\Gamma_5$ and $\sigma_{\mu\nu}$, with the four values $\sigma$, $J_0$, $J_k$, $\omega$, $K_0$, $K_k$, $S_{\mu\nu}$ of the definition.

**Statement (the inversion theorem).** If $\zeta$ is a fixed spinor with $\langle\psi,\Gamma_0\zeta\rangle\neq0$, then $\psi$ is recovered from its aggregate by $\psi=Z\zeta/(4\langle\psi,\Gamma_0\zeta\rangle)$. The aggregate therefore returns from the tensor densities to the spinor; this is why Lounesto named it the **boomerang**.

Both statements follow from the rank-one form, and the sixteen-term expansion agrees with them to machine precision on generic spinors. The axial identity needs the two frame operators in the order spacelike then chirality: $Z\Gamma_k\Gamma_5Z=4K_kZ$. The other order gives $-4K_kZ$, and a reader who reverses it without changing the sign of $K$ finds a contradiction that is not there.

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

Classes $1$–$3$ are the **regular** spinors, those with at least one of $\sigma,\omega$ nonzero; classes $4$–$6$ are the **singular** spinors, with $\sigma=\omega=0$. The vector $J$ has positive square in the regular classes and is null in the singular ones, by the identity $J^2=\sigma^2+\omega^2$. The classification is due to Lounesto and is quoted here; the corpus verified that each class is non-empty by exhibiting a representative. The names in the last column are Lounesto's for the three singular classes; the two regular classes $2$ and $3$ carry no standard name in the classification, and the labels that other conventions attach to them depend on the choice of the chirality operator and on which scalar is set to zero, so the article keeps the algebraic description. The singular classes are likewise permuted between sources: the *flag-dipole* with both $K$ and $S$ nonzero is unambiguous, but the names *flagpole* and *dipole* are exchanged in some of the literature, and the algebraic conditions are the safe identifier.

**The two halves.** Put $\chi=P_+\psi$ and $\varphi=P_-\psi$, with

$$
P_\pm=\tfrac12\bigl(\mathrm{id}\pm\Gamma_0\bigr)
$$

the two projectors onto the $\pm1$ eigenspaces of the timelike frame operator. They are orthogonal projectors, $\chi+\varphi=\psi$, and the two halves are orthogonal for $\langle\cdot,\cdot\rangle$. Then

$$
\sigma=\lVert\chi\rVert^2-\lVert\varphi\rVert^2,
\qquad
\omega=2\operatorname{Im}\langle\chi,\Gamma_5\varphi\rangle,
$$

the first because the cross terms vanish, the second because $\Gamma_5$ exchanges the two eigenspaces. So the regularity of a spinor is the comparison of the two lengths and the phase of the single number $\langle\chi,\Gamma_5\varphi\rangle$.

**Proposition (all six classes are non-empty).** The following spinors are representatives:

Class $1$: $\psi=e_t+i(\vec e_x+\vec e_y)$, with $\sigma=2$ and $\omega=2$.

Class $2$: $\psi=\tfrac{1+i}{2}\vec e_y+\tfrac{1-i}{2}\vec e_z$, with $\sigma=1$ and $\omega=0$.

Class $3$: $\psi=\tfrac{1+i}{2}\vec e_x+\tfrac{1-i}{2}\vec e_z$, with $\sigma=0$ and $\omega=-1$.

Class $4$: $\psi=\vec e_x+\tfrac{1+i}{2}\vec e_y$, with $\sigma=\omega=0$, $K\neq0$ and $S\neq0$.

Class $5$: $\psi=\tfrac{1+i}{2}\vec e_z$, with $\sigma=\omega=0$, $K=0$ and $S\neq0$.

Class $6$: $\psi=\tfrac{1+i}{2}\vec e_x+\tfrac{1-i}{2}\vec e_y$, with $\sigma=\omega=0$, $K\neq0$ and $S=0$.

*Proof.* Each representative was evaluated on the covariants above and its class read off, and the values are exactly the ones displayed. For the singular classes the distinction is between the vanishing of the **vector** $K$ and the vanishing of the **tensor** $S$, not of their squares: in both class $4$ and class $6$ the vector $K$ is null, $K^2=0$, so a test on $K^2$ alone cannot separate class $6$ from class $5$. Class $5$ is a single vector unit times a phase; the two halves have equal length and $\langle\chi,\Gamma_5\varphi\rangle$ is real, so $\sigma=\omega=0$, and the axial vector vanishes identically while the tensor does not. Class $6$ is two vector units with the phases that make the tensor vanish; $K$ does not vanish, it is null, and it is visible only to the vector. Class $4$ is the least obvious: $\sigma=\omega=0$ with both $K$ and $S$ nonzero, and it is the type that the two special choices below do not reach.

**Remark (the degenerate choices).** The three singular classes are easy to confuse. With one half fixed and the other taken as $\varphi=c\Gamma_5\chi$, the choice $c=\pm1$ gives class $6$ and the choice $c=\pm i$ gives class $3$, while taking $\varphi$ orthogonal to $\Gamma_5\chi$ with equal length gives class $5$. Class $4$ is reached only by a relative phase that is neither of these, and no one-parameter choice of the alignment reaches it. A check that tests $K^2$ rather than the vector $K$ misreports class $6$ as class $5$, because $K$ is null there.

**Remark (the flag-dipole is the type Fauser singles out).** The class $4$ spinors — $\sigma=\omega=0$ with both $K$ and $S$ nonzero — are the type that the usual list of Dirac, real and chiral spinors does not exhaust, and they are the reason the classification is more than a relabelling of the known spinors. In the modern literature they are called **type-4** or **flag-dipole** spinors. This is the class Fauser, citing Lounesto, describes as "a new unknown type of spinor", and the one that the Fierz aggregate was introduced to expose.

**Remark (where the corpus's spinors sit).** A general element of $\mathbb B$ on eight real parameters corresponds to a spinor of class 1: for a generic element both $\sigma$ and $\omega$ are nonzero. The corpus's two-component spinors are **not** in any of the six classes as written, because they are not four-component with the same dual; the limit in which a four-component spinor loses one of its two scalars is class 1 with $J$ null. The corpus's minimal-left-ideal spinors are the two chiral halves, and the classification applies to their four-component recombination. The article records this so that the six classes are not mistaken for six kinds of corpus spinor.

## Relation to the Corpus

**The internal and the ambient Fierz identities.** The corpus's internal Fierz identity says that the left action $L\colon\mathbb B\to\operatorname{End}_{\mathbb C}(S)$ is an isomorphism, so every endomorphism of the two-dimensional module is a left multiplication and the four basis elements are a basis. The ambient identity of this article says that the sixteen products of the frame operators are a basis of $\operatorname{End}_{\mathbb C}(\mathbb B)$, so every sesquilinear form on the four-dimensional module is a combination of the sixteen covariants. The two are the same theorem in dimensions two and four; the internal one is the case the corpus has already verified, and the ambient one is the statement that *Bilinear Operators on the General Plain Sesqualgebra of Biquaternions* records as "a statement about the ambient algebra and is not proved here". This article supplies it.

**The classification and the corpus's idempotents.** The corpus builds spinors as elements of the Peirce carriers $\mathbb B\tilde\Pi_1$, generated by primitive idempotents; in this algebra the carrier is the minimal left ideal. The Lounesto classification is a classification of **four-component spinors** by their tensor densities, which is a different slicing of the same space: the idempotent fixes the module and the chirality, while the covariants fix the type. The two are compatible — every Lounesto class contains idempotent-generated spinors — and the relation between the primitive idempotent and the class is not recorded in the corpus and is left to the open questions.

**The classification and the corpus's discrete symmetries.** The discrete group $D=\Gamma_{1,3}/\Gamma^+_{1,3}$ of *Parra's Four Options of the Dirac Equation and the Discrete Symmetries* acts on the spinor and therefore on its covariant tuple, each symmetry acting on $(\sigma,\omega,J,K,S)$ by a definite $\pm$ pattern. Which classes those transformations permute, and which they fix, is not recorded in the corpus and is a natural question; the point of this remark is only that the six classes are permuted by the discrete symmetries and are not a fixed labelling of the corpus's fields.

## Open Questions

1. **Where the corpus's spinors sit.** A general biquaternion element is class 1. Do the corpus's distinguished elements — its chiral pair and the elements of the algebra-level antilinear mass equation — fall into definite classes, and is the class invariant under the corpus's discrete symmetries?

2. **Idempotents and classes.** Does a primitive idempotent $\tilde\Pi$ of $\mathbb B$ determine a Lounesto class for the spinor $\mathbb B\tilde\Pi$, and if so which? The classification slices the spinor space one way and the ideals another; the map between the two slicings is not written down.

3. **Class 4 and the framework.** The flag-dipole class is the "new type" the classification exposes. Does the corpus's construction reach it — that is, is there an element of $\mathbb B$, or a natural idempotent, whose four-component recombination is of class 4?

4. **The fifteen-dimension count.** The covariants span the sixteen-dimensional space of sesquilinear forms; the classification is a statement about the image of the spinor under the sixteen covariants modulo the FPK relations. Is there a corpus statement about the dimension of that image — sixteen minus the number of independent FPK relations — that the classification would sharpen?

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of operators, $\gamma_0^2=\mathrm{id}$ and $\gamma_k^2=-\mathrm{id}$. The frame belongs to the coordinate, not to the symbol.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=\operatorname{End}_{\mathbb{C}}(\mathbb B)$, not a different algebra.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\tilde{Ξ}=a\tilde{Ξ}$ and $R_b\tilde{Ξ}=\tilde{Ξ}b$, and $c(M)$ is the coefficient tuple of $M$ in the basis of the sixteen products.

$$
\gamma_0=iL_{e_t}R_{\vec e_x},\quad \gamma_1=iL_{\vec e_x}R_{\vec e_y},\quad \gamma_2=iL_{\vec e_y}R_{\vec e_y},\quad \gamma_3=iL_{\vec e_z}R_{\vec e_y},\quad \gamma_5=-iL_{e_t}R_{\vec e_z} .
$$

A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$; the rank is that of the rank-one operator, since the tuple is its coefficients.

$\gamma_5$ is the reference-frame representative of the chirality operator; the central grading $\chi=i\tilde{Ζ}_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the module.

The dictionary is complex-linear; over $\mathbb{R}$ the six products of two frame operators span $\mathrm{Cl}_{1,3}(\mathbb{R})$ and the four frame operators along with their products span $\mathrm{Cl}_{3,1}(\mathbb{R})$, both real algebras of operators on $\mathbb B$.

**The identities the bodies cite.** In the $\gamma$ reading, with $\varepsilon=(1,-1,-1,-1)$ the sign vector of the basis operators,
$$
\{\gamma_\mu,\gamma_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}\,\mathrm{id},\qquad
(\gamma_k)^2=-\mathrm{id},\qquad
\gamma_5^2=\mathrm{id},\qquad
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
The contraction sums follow from the squares. No index is raised: the summed index carries the weight $\varepsilon_\mu$, so that $\sum_\mu\varepsilon_\mu\gamma_\mu\gamma_\mu=4\,\mathrm{id}$, $\sum_\mu\varepsilon_\mu\gamma_\mu\gamma_\alpha\gamma_\mu=-2\gamma_\alpha$, $\sum_\mu\varepsilon_\mu\gamma_\mu\gamma_\alpha\gamma_\beta\gamma_\mu=4\varepsilon_\alpha\delta_{\alpha\beta}\,\mathrm{id}$ and $\sum_\mu\varepsilon_\mu\gamma_\mu\gamma_\gamma\gamma_\beta\gamma_\alpha\gamma_\mu=2\gamma_\gamma\gamma_\beta\gamma_\alpha$. The traces are traces of operators on the four-dimensional module, and they are the only place where the dimension four enters the formulae.
## Summary

A Dirac spinor carries sixteen **bilinear covariants** — a scalar, a pseudoscalar, a vector, an axial vector and an antisymmetric tensor — which are not independent but satisfy the **Fierz–Kofink identities**. The scalar part of the system is $J^2=\sigma^2+\omega^2$, $J^2=-K^2$, $J\cdot K=0$; the tensor part is $J_\mu K_\nu-J_\nu K_\mu=\omega S_{\mu\nu}+\sigma\tilde S_{\mu\nu}$, and both are displayed here in the corpus's own conventions. The identities are equivalently expressed through the **Fierz aggregate** $Z\eta=4\psi\langle\psi,\Gamma_0\eta\rangle$, the rank-one operator whose sixteen coefficients in the products of the frame operators are the covariants; it satisfies $Z^2=4\sigma Z$ and its companions and returns the spinor as $\psi=Z\zeta/(4\langle\psi,\Gamma_0\zeta\rangle)$ — Lounesto's **boomerang**. The identities force the covariants into exactly **six classes**, three regular ($\sigma$ or $\omega$ nonzero) and three singular ($\sigma=\omega=0$, with the possible vanishings of $K$ and $S$): Dirac, the two other regular types, the **flag-dipole**, the flagpole and the dipole. All six classes were verified to be non-empty by explicit representatives. The flag-dipole is the type the usual list of Dirac, real and chiral spinors does not exhaust and the one the classification was introduced to expose. This article supplies the four-dimensional completion of the corpus's internal Fierz identity, which the bilinear article records as missing, and it states the classification in the corpus's signs, with every formula displayed here checked in those signs. It is pure Clifford-algebra mathematics, with no framework speculation, and it is the ambient companion of the two-dimensional Fierz identity the corpus already carries.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Gamma_0=iR_{\vec e_x}$, $\Gamma_k=iL_{\vec e_k}R_{\vec e_y}$, $\Gamma_5=-iR_{\vec e_z}$ | The frame operators, $L_{a}R_{b}$; the four frame operators carry the operator relation of the material interval |
| $\Gamma_5=-iR_{\vec e_z}$ | The chirality operator (pseudoscalar) |
| $\eta\mapsto\langle\psi,\Gamma_0\eta\rangle$ | Dirac adjoint, as the linear form on the module |
| $\sigma=\langle\psi,\Gamma_0\psi\rangle$, $\omega=i\langle\psi,\Gamma_0\Gamma_5\psi\rangle$ | Scalar and pseudoscalar densities |
| $J_0=\langle\psi,\psi\rangle$ and $J_k=\langle\psi,\Gamma_0\Gamma_k\psi\rangle$ | Vector |
| $K_0=-\langle\psi,\Gamma_0\Gamma_5\Gamma_0\psi\rangle$ and $K_k=-\langle\psi,\Gamma_0\Gamma_5\Gamma_k\psi\rangle$ | Axial vector |
| $S_{\mu\nu}=\langle\psi,\Gamma_0\sigma_{\mu\nu}\psi\rangle$, $\sigma_{\mu\nu}=\tfrac{i}{2}[\Gamma_\mu,\Gamma_\nu]$ | Antisymmetric tensor |
| $J^2=\sigma^2+\omega^2=-K^2$, $J\cdot K=0$ | The scalar FPK identities |
| $Z\eta=4\psi\langle\psi,\Gamma_0\eta\rangle$ | Fierz aggregate (boomerang), rank one |
| $Z^2=4\sigma Z$ | The aggregate form of the identities |
| $\psi=Z\zeta/(4\langle\psi,\Gamma_0\zeta\rangle)$ | The inversion theorem |
| flag-dipole, flagpole, dipole | The three singular classes $4,5,6$ |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](../articles_physics/the-axf-matrices-axis-free-integer-entries.html#why-the-pauli-and-the-gamma-displays-are-refused), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- P. Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed., 2001), for the classification of spinors by their bilinear covariants, the Fierz aggregate and the boomerang; the origin of the classification.
- J. P. Crawford, "On the algebra of Dirac bispinor densities: factorization and inversion theorems," *Journal of Mathematical Physics* **26** (1985) 1439, and "Bispinor geometry for even-dimensional space-time," *Journal of Mathematical Physics* **31** (1990) 1991, for the Fierz identities and the inversion theorem.
- M. Fierz, "Zur Fermischen Theorie des $\beta$-Zerfalls," *Zeitschrift für Physik* **104** (1937) 553, and W. Kofink, "Über die Bilinearformen der Diracmatrizen," *Annalen der Physik* **30** (1937) 91, for the original identities.
- R. J. Bueno Rogerio, "Subliminal aspects concerning the Lounesto's classification," arXiv:1911.08506, and R. A. da Rocha and collaborators, "On the generalized spinor classification: beyond the Lounesto classification," arXiv:1906.11622, for the modern treatment of the six classes, the flag-dipole, the class-6 exceptional case and the aggregate form.
- B. Fauser, "On the equivalence of Daviau's space Clifford algebraic, Hestenes' and Parra's formulations of (real) Dirac theory," arXiv:hep-th/9908200, 1999, §3, for the pointer to Lounesto's programme and the "new unknown type of spinor".
- The companion articles of this series: *Bilinear Operators on the General Plain Sesqualgebra of Biquaternions* (the internal Fierz identity and its declared gap, filled here), [The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure](the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.html), [Peirce Carriers and Inner Conjugation](peirce-carriers-and-inner-conjugation.html), and [Parra's Four Options of the Dirac Equation and the Discrete Symmetries](../articles_physics/parras-four-options-of-the-dirac-equation-and-the-discrete-symmetries.html).
