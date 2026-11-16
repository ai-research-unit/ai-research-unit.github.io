# __From the Spin of the Rotor to the Spin of a Pair of Operators Acting on Two Sides__

## Introduction

A single rotor carries spin $\tfrac12$. The number comes from three real $4\times4$ matrices and one sum of squares, and it needs no complex two-vector and no table of coefficients. A pair of operators acting on two sides carries two such factors, one on the left and one on the right, and the pair carries spin $0$ and spin $1$. This article computes both numbers in the real display and states exactly what each step uses.

**The thread.** Left multiplication by a unit quaternion is a real orthogonal matrix. Its three generators square to minus the identity, so the sum of their squares is $-3\mathrm{I}_4$, and the Casimir of the halved generators is $\pm\tfrac34$. On an irreducible carrier the Casimir is $s(s+1)$, so $s=\tfrac12$. The pair is an element of the product group $S^3_L\times S^3_R$, each factor carries $\tfrac12$, and the addition rule for the irreducible carriers of the rotor group gives $0$ and $1$. The total Casimir then takes the values $0$ and $2$, and those are the only two values.

**What the article does not use.** No matrix group called $SU(2)$, no complex two-space, and no Clebsch–Gordan coefficients. The carriers are real, the generators are real antisymmetric matrices, and the multiplicities are read off as dimensions of eigenspaces. The complex display appears once, in a remark, as a bookkeeping device that the real computation does not need.

**Roadmap.** The rotor group comes first, then the single rotor and its Casimir, then the two-sided operator and the correction it needs, then the pair, then the addition rule, then the Casimir check on the two carriers, then what is and is not claimed. The corrections, the verification and the summary close the article.

## The Rotor Group

**Definition.** The **rotor group** is the group of unit quaternions,

$$
\mathrm{Rot}:=\{\tilde q\in\mathbb{H}:\langle\tilde q\rangle_{\natural}=1\}=\{\tilde q\in\mathbb{H}:\lvert\tilde q\rvert=1\}=S^3,
$$

under quaternion multiplication. Its real dimension is three. It is the spin group $Spin(3)$, and it is not a group of matrices: every matrix group below is an image of it.

**The double cover.** The map

$$
S^3\longrightarrow SO(3),\qquad \tilde q\longmapsto\bigl[\vec v\mapsto\tilde q\vec v\tilde q^{-1}\bigr],
$$

is a surjective homomorphism with kernel $\{\pm e_t\}$. A rotation by $2\pi$ corresponds to the rotor $-e_t$, and only a rotation by $4\pi$ corresponds to $+e_t$. This is the geometric origin of the half-integer numbers: the sphere covers the rotation group twice, so a carrier on which $-e_t$ acts as $-1$ is available, and it does not descend to the rotation group.

**The two names.** $Spin(3)$ and $\mathrm{Rot}$ denote one object. For $n\ge4$ the spin group is a cover of $SO(n)$ of dimension $\binom n2$ and is not a sphere; the identification with the rotor group is a statement about $n=3$ only.

**Remark (the excluded sentence).** The sentence "the rotor group is $SU(2)$" is excluded. $SU(2)$ is the image of the $2\times2$ complex display, and the isomorphism from $S^3$ to that image is a choice of display. Every statement below is a statement about $S^3$ and about real carriers, so the exclusion costs nothing here.

## The Single Rotor

**The generators.** On the real basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$ of $\mathbb{H}$, left multiplication by $\tilde q$ is $X\mapsto\tilde qX$, with matrix $L(\tilde q)_{\mu\nu}=[\tilde qe_\nu]_\mu$. The three generators $L_k:=L(\vec e_k)$ are real, antisymmetric, signed permutation matrices, and they satisfy

$$
L_k^2=-\mathrm{I}_4,\qquad [L_x,L_y]=2L_z\ \text{and cyclically.}
$$

The first identity is $\vec e_k^2=-e_t$ read in the display; the second is $\vec e_x\vec e_y-\vec e_y\vec e_x=2\vec e_z$ read in the display.

**The normalization.** With $J_k:=\tfrac12L_k$ the bracket is the standard one,

$$
[J_i,J_j]=\varepsilon_{ijk}J_k .
$$

**The Hermitian normalization.** The $J_k$ are real antisymmetric, hence anti-Hermitian, so the spectral statements are made with

$$
H_k:=iJ_k=\tfrac i2L_k,\qquad [H_i,H_j]=i\varepsilon_{ijk}H_k .
$$

The two normalizations differ by $i^2$ in every square, and the article states both wherever a sign is involved.

**The Casimir.** Define

$$
\mathbf{J}^2:=\sum_kJ_k^2,\qquad \mathbf{H}^2:=\sum_kH_k^2=-\mathbf{J}^2 .
$$

Since $L_k^2=-\mathrm{I}_4$,

$$
\mathbf{J}^2=\tfrac14(-3\mathrm{I}_4)=-\tfrac34\,\mathrm{I}_4,
\qquad
\mathbf{H}^2=+\tfrac34\,\mathrm{I}_4 .
$$

**The number.** On an irreducible carrier the Hermitian Casimir is $s(s+1)$ times the identity, by the definition of the spin of the carrier. Therefore

$$
s(s+1)=\tfrac34\quad\Longrightarrow\quad s=\tfrac12,
$$

the other root being $-\tfrac32$ and the spin being taken non-negative.

**The weights.** The eigenvalues of $H_z$ on $\mathbb{R}^4$ are $+\tfrac12$ and $-\tfrac12$, each twice. The weight set is $\{\pm\tfrac12\}$ and the carrier is the spin-$\tfrac12$ carrier.

**The dimension, and the factor of two.** The carrier has real dimension $4$ where $2s+1=2$. The factor of two is not an error: the spin-$\tfrac12$ carrier is of quaternionic type, so its smallest real form has twice the complex dimension. In general an irreducible carrier of spin $s$ has real dimension $2s+1$ for integer $s$ and $2(2s+1)$ for half-integer $s$. The two rules are used in the counting below.

**The statement.** The left-regular representation on $\mathbb{R}^4$ carries spin $\tfrac12$, and the three $L$-generators are the spin-$\tfrac12$ generators in real $4\times4$ form. This is the only spin the $L$-generators give, because they act on one carrier and that carrier is irreducible.

## The Two-Sided Operator

**Why two-sided.** Let $A$ be an associative algebra with a unit and let $R\in A$ be invertible. One-sided multiplication $\Lambda(X)=RX$ is multiplicative only when $R=e_t$. Conjugation $\Theta(X)=RXR^{-1}$ is multiplicative for every invertible $R$. The count of factors is the whole proof: $R(XY)$ carries one factor $R$ and $(RX)(RY)$ carries two, and no normalization repairs the count. A two-sided product is therefore forced, and it is the only inner-type action available.

**The corpus operator.** For the biquaternion algebra the operator is

$$
\Theta_{\natural}(\tilde Q):\ \tilde X\longmapsto\tilde Q\,\tilde X\,\tilde Q^{\natural},
$$

and its Hermitian partner is $\Theta_{*}(\tilde X)=\tilde Q\tilde X\tilde Q^{*}$. On a real quaternion the two marks agree, since $\natural$ is the quaternion conjugation and the complex conjugation of a real coefficient does nothing.

**Proposition (both operators, in closed form).** For invertible $\tilde Q$,

$$
\tilde Q\tilde X\tilde Q^{\natural}=\langle\tilde Q\rangle_{\natural}\,\tilde Q\tilde X\tilde Q^{-1},
\qquad
\Theta_{*}(\tilde X^{*})=\Theta_{*}(\tilde X)^{*} .
$$

*Proof.* $\tilde Q\tilde Q^{\natural}=\langle\tilde Q\rangle_{\natural}e_t$, so $\tilde Q^{\natural}=\langle\tilde Q\rangle_{\natural}\tilde Q^{-1}$. For the second, $\tilde Q\tilde X^{*}\tilde Q^{*}=(\tilde Q\tilde X\tilde Q^{*})^{*}$ because the adjoint reverses the order twice. ∎

**Corollary.** The $\natural$-operator is an algebra automorphism exactly on the norm-one surface, and there it is conjugation by the inverse. The $*$-operator preserves the involution for every $\tilde Q$, and it is conjugation by the inverse exactly when $\tilde Q^{*}=\tilde Q^{-1}$.

**The rotor.** For a real unit quaternion $\tilde u$ the two marks coincide, $\tilde u^{*}=\tilde u^{\natural}=\tilde u^{-1}$, so the two operators are the same operator and each is conjugation by the inverse. This is the sense in which a rotor is the element whose two-sided action is an inner automorphism with no scalar in front and no choice between the two forms. The action is a rotation of $\mathbb{H}$, and it is the double cover $S^3\to SO(3)$ when it is restricted to the imaginary part.

**The boost, and the correction the brief needs.** A boost is $\tilde U_{\mathrm b}=\cosh\tfrac\phi2\,e_t+i\sinh\tfrac\phi2\,\vec n$ with real unit $\vec n$. It is Hermitian, $\tilde U_{\mathrm b}^{*}=\tilde U_{\mathrm b}$, and that part of the usual statement is right. But its $\natural$-conjugate is $\cosh\tfrac\phi2\,e_t-i\sinh\tfrac\phi2\,\vec n$, and the product of the two is $\cosh^2-\sinh^2=1$, because $(i\vec n)^2=+e_t$. So

$$
\tilde U_{\mathrm b}^{\natural}=\tilde U_{\mathrm b}^{-1},
$$

and the $\natural$-operator **is** conjugation by the inverse on a boost. The honest form of the correction is this: on the rotor sphere the two operators coincide; on the boost sector they separate, and the one that fails to be inverse-conjugation is the $*$-operator, since $\tilde U_{\mathrm b}^{*}=\tilde U_{\mathrm b}\ne\tilde U_{\mathrm b}^{-1}$. The $\natural$-operator preserves the product on the whole norm-one surface, rotor and boost alike; the $*$-operator preserves the involution everywhere and the product only on the unitary elements.

**The general Lorentz element.** A general element is a product of a boost and a rotor, and it has norm one as well. So the $\natural$-operator is conjugation by the inverse on the whole Lorentz group, and the $*$-operator is not. The sentence to keep is: *the two-sided form is compulsory; it is conjugation by the inverse exactly on the norm-one surface of the mark in use.*

**The right factor is an anti-homomorphism.** Write $R(\tilde p)$ for right multiplication, $X\mapsto X\tilde p$. Then $R(\tilde q)R(\tilde p)=R(\tilde p\tilde q)$, because $(X\tilde p)\tilde q=X(\tilde p\tilde q)$. The map $\tilde q\mapsto R(\tilde q)$ is therefore an anti-homomorphism, and the pair $(\tilde q,\tilde p)\mapsto[X\mapsto\tilde qX\tilde p]$ is an action of $S^3_L\times S^3_R$ in which the right factor composes in reverse order. Two consequences are used below: the right generators obey $[R_x,R_y]=-2R_z$ while the left ones obey $[L_x,L_y]=+2L_z$, and the diagonal rotation $X\mapsto\tilde qX\tilde q^{-1}$ has generator $J_k-J'_k$, not $J_k+J'_k$, where $J'_k=\tfrac12R(\vec e_k)$.

## The Pair

**The group and the carrier.** A pair of operators acting on two sides is an element of

$$
S^3_L\times S^3_R,\qquad (\tilde q,\tilde p)\longmapsto\bigl[X\mapsto\tilde qX\tilde p\bigr],
$$

acting on $\mathbb{H}$, of real dimension four. The map is onto $SO(4)$ with kernel $\{\pm(\mathrm{I}_4,\mathrm{I}_4)\}$, so the pair is the classical double cover $Spin(4)\to SO(4)$, and the two factors commute: $L(\tilde q)R(\tilde p)=R(\tilde p)L(\tilde q)$ for all $\tilde q,\tilde p$.

**The two Casimirs.** Each factor has its own Casimir, built from its own generators,

$$
C_L=\sum_kJ_k^2=-\tfrac34\,\mathrm{I}_4,
\qquad
C_R=\sum_kJ_k^{\prime 2}=-\tfrac34\,\mathrm{I}_4 .
$$

Each factor is spin $\tfrac12$. The two Casimirs commute, because the two families of generators commute, and each is a scalar on the carrier.

**The total generators.** The diagonal generators of the pair, which are the generators of the rotation $X\mapsto\tilde qX\tilde q^{-1}$, are

$$
J_k^{\mathrm{tot}}:=J_k-J'_k,
$$

and they obey the standard bracket, $[J_i^{\mathrm{tot}},J_j^{\mathrm{tot}}]=\varepsilon_{ijk}J_k^{\mathrm{tot}}$, since the minus sign in the right bracket cancels the minus sign in the combination. The total Casimir is

$$
\mathbf{J}^2_{\mathrm{tot}}:=\sum_k\bigl(J_k^{\mathrm{tot}}\bigr)^2 .
$$

**The second carrier.** There is a second object that the phrase *a pair of rotors* can mean, and the two must be kept apart.

- **Carrier A**, $\mathbb{H}$ itself, real dimension $4$. This is the carrier of the two-sided action $X\mapsto\tilde qX\tilde p$. The pair acts on it and the diagonal generators are $J_k-J'_k$.
- **Carrier B**, $\mathbb{H}\otimes\mathbb{H}$, real dimension $16$. This is the state space of two independent rotor systems, each in the left-regular carrier. The generators are $J_k\otimes\mathrm{I}+\mathrm{I}\otimes J_k$, by the Leibniz rule of a derivation.

The brief of this article names $\mathbb{R}^{16}$ and the generators $J_k\otimes\mathrm{I}+\mathrm{I}\otimes J_k$; those belong to carrier B. Both carriers are computed below, because the claim *the pair carries $0$ and $1$* is true on both, and the multiplicities differ.

## The Addition Rule

**The theorem.** The irreducible unitary carriers of the rotor group are labelled by

$$
j\in\tfrac12\mathbb{Z}_{\ge0}=\{0,\tfrac12,1,\tfrac32,2,\ldots\},
$$

the carrier of label $j$ carrying the Casimir $j(j+1)$ and having complex dimension $2j+1$. For two labels $j_1,j_2$ the tensor product decomposes as a direct sum of irreducible carriers, each occurring once,

$$
j_1\otimes j_2=\bigoplus_{j=\lvert j_1-j_2\rvert}^{j_1+j_2} j .
$$

This is a theorem about the representation theory of the rotor group, equivalently about its Lie algebra. It is not a formula about complex matrices, and no coefficient is computed in this article; the statement used here is the list of labels, and the labels are identified with the numbers $0$ and $1$ by the Casimir, in the next section.

**The case of two rotors.** With $j_1=j_2=\tfrac12$,

$$
\tfrac12\otimes\tfrac12=0\oplus1,
\qquad\text{that is}\qquad j_{\mathrm{tot}}\in\{0,1\}.
$$

**The dimension bookkeeping, over the reals.** The carrier of label $\tfrac12$ has real dimension $4$ and the carriers of labels $0$ and $1$ have real dimensions $1$ and $3$. On carrier A the count is $4=1+3$, one copy each. On carrier B the count is $16=4\cdot1+4\cdot3$, four copies each. The two counts are consistent with the same labels, and the difference between them is the multiplicity, not the spin.

**What the rule does and does not say.** It says which labels occur and that each occurs once in the decomposition of the tensor product of two irreducibles. It does not say that a given carrier is irreducible, and it does not give the eigenvalues of the Casimir by itself. The eigenvalues are computed directly, and the agreement of the two computations is the check.

**Remark (no Clebsch–Gordan coefficients).** A treatment by complex two-vectors would expand the four basis products in a table of coefficients. That table is one way to prove the theorem, and it is not the theorem. Nothing in the argument below needs a coefficient, because nothing below projects onto a particular vector: the splitting is by the eigenspaces of one symmetric operator, and the eigenvalues are read from its spectrum.

## The Casimir Check

**Carrier A, direct computation.** The Hermitian total generators are $H_k-H'_k$, and their Casimir has the spectrum

$$
\mathbf{H}^2_{\mathrm{tot}}\Big|_{\mathbb{H}}:\quad 0\ \text{once},\qquad 2\ \text{three times.}
$$

The weights of $H_z-H'_z$ are $\{-1,0,+1\}$, so the three-dimensional part is the carrier of label $1$ and the one-dimensional part is the carrier of label $0$. The one-dimensional part is the line $\mathbb{R}e_t$, on which conjugation fixes every point.

**Carrier B, direct computation.** The Casimir of $H_k\otimes\mathrm{I}+\mathrm{I}\otimes H_k$ has the spectrum

$$
\mathbf{H}^2_{\mathrm{tot}}\Big|_{\mathbb{H}\otimes\mathbb{H}}:\quad 0\ \text{four times},\qquad 2\ \text{twelve times.}
$$

On the four-dimensional part every weight is $0$; on the twelve-dimensional part the weights are $+1$ and $-1$, four times each, and $0$ four times. By the real-dimension rule of *The Single Rotor*, the two parts are four copies of label $0$ and four copies of label $1$, and $4\cdot1+4\cdot3=16$.

**Theorem (the Casimir is a projector, up to an affine map).** On each carrier the Hermitian total Casimir is

$$
\mathbf{H}^2_{\mathrm{tot}}=2\bigl(\mathrm{I}-Q\bigr),
$$

where $Q$ is the orthogonal projection onto the part of label $0$. On carrier A, $Q=\mathrm{I}_4+\tfrac12\sum_k(J_k-J'_k)^2$ has rank $1$ and image $\mathbb{R}e_t$. On carrier B, $Q=\tfrac14\mathrm{I}_{16}+\sum_kJ_k\otimes J_k$ has rank $4$.

*Proof.* For carrier A, expand $\sum_k(J_k-J'_k)^2$ using $[J_k,J'_l]=0$ and $\sum_kJ_k^{\prime 2}=\sum_kJ_k^2=-\tfrac34\mathrm{I}_4$. The result is $\sum_k(J_k-J'_k)^2=2Q-2\mathrm{I}_4$ with $Q$ as displayed, and the sign change to the Hermitian normalization gives $\mathbf{H}^2_{\mathrm{tot}}=2(\mathrm{I}_4-Q)$. That $Q$ is an orthogonal projection is checked by $Q^2=Q$ and $Q^{\mathsf T}=Q$, and its rank is its trace. Carrier B is the same expansion with $\sum_kJ_k\otimes J_k$ in place of the cross term; the identities $Q^2=Q$ and $Q^{\mathsf T}=Q$ hold there too, and the trace is $4$. ∎

**Two consequences.** First, the total Casimir has exactly two eigenvalues, $0$ and $2$, so the composite carries exactly the two labels $0$ and $1$ and no third. Second, the projecting operator $Q$ commutes with the total generators but **not** with the generators of a single factor: on carrier B the commutator of $Q$ with $J_k\otimes\mathrm{I}$ is $\tfrac14$ in norm. That is the precise sense in which the split into $0$ and $1$ belongs to the pair and not to either factor alone.

**The full turn, as a second reading.** The rotor of a full turn is $-e_t$. On the single carrier it acts as $\exp(2\pi J_z)=-\mathrm{I}_4$, which is the reason a single rotor needs the double cover. On carrier A the same turn is $\exp(2\pi(J_z-J'_z))=\mathrm{I}_4$, and on carrier B it is $\mathrm{I}_{16}$; both are identity, so both pair carriers are actions of the rotation group and not merely of its double cover. A half turn is not the identity on either: its spectrum contains $-1$ on the part of label $1$ in both cases, and $+1$ on the part of label $0$.

**Why the check is not circular.** The total Casimir is defined by a sum of squares of explicit matrices, and its spectrum is computed from those matrices. The addition rule is a theorem about labels, stated independently. The two agree, and neither was used to obtain the other. What the agreement buys is that the labels $0$ and $1$ are the labels of the two pieces, and the multiplicities $1+3$ and $4+12$ are the multiplicities of those labels.

## What Is and Is Not Claimed

**Claimed.** Each factor of the pair carries spin $\tfrac12$, by the computation on $\mathbb{R}^4$. The pair carries spin $0$ and spin $1$ and nothing else, on either carrier, by the addition rule and by the spectrum of the total Casimir. The two-sided action is forced, and the diagonal generator of the pair is $J_k-J'_k$.

**Not claimed.** The pair does not contain spin $2$. Two factors of $\tfrac12$ reach at most $1$, and each further factor raises the maximum by $\tfrac12$, so spin $2$ needs four factors and spin $\tfrac32$ needs three. The pair does not contain a half-integer piece either: the spectrum of the total Casimir is $\{0,2\}$ with no intermediate value.

**Not claimed either.** The $L$-generators do not give all spins. They act on one carrier, that carrier is irreducible, and its label is $\tfrac12$. Another label needs another carrier and the same Casimir read there — on the vector part of the algebra the label is $1$ and the value is $2$, and on the fixed line the label is $0$ and the value is $0$.

**One sentence.** The single rotor is the carrier of label $\tfrac12$; the pair is the direct sum of the carriers of labels $0$ and $1$; the passage from one to the other is the addition rule, and the Casimir confirms it.

## Corrections

**The sentences that must not be written.** Each is an error of fact or of scope, and each has a repair above.

1. **"The rotor group is $SU(2)$."** The rotor group is $S^3$. $SU(2)$ is the image of one complex display, and the isomorphism is a choice.
2. **"The $L$-generators give all spins."** They give $\tfrac12$, on $\mathbb{R}^4$. Other spins need other carriers.
3. **"A boost has $\tilde U_{\mathrm b}^{\natural}\ne\tilde U_{\mathrm b}^{-1}$, so the two-sided operator is not inverse-conjugation on the boost sector."** The premise is false: a boost has norm one, so $\tilde U_{\mathrm b}^{\natural}=\tilde U_{\mathrm b}^{-1}$ and the $\natural$-operator is inverse-conjugation on it. The operator that fails to be inverse-conjugation there is the $*$-operator, since $\tilde U_{\mathrm b}^{*}=\tilde U_{\mathrm b}$.
4. **"The pair contains spin $2$."** It contains $0$ and $1$. Spin $2$ needs four factors.
5. **"The pair carries spin $\tfrac12$ again."** The total Casimir has no half-integer value on either carrier. The half-integer belongs to one factor, not to the pair.
6. **"The right multiplication is a homomorphism, so the total generator is $J_k+J'_k$."** Right multiplication is an anti-homomorphism, $R(\tilde q)R(\tilde p)=R(\tilde p\tilde q)$, its generators obey $[R_x,R_y]=-2R_z$, and the diagonal rotation generator is $J_k-J'_k$. The combination $J_k+J'_k$ generates $X\mapsto\tilde qX\tilde q$, which is not a group action at all.
7. **"The decomposition is the complex formula $\mathbf{2}\otimes\mathbf{2}=\mathbf{1}\oplus\mathbf{3}$, imported."** The formula is a matrix realization of the theorem. The theorem is the addition rule for the labels of the rotor group, and the real computation confirms it with real matrices.
8. **"Differentiate at $R=1$."** The Lie algebra is the tangent space at the identity; the phrase "differentiate at $R=1$" mixes a matrix entry with a group element.
9. **"The proof is circular, because the Casimir is used to define the spin and the addition rule to define the Casimir."** Neither is used to define the other. The Casimir is a sum of squares of explicit matrices, the addition rule is a theorem about labels, and the two agree.
10. **"The Casimir of the real antisymmetric generators is $+\tfrac34$."** It is $-\tfrac34$; the Hermitian normalization $H_k=iJ_k$ gives $+\tfrac34$. Both appear above, and the sign is the sign of $i^2$.

## Verification

**How the numbers were obtained.** All matrices were built from the multiplication table of $\mathbb{H}$, with no library quaternion type. The right-regular matrices were built as the columns $e_\nu\tilde q$ and checked against the anti-homomorphism law. The Casimir spectra were obtained by diagonalising the sum of squares of explicit $4\times4$ and $16\times16$ matrices. The exponentials were obtained from the eigen-decomposition of the generator, not from a closed form.

| claim | what was computed | residual or value |
| --- | --- | --- |
| the left generators are antisymmetric | $L_k+L_k^{\mathsf T}$ | $0$ |
| the left bracket | $[L_x,L_y]-2L_z$ | $0$ |
| the halved bracket | $[J_x,J_y]-J_z$ | $0$ |
| the Hermitian bracket | $[H_x,H_y]-iH_z$ | $0$ |
| the two families commute | $[J_k,J'_l]$ | $0$ |
| right multiplication is an anti-homomorphism | $R(\tilde q\tilde p)-R(\tilde p)R(\tilde q)$ | $1.8\cdot10^{-15}$ |
| the right bracket | $[J'_x,J'_y]+J'_z$ | $0$ |
| the single-rotor Casimir | $\sum_kJ_k^2+\tfrac34\mathrm{I}_4$ and $\sum_kH_k^2-\tfrac34\mathrm{I}_4$ | $0$ |
| the single-rotor weights | eigenvalues of $H_z$ | $\pm\tfrac12$, each twice |
| carrier A: total bracket | $[J^{\mathrm{tot}}_x,J^{\mathrm{tot}}_y]-J^{\mathrm{tot}}_z$ | $0$ |
| carrier A: Casimir spectrum | eigenvalues of $\mathbf{H}^2_{\mathrm{tot}}$ | $0$ once, $2$ thrice |
| carrier A: weights | eigenvalues of $H_z-H'_z$ | $\{-1,0,+1\}$ |
| carrier A: projector | $Q^2-Q$, $Q-Q^{\mathsf T}$, $\operatorname{tr}Q$ | $0$, $0$, $1$ |
| carrier A: Casimir $=2(\mathrm{I}-Q)$ | $\mathbf{H}^2_{\mathrm{tot}}-2(\mathrm{I}_4-Q)$ | $0$ |
| carrier B: Casimir spectrum | eigenvalues of $\mathbf{H}^2_{\mathrm{tot}}$ | $0$ four times, $2$ twelve times |
| carrier B: weights | eigenvalues of $H_k\otimes\mathrm{I}+\mathrm{I}\otimes H_k$ | $\pm1$ four each, $0$ eight times |
| carrier B: projector | $Q^2-Q$, $Q-Q^{\mathsf T}$, $\operatorname{tr}Q$ | $0$, $0$, $4$ |
| carrier B: Casimir $=2(\mathrm{I}-Q)$ | $\mathbf{H}^2_{\mathrm{tot}}-2(\mathrm{I}_{16}-Q)$ | $0$ |
| carrier B: $Q$ commutes with the total generators | $[Q,H^{\mathrm{tot}}_z]$ | $0$ |
| carrier B: $Q$ does not commute with one factor | $[Q,H_z\otimes\mathrm{I}]$ | $0.25$ |
| full turn on the single carrier | $\exp(2\pi J_z)$ | $-\mathrm{I}_4$ |
| full turn on carrier A | $\exp(2\pi(J_z-J'_z))$ | $\mathrm{I}_4$ |
| full turn on carrier B | $\exp(2\pi(H_z\otimes\mathrm{I}+\mathrm{I}\otimes H_z))$ | $\mathrm{I}_{16}$ |
| half turn on the pair | $\exp(\pi\cdot)$ on both carriers | spectrum contains $-1$ |

**The two rows that carry the article.** The two Casimir spectra are the whole result: $0$ and $2$ are the only values, and $j(j+1)$ with $j\in\{0,1\}$ are the only solutions. The two projector rows show why: the Casimir is an affine function of a projection, so its spectrum has exactly two values by construction and not by accident.

**One check that is not numerical.** The addition rule is a theorem about all labels, and no sample confirms it. What the numbers confirm is the case $\tfrac12\otimes\tfrac12$: two values, the multiplicities $1+3$ and $4+12$, and the labels forced by the real dimensions.

## Summary

The rotor group is $S^3$, of real dimension three, and it is $Spin(3)$. Its double cover of $SO(3)$ has kernel $\{\pm e_t\}$, a full turn upstairs is $-e_t$, and this is where half-integer carriers come from.

Left multiplication gives three real antisymmetric generators with $L_k^2=-\mathrm{I}_4$ and $[L_x,L_y]=2L_z$. Halving them gives $[J_i,J_j]=\varepsilon_{ijk}J_k$ and the Casimir $\sum_kJ_k^2=-\tfrac34\mathrm{I}_4$, or $+\tfrac34\mathrm{I}_4$ in the Hermitian normalization $H_k=iJ_k$. On the irreducible carrier $\mathbb{R}^4$ the Casimir is $s(s+1)$, so $s=\tfrac12$, and the weights $\pm\tfrac12$ confirm it. The real dimension is $4$ where $2s+1=2$, because the carrier is quaternionic.

The two-sided product is forced, since one-sided multiplication is multiplicative only for the unit. The corpus operator $\tilde X\mapsto\tilde Q\tilde X\tilde Q^{\natural}$ equals the norm times conjugation by the inverse, so it is an automorphism exactly on the norm-one surface, and on the rotor sphere the two marks coincide and the operator is conjugation by the inverse with no ambiguity. On the boost sector $\natural$ is still the inverse, since a boost has norm one; the operator that fails there is the $*$-operator. The right factor of a two-sided action is an anti-homomorphism, and the diagonal rotation generator is $J_k-J'_k$.

The pair is $S^3_L\times S^3_R$, acting on $\mathbb{H}$ of real dimension four, with two commuting Casimirs each $-\tfrac34$. The addition rule for the labels of the rotor group gives $\tfrac12\otimes\tfrac12=0\oplus1$. The total Casimir is $2(\mathrm{I}-Q)$ with $Q$ the projection onto the singlet part: on $\mathbb{H}$ its spectrum is $0$ once and $2$ three times, and on $\mathbb{H}\otimes\mathbb{H}$ it is $0$ four times and $2$ twelve times. The values $0$ and $2$ are $j(j+1)$ at $j=0$ and $j=1$, and those are the two spins of the pair.

A full turn is $-1$ on the single carrier and $+1$ on both pair carriers, so the pair is an action of the rotation group. The projection $Q$ commutes with the total generators and not with either factor alone, which is the precise sense in which the split belongs to the pair.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\mathrm{Rot}=S^3=Spin(3)$ | the rotor group, the unit quaternions |
| $\mathbb{H}$, $e_t,\vec e_x,\vec e_y,\vec e_z$ | the quaternion algebra and its real basis |
| $\natural$, $*$ | quaternion conjugation and the Hermitian adjoint $*=\bar{\cdot}\circ\natural$ |
| $\langle\tilde Q\rangle_{\natural}$ | the value of the quaternion norm on $\tilde Q$ |
| $\Theta_{\natural}$, $\Theta_{*}$ | $\tilde X\mapsto\tilde Q\tilde X\tilde Q^{\natural}$ and $\tilde X\mapsto\tilde Q\tilde X\tilde Q^{*}$ |
| $L(\tilde q)$, $L_k$ | the real left-regular matrix and its three generators |
| $R(\tilde q)$, $R_k$ | the real right-regular matrix and its three generators |
| $J_k=\tfrac12L_k$, $J'_k=\tfrac12R_k$ | the halved left and right generators |
| $H_k=iJ_k$ | the Hermitian generators, $[H_i,H_j]=i\varepsilon_{ijk}H_k$ |
| $\mathbf{H}^2=\sum_kH_k^2$ | the quadratic Casimir, $s(s+1)$ on an irreducible carrier |
| $J_k^{\mathrm{tot}}=J_k-J'_k$ | the diagonal generators of the pair on $\mathbb{H}$ |
| $J_k\otimes\mathrm{I}+\mathrm{I}\otimes J_k$ | the generators of two independent systems on $\mathbb{H}\otimes\mathbb{H}$ |
| $Q$ | the orthogonal projection onto the part of label $0$; $\mathbf{H}^2_{\mathrm{tot}}=2(\mathrm{I}-Q)$ |
| $s$, $j$ | the spin of a carrier, read from the Casimir and the real dimension |

## Further Reading

- [From the Rotor to the Spin of the Rotor](from-the-rotor-to-the-spin-of-the-rotor.html), for the single-rotor Casimir, the forcing of the two-sided product and the tensor square of the rotor carrier.
- [The Rotor Group via 4×4 Real Matrices](the-rotor-group-via-4x4-real-matrices.html), for the left-regular display, its generators, its exponential and the two isoclinic copies of $S^3$ in $SO(4)$.
- [The Two-Sided Operators and the Spin Group](the-two-sided-operators-and-the-spin-group.html), for the two-sided operators of the biquaternion algebra and their relation to the spin group.
- [The Carriers, the Representation, the Spin and the Closure](the-carriers-the-representation-the-spin-and-the-closure.html), for the three carriers, the spin table and the identity $2s+1=\dim$.
- [Hermitian Pair of N-Regular, Spectrally Regular Operators Acting on Two Sides](hermitian-pair-of-n-regular-spectrally-regular-operators-acting-on-two-sides.html), for the operator $\Theta_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*}$ and its multiplicativity.
- [The Pin and Spin Groups of the Quaternion Algebra](the-pin-and-spin-groups-of-the-quaternion-algebra.html), for the Clifford description of the same groups.
- I. R. Porteous, *Clifford Algebras and the Classical Groups*, ch. 13 and 16, for the spin groups, the double covers and $Spin(4)\cong S^3\times S^3$.
- S. Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces*, ch. II and III, for the Casimir element and the addition rule for the labels of a compact group.
