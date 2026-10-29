# __Element and Operator Representations: The Three Actions__

## Introduction

One biquaternion can be written in five standard matrix-shaped ways, and the five divide into two kinds. The **element representations** answer what the element is: the four-vector of complex coefficients, the $2\times2$ complex matrix $\mathsf{M}_2(\tilde Q)$, and the $4\times4$ left regular matrix $\mathsf{M}_4^{L}(\tilde Q)$. The **operator representations** answer what the element does: the $2\times2$ congruence $X\mapsto \mathsf{M}_2(\tilde Q)X\mathsf{M}_2(\tilde Q)^{\dagger}$ and the $4\times4$ sandwich. The first kind is linear in the element; the second is quadratic. That difference is the whole content of the article.

The physical stake is a distinction that is easy to lose. A state is carried by an element representation, a transformation by an operator representation. A spinor is a coordinate on a Peirce carrier, which in the $2\times2$ matrix model is a two-component column on which the $2\times2$ matrix acts; a four-vector is an element of the material sector on which the sandwich acts. Reading the determinant of the regular matrix as the norm, or the sandwich as a linear map of its parameter, or the doubled regular picture as two particles, are the three standard errors that the distinction prevents.

The article is a reader and owns no new theorem. Each result is stated in a sentence, the mathematics article that proves it is linked, and the physical reading is given with its boundary. It is the entry of the *Element and Operator Representations* group that fixes the vocabulary the other representation articles use.

The operator side is stated once, here. An element acts in three ways: left multiplication and right multiplication, which carry an element with one side fixed, and the sandwich, which acts on both sides and carries a frame. The composition laws, the adjoint for the plain form, the two-sided pair and the Peirce decomposition are the grammar the rest of the category uses. The matrix pictures of the three actions are the subject of the operator sections; the operator calculus itself is not repeated in a separate article.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The coefficient space and the norm | [The Biquaternion Algebra and Its Vector Spaces](../articles_maths/the-biquaternion-algebra-and-its-vector-spaces.html) |
| The algebra isomorphism $\mathsf{M}_2$, the trace, the determinant, the sectors and the ideals | [$M_2(\mathbb{C})$ Representation : The Matrix Product and the Algebra Structure](../articles_maths/m2c-representation-the-matrix-product-and-the-algebra-structure.html) |
| The left regular matrix, its determinant $N^2$, its trace $4Q_t$ and its block decomposition | [$M_4(\mathbb{C})_L$ Representation : The Matrix Product and the Algebra Structure](../articles_maths/m4c-representation-the-matrix-product-and-the-algebra-structure.html) |
| The right regular matrix and its relation to the left one | [$M_4(\mathbb{C})_L$ Representation : The Matrix Product and the Algebra Structure](../articles_maths/m4c-representation-the-matrix-product-and-the-algebra-structure.html) |
| The congruence, the two-sided maps and the enveloping operator algebra | [The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure](../articles_maths/the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.html) |
| The sandwich, its spectrum, determinant, trace and rank | [$M_4(\mathbb{C})_L$ Representation : The Matrix Product and the Algebra Structure](../articles_maths/m4c-representation-the-matrix-product-and-the-algebra-structure.html), §*The Sandwich in the Regular Basis*, for the matrix, the determinant and the trace; [Two-Sided Operator and the Polar Decomposition of a N-Regular, Spectrally Regular Biquaternion](../articles_maths/two-sided-operator-and-the-polar-decomposition-of-a-n-regular-spectrally-regular-biquaternion.html), §*The Spectrum of the Sandwich*, for the spectrum, and §*The Vanishing of the Modulus*, for the rank |
| The module structure and the Hilbert structure of the spinor space | [Modules over the Biquaternion Algebra](../articles_maths/modules-over-the-biquaternion-algebra.html) |
| The left and right multiplications, their kernels and their images | [One-Sided Operators on the Biquaternion Algebra](../articles_maths/one-sided-operators-on-the-biquaternion-algebra.html) |
| The two-sided operators, their types and their composition | [Two-Sided Operators on the Biquaternion Algebra](../articles_maths/two-sided-operators-on-the-biquaternion-algebra.html) |
| The transpose, association and the swap of the sides | [Association and the Transpose on the Quaternion Algebra](../articles_maths/association-and-the-transpose-on-the-quaternion-algebra.html) |
| The monoid of acting maps and the enveloping algebra | [The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure](../articles_maths/the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.html) |
| The rotor action on the two sectors and the double cover | [Biquaternion Rotations and Lorentz Transformations](../articles_maths/biquaternion-rotations-and-lorentz-transformations.html) |
| The coefficient dictionary of the two sectors | [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](../articles_maths/the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html) |

## Five Pictures of One Element

The five pictures are five images of the same eight real numbers. The table records the carrier of each, the dependence on the element, and the one thing the picture makes visible.

| Picture | Object | Carrier | Dependence on $\tilde Q$ | What it shows |
| --- | --- | --- | --- | --- |
| Four-vector | the column $Q$ | $\mathbb{C}^4$ | linear, the identity | the coordinates and the sectors |
| $2\times2$ element | $\mathsf{M}_2(\tilde Q)$ | $\mathbb{C}^2$ | linear | the spinor, the trace and the determinant |
| $4\times4$ left regular | $\mathsf{M}_4^{L}(\tilde Q)$ | $\mathbb{B}$ | linear | the element acting on the algebra |
| $2\times2$ operator | $X\mapsto M X M^{\dagger}$ | $M_2(\mathbb{C})$ | quadratic | the rank, the positivity and the collapse |
| $4\times4$ operator | $X\mapsto \tilde Q X\tilde Q^{*}$ | $\mathbb{B}$ | quadratic | the spectrum, the determinant and the rank |

A sixth object is the **four-vector operator**, the sandwich written on the material sector. It is a coordinate shadow of the $2\times2$ congruence and is treated with the operators below.

The first three pictures are linear in $\tilde Q$: doubling the element doubles the matrix. The last two are quadratic: doubling the element multiplies the operator by four, because $\tilde Q X\tilde Q^{*}$ has two slots. The element picture is also basis-dependent: the column changes with the choice of basis while the matrix changes by similarity, and the operator picture is the invariant object behind both.

The count of the parameters is the same in every picture: four complex coefficients, hence eight real numbers. The $2\times2$ matrix has four complex entries, the $4\times4$ regular matrix has sixteen complex entries constrained to a four-complex-dimensional subspace, and the operator has sixteen complex entries constrained by the same four parameters. None of the pictures adds a parameter; each adds a way of reading the same eight.

## The Physical Dictionary

The four-vector picture is the one that carries the dictionary. The four complex coefficients are not four independent physical coordinates: each coefficient holds one material and one informational coordinate. In the conventions of the corpus,

$$
Q^t = c t + i c t', \qquad Q^x = x + i x', \qquad Q^y = y + i y', \qquad Q^z = z + i z'.
$$

The real part of the scalar coefficient is the informational time and the imaginary part is the material time; each vector coefficient carries one material and one informational spatial coordinate.

| Sector | Condition on the coefficients | Four-vector | Physical object |
| --- | --- | --- | --- |
| Material $\mathbb{M}_-$ | $Q_t$ purely imaginary, $Q_k$ real | $(i c t', x, y, z)$ | four-position, four-momentum, four-velocity |
| Informational $\mathbb{M}_+$ | $Q_t$ real, $Q_k$ purely imaginary | $(c t, i x', i y', i z')$ | state, observable, field strength |
| Real quaternion $\mathbb{H}_{\mathbb{B}}$ | all four coefficients real | $(q_t, q_x, q_y, q_z)$ | rotor, scale, ordinary quaternion |

The split is a reading and not a theorem of the algebra. What the algebra supplies is the Hermitian conjugation ${}^{*}$, whose fixed and anti-fixed subspaces are the two sectors; the identification of the anti-fixed subspace with the material four-vectors and of the fixed one with the informational objects is the physical hypothesis of the framework. The dictionary is consistent because the norm restricts to the Minkowski interval on $\mathbb{M}_-$ and to its negative on $\mathbb{M}_+$.

## The Element Representations

### The Four-Vector

The four-vector is the coefficient list

$$
\tilde Q = Q_t e_t + Q_x \vec e_x + Q_y \vec e_y + Q_z \vec e_z, \qquad Q_\mu\in\mathbb{C}.
$$

Its product is the bilinear map on $\mathbb{C}^4$ whose scalar component is $Q_t R_t-\vec Q\cdot\vec R$ and whose vector component is $Q_t\vec R+R_t\vec Q+\vec Q\times\vec R$. The norm is the central complex number

$$
N=\langle\tilde Q\rangle_{\natural}=Q_t^2+Q_x^2+Q_y^2+Q_z^2,
$$

multiplicative and indefinite; the element is a unit exactly when $N\neq0$, and then $\tilde Q^{-1}=\tilde Q^{\natural}/N$.

The four-vector is a coordinate list of an element of the algebra. It is **not** a Dirac spinor and **not** a column of the regular representation: it is the element written in its own basis, and the number four is the dimension of the algebra, not the dimension of the spin module. The spinor is two-dimensional and appears in the next picture.

### The $2\times2$ Element

The isomorphism $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ is written on the Pauli matrices,

$$
\boxed{\;\mathsf{M}_2(\tilde Q)=Q_t\mathrm{I}_2-i\bigl(Q_x\sigma_x+Q_y\sigma_y+Q_z\sigma_z\bigr)
=\begin{pmatrix}Q_t-iQ_z & -iQ_x-Q_y\\ -iQ_x+Q_y & Q_t+iQ_z\end{pmatrix}\;}.
$$

The two matrix invariants are the two physical invariants of the element:

$$
\operatorname{Tr}\mathsf{M}_2(\tilde Q)=2Q_t, \qquad \det\mathsf{M}_2(\tilde Q)=N.
$$

In the $2\times2$ image the trace is twice the scalar part, the determinant is the norm, and the unit-norm slice is $\mathrm{SL}(2,\mathbb{C})$. The Hermitian conjugation ${}^{*}$ becomes the conjugate transpose, so $\mathbb{M}_+$ and $\mathbb{M}_-$ become the Hermitian and anti-Hermitian matrices. The determinant is the interval on the material sector; on the informational sector its sign is the causal type, and a Hermitian matrix is a state exactly when it is positive, which requires both a positive trace and a non-negative determinant.

The matrix acts on a two-component column. That column is the **spinor**, and the action is the left multiplication of the algebra on its simple module. The two columns of the matrix algebra are the two minimal left ideals, which the corpus calls the two chiralities; this article writes **column chirality** for that column-index convention. The spinor picture is the smallest picture that carries the state; it does not carry the four-vector.

### The $4\times4$ Left Regular Element

The left regular matrix $\mathsf{M}_4^{L}(\tilde Q)$ is the matrix of the map $X\mapsto \tilde Q X$ in the basis $e_t,\vec e_x,\vec e_y,\vec e_z$. Its invariants are the doubled invariants:

$$
\det\mathsf{M}_4^{L}(\tilde Q)=N^2, \qquad \operatorname{Tr}\mathsf{M}_4^{L}(\tilde Q)=4Q_t.
$$

In a basis adapted to the two minimal left ideals the matrix is block diagonal,

$$
\mathsf{M}_4^{L}(\tilde Q)\cong\begin{pmatrix}A_+(\tilde Q)&0\\0&A_-(\tilde Q)\end{pmatrix},
\qquad A_\pm(\tilde Q)\sim\mathsf{M}_2(\tilde Q),
$$

and each block has trace $2Q_t$ and determinant $N$. The regular picture is the spinor picture taken twice. The two blocks are the two column chiralities; left multiplication preserves each of them, which is why the matrix is block diagonal.

The determinant is a **volume**, not the norm. On a four-position it is $s^4$, on a four-velocity $c^4$, on an on-shell four-momentum $m^4c^4$, and on a lightlike four-vector it vanishes. The square does not change the zero set, so the light-cone statement survives the doubling, but it changes the degree: an identity that holds to the first power of $N$ in the $2\times2$ picture holds to the second power here.

The right regular matrix $\mathsf{M}_4^{R}(\tilde Q)$ is the matrix of $X\mapsto X\tilde Q$. It is not the transpose of the left one; the relation uses the sign matrix $D=\operatorname{diag}(-1,1,1,1)$, and the two matrices are genuinely different as soon as the algebra is non-commutative. The left copy preserves the two column chiralities and the right copy is the only one that can move between them. This is the structural reason the mass term is a right multiplication, and it is read in the operator article.

## The Operator Representations

### The Sandwich

The one operator that both matrix pictures realize is the sandwich

$$
\operatorname{H}_{\tilde Q}(X)=\tilde Q X\tilde Q^{*}.
$$

It is linear in the argument $X$ and quadratic in the parameter $\tilde Q$. In the $2\times2$ picture it is the congruence $X\mapsto M X M^{\dagger}$; in the $4\times4$ picture it is the product of the two regular maps,

$$
\boxed{\;\operatorname{H}_{\tilde Q}=\mathsf{M}_4^{L}(\tilde Q)\,\mathsf{M}_4^{R}(\tilde Q^{*})\;}.
$$

The sandwich is multiplicative in its parameter, $\operatorname{H}_{\tilde Q}\operatorname{H}_{\tilde U}=\operatorname{H}_{\tilde Q\tilde U}$, but it is not linear, and on the unit group it is not faithful: $\operatorname{H}_{\lambda\tilde Q}=|\lambda|^2\operatorname{H}_{\tilde Q}$, so every central phase of modulus one gives the same operator. It is a quadratic map that descends to a faithful representation of the unit group modulo its central phase circle, not a linear one.

### The $2\times2$ Congruence

On matrices the operator is

$$
X\longmapsto M X M^{\dagger}, \qquad M=\mathsf{M}_2(\tilde Q).
$$

Off the cone, $M$ is invertible, the congruence is a bijection, it preserves the rank of every argument, and it scales the determinant by $|\det M|^2=|N|^2$. On the cone, $M$ has rank one and the congruence collapses: every image is a multiple of the Hermitian rank-one matrix $u u^{\dagger}$, the image is a single complex line, and the operator has rank one. The value of the trace $4|Q_t|^2$ decides whether the surviving operator is nilpotent ($Q_t=0$) or a scaled projection ($Q_t\neq0$).

The congruence is a completely positive map with a single Kraus operator. It is trace-preserving exactly when $M$ is $*$-unitary, that is for the $*$-unitary elements; otherwise it rescales the trace. On the cone it is a destructive map: it projects every operand onto one line and erases the distinctions between them. The algebra supplies the shape of a quantum channel and of a measurement; it does not supply the probability rule for the outcomes.

### The $4\times4$ Operator

On the algebra the same sandwich is the matrix $\operatorname{H}_{\tilde Q}=\mathsf{M}_4^{L}(\tilde Q)\mathsf{M}_4^{R}(\tilde Q^{*})$. If $\mathsf{M}_2(\tilde Q)$ has eigenvalues $\lambda_1,\lambda_2$, the operator has the four eigenvalues

$$
\lambda_1\bar\lambda_1,\quad \lambda_1\bar\lambda_2,\quad \lambda_2\bar\lambda_1,\quad \lambda_2\bar\lambda_2,
$$

and therefore

$$
\boxed{\;\det\operatorname{H}_{\tilde Q}=|N|^4, \qquad \operatorname{Tr}\operatorname{H}_{\tilde Q}=4|Q_t|^2, \qquad \operatorname{rank}\operatorname{H}_{\tilde Q}=\bigl(\operatorname{rank}\mathsf{M}_2(\tilde Q)\bigr)^2\;}.
$$

The invariants are real and non-negative for every element, and they are not the invariants of the element matrix: the element matrix has complex determinant $N^2$ and complex trace $4Q_t$, while the operator has thrown the phase away. The operator is invertible exactly off the cone, has rank four there and rank one on it, and is zero only at zero.

The operator's trace and determinant remember only the time coordinate and the modulus. The operator itself remembers more: it determines the parameter up to a central phase, so the scale, the boost axis and the rotor are recoverable from it. The phase alone is lost, because the operator is quadratic and phase-blind.

### The Four-Vector Operator

On the material sector the sandwich is the frame action

$$
\operatorname{H}_{\tilde Q}(\tilde W)=\tilde Q\tilde W\tilde Q^{*}, \qquad \tilde W\in\mathbb{M}_-.
$$

It is linear in the four-vector and quadratic in the frame. On the identity it returns $\tilde Q\tilde Q^{*}$, whose scalar part is $\sum_\mu|Q_\mu|^2$, the Euclidean square of the Born form, and not the indefinite interval $\sum_\mu Q_\mu^2$. The two numbers answer different questions: the positive one is a probability weight, the indefinite one a spacetime length. The operator carries the positive one because it acts on the algebra and not on the metric.

A boost mixes time and space, a rotation does not; on the cone the operator collapses to a projection or a nilpotent. The absence of a rest frame for a null four-vector is the physical face of the collapse. These are the coordinate forms of the $2\times2$ statements, and the article on the four-vector operator owns the computations.

## The Three Actions

### The Three Families

The element acts on the algebra in three ways, distinguished by the side on which the parameter stands:

$$
L_{\tilde Q}(X)=\tilde Q X, \qquad R_{\tilde Q}(X)=X\tilde Q, \qquad \operatorname{H}_{\tilde Q}(X)=\tilde Q X\tilde Q^{*}=L_{\tilde Q}R_{\tilde Q^{*}}(X).
$$

| family | parameter dependence | what it carries | kernel | image |
| --- | --- | --- | --- | --- |
| $L_{\tilde Q}$ | linear | an element acting on the left | $\{0\}$ if $\tilde Q$ is a unit; otherwise $\{X:\tilde QX=0\}$ | $\tilde Q\mathbb{B}$, a right ideal |
| $R_{\tilde Q}$ | linear | an element acting on the right | $\{0\}$ if $\tilde Q$ is a unit; otherwise $\{X:X\tilde Q=0\}$ | $\mathbb{B}\tilde Q$, a left ideal |
| $\operatorname{H}_{\tilde Q}$ | quadratic | a frame acting on both sides | $\{0\}$ if $\tilde Q$ is a unit; otherwise $\{X:\tilde QX\tilde Q^{*}=0\}$ | $\tilde Q\mathbb{B}\tilde Q^{*}$ |

All three are $\mathbb{C}$-linear in the argument $X$. The assignments are injective in the parameter, but not all are injective as assignments of operators: $L_{\tilde Q}=L_{\tilde U}$ iff $\tilde Q=\tilde U$, while $\operatorname{H}_{\tilde Q}=\operatorname{H}_{\tilde U}$ can hold for different parameters, because a central phase cancels.

The distinction is between **carriage** and **frame change**. A one-sided map has a nontrivial kernel in its argument exactly when the parameter is not a unit; it drags an object without compensating the other side, and it changes the scale and in general the sector of what it acts on. The sandwich acts on both sides at once, preserves the two sectors, and is the algebraic shape of a change of frame. The physical Lorentz transformation is a sandwich, not a multiplication. The mass term is a right multiplication, and that is why it can move between the two chiralities while a left multiplication cannot.

### The Composition Laws

The one-sided maps compose by multiplying their parameters:

$$
L_{\tilde A}L_{\tilde B}=L_{\tilde A\tilde B}, \qquad R_{\tilde A}R_{\tilde B}=R_{\tilde B\tilde A}, \qquad L_{\tilde A}R_{\tilde B}=R_{\tilde B}L_{\tilde A}.
$$

The reversal in the right family is the anti-automorphism of the composition of maps: $(R_{\tilde A}R_{\tilde B})(X)=X\tilde B\tilde A=R_{\tilde B\tilde A}(X)$. The left and right families commute, because multiplication in the algebra is associative.

The two-sided maps compose by

$$
\bigl(L_{\tilde A}R_{\tilde B}\bigr)\bigl(L_{\tilde C}R_{\tilde D}\bigr)=L_{\tilde A\tilde C}R_{\tilde D\tilde B},
$$

and the sandwich is the special case in which the right parameter is the Hermitian conjugate of the left:

$$
\operatorname{H}_{\tilde Q}\operatorname{H}_{\tilde U}=\operatorname{H}_{\tilde Q\tilde U}.
$$

The sandwich is multiplicative in its parameter but not linear: $\operatorname{H}_{\lambda\tilde Q}=|\lambda|^2\operatorname{H}_{\tilde Q}$, and $\operatorname{H}_{\tilde Q+\tilde U}\neq\operatorname{H}_{\tilde Q}+\operatorname{H}_{\tilde U}$ in general. It is a quadratic map that descends to a representation of the unit group modulo its central phase circle. The one-sided families generate the full endomorphism algebra; the sandwich alone does not, being an eight-real-parameter family of maps rather than a sixteen-real-parameter algebra.

### The Adjoint and the Swap

For the plain bilinear form $\langle X,Y\rangle=\operatorname{Sc}(XY)$, the adjoint is the **associate** $T^{\approx}$:

$$
\langle L_{\tilde Q}X,Y\rangle=\operatorname{Sc}(\tilde QXY)=\operatorname{Sc}(XY\tilde Q)=\langle X,R_{\tilde Q}Y\rangle,
$$

so

$$
\bigl(L_{\tilde Q}\bigr)^{\approx}=R_{\tilde Q}, \qquad \bigl(R_{\tilde Q}\bigr)^{\approx}=L_{\tilde Q}, \qquad \bigl(L_{\tilde A}R_{\tilde B}\bigr)^{\approx}=L_{\tilde B}R_{\tilde A}.
$$

The adjoint **swaps the sides and does not conjugate the parameter**. This separates it from the Hermitian dagger, which keeps the side and conjugates, and from the quaternionic and signed adjoints. The type criteria follow: a left multiplication is self-adjoint exactly when $\tilde Q$ is central; a nonzero one-sided operator is never skew-adjoint; a nonzero two-sided operator is self-adjoint exactly when its parameters are proportional over $\mathbb{C}$.

The physical reading is the absence of orientation in the measuring pairing. The plain form pairs two displacements and returns a number; it does not know which factor is on the left. The orientation of a process is in the commutator $XY-YX$, not in the form. The form measures the symmetric data and leaves the orientation to the commutator.

### The Two-Sided Operator as a Pair

A two-sided operator is a pair of parameters, and only the relative data are physical:

$$
L_{\tilde A}R_{\tilde B}=L_{\tilde C}R_{\tilde D}
\iff \tilde C=\lambda\tilde A,\quad \tilde D=\lambda^{-1}\tilde B,
\qquad \lambda\in\mathbb{C}^{\times}.
$$

The identity is the pair $(\lambda e_t,\lambda^{-1}e_t)$. A frame change is specified by an operand and its adjoint operand, and a common central phase cancels between them. The pair, not either member, is the physical object. The operator is invertible exactly when both parameters are units; if either is a zero divisor, the kernel is nontrivial. This is the operator-level form of the cone: the non-invertible two-sided maps are exactly those whose pair meets it.

### The Sandwich: Sectors, Congruence, Self-Adjointness

The sandwich has three properties that the general two-sided operator does not.

**It preserves the two sectors.** For $X\in\mathbb{M}_\pm$,

$$
(\tilde QX\tilde Q^{*})^{*}=\tilde QX^{*}\tilde Q^{*}=\pm\,\tilde QX\tilde Q^{*},
$$

so the image lies in the same sector. This is why the Lorentz transformation of a four-vector is a sandwich and not a general two-sided map.

**It is a congruence.** In the matrix picture it is $X\mapsto MXM^{\dagger}$, which preserves rank off the cone, scales the determinant by $|\det M|^2=|N|^2$, and collapses to a rank-one line on the cone.

**It is self-adjoint for the Hermitian form exactly when its parameter is a phase multiple of a sector element.** For $\langle X,Y\rangle_{*}=\operatorname{Sc}(X^{*}Y)$,

$$
\bigl(\operatorname{H}_{\tilde Q}\bigr)^{\dagger}=\operatorname{H}_{\tilde Q^{*}},
$$

so the sandwich is self-adjoint iff $\tilde Q^{*}=\lambda\tilde Q$ with $|\lambda|=1$, equivalently iff a central-phase multiple of $\tilde Q$ lies in $\mathbb{M}_+$ or $\mathbb{M}_-$. The criterion is algebraic; it does not by itself make the self-adjoint sandwiches observables. A Lorentz boost is a Hermitian parameter, hence gives a self-adjoint sandwich, and it is a transformation, not an observable.

On the $*$-unitary slice $\tilde Q\tilde Q^{*}=e_t$, the sandwich is the inner automorphism $\operatorname{Ad}_{\tilde Q}$: it preserves the product, not only the sector. Off the slice it is a congruence that scales the interval. On the null cone it survives as a rank-one map; the nilpotent and the scaled projection are its two faces.

### The Monoid of Acting Maps

The left multiplications form a monoid under composition, isomorphic to the multiplicative monoid of $\mathbb{B}$:

$$
L_{\tilde A}L_{\tilde B}=L_{\tilde A\tilde B}, \qquad L_{e_t}=\mathrm{id}.
$$

The reversible elements are the units of the algebra, that is the elements off the cone. The right multiplications form the opposite monoid, and the two-sided maps form a monoid whose units are the pairs of units.

The reading is the **process–state split**. A process is an acting map: it composes, it can be undone exactly when it is a unit, and the reversible processes form a group. A state is an idempotent: it is the fixed point of a projection and it is not a map of the same kind. The algebra supplies both in one object, and the cone is the boundary between the reversible and the irreversible. The monoid is not a $C^{*}$-algebra; a kernel is not a measurement, and the passage from an invertible map to a non-invertible one is the collapse, not the mere vanishing of the norm.

### The Peirce Decomposition

Relative to a Hermitian idempotent $\tilde\Pi$, the algebra splits into four corners:

$$
X=\tilde\Pi X\tilde\Pi+\tilde\Pi X(1-\tilde\Pi)+(1-\tilde\Pi)X\tilde\Pi+(1-\tilde\Pi)X(1-\tilde\Pi).
$$

In block form, the two diagonal corners are the **populations** and the two off-diagonal corners are the **coherences**. Hermitian conjugation fixes the populations and exchanges the coherences. The Peirce decomposition is the operator-level form of the state/observable split: the idempotent is the two-outcome observable, with eigenvalues $0$ and $1$, and the four corners are the four ways an element can sit relative to it.

The left multiplication by $\tilde\Pi$ keeps the first row and kills the second; the right multiplication by $\tilde\Pi$ keeps the first column and kills the second. The minimal left ideals are the column supports, and left multiplication preserves them. The right multiplication by the nilpotent moves between them. That is the structural reason the mass coupling is a right action: the left action preserves each column ideal, and the right action is the one that can carry an element from one to the other.

## Physical Readings

**The spinor and the regular picture.** The $2\times2$ picture is the spinor picture: a biquaternion acts on a two-component column. The $4\times4$ picture is that same action written on the algebra itself, and it is the spinor picture taken twice. The two blocks are the two column chiralities, not two particles; the doubling is the dimension of the module, not a doubling of the physical state space. The column chirality is not the module chirality: the two ideals are isomorphic, while the module chiral halves are $S$ and its conjugate module $\bar S$, which are inequivalent as complex modules and isomorphic only as real representations. *Spin and the Three Elementary Carriers* states the same warning.

**The double cover.** The norm-one group is $\mathrm{SL}(2,\mathbb{C})=\mathrm{Spin}(1,3)$, and it covers the proper orthochronous Lorentz group two-to-one with kernel $\{\pm \mathrm{I}_2\}$. A rotation through $2\pi$ gives $-\mathrm{I}_2$ and a rotation through $4\pi$ gives $\mathrm{I}_2$. The sign is the sign of the spinor, and it is the discrete difference between the spinor picture and the four-vector picture.

**The mass coupling.** Left multiplication preserves each column chirality, so a mass term that couples the two column chiralities cannot be a left multiplication. It is a right multiplication by a nilpotent element, which maps one minimal left ideal onto the other and annihilates the second. In the $4\times4$ picture this is the off-diagonal block that the left regular matrix does not have; in the $2\times2$ picture it is the right action that the column picture does not show.

**The central phase.** A central phase is a scalar matrix. It multiplies the element matrix, it multiplies the determinant by $\lambda^2$, and it disappears from the sandwich. The element picture sees the phase; the operator picture does not. This is why the polar word carries the phase and the sandwich does not.

**The degree of the determinant.** The $2\times2$ determinant is $N$, the $4\times4$ determinant is $N^2$, and the operator determinant is $|N|^4$. Only the zero sets agree. A computation that reads a determinant must say which picture it is in.

**The trace factor.** The trace of the $2\times2$ matrix is $2Q_t$, the trace of the regular matrix is $4Q_t$, and the trace of the operator is $4|Q_t|^2$. The factor two is the number of column chiralities; the factor four is the dimension of the regular module or the number of matrix units. The factors are bookkeeping, not physics, but they are the bookkeeping in which the factor-of-two errors of the corpus live.

**The three actions.** A left multiplication and a right multiplication carry an element with one side fixed; they are the operators of carriage, and they change the scale and in general the sector of what they act on. The sandwich acts on both sides and carries a frame; it preserves the two sectors, and the physical Lorentz transformation is a sandwich, not a multiplication. The mass term is a right multiplication, which is why it can move between the two chiralities while a left multiplication cannot.

**The plain adjoint swaps the sides.** The adjoint for $\langle X,Y\rangle=\operatorname{Sc}(XY)$ is the associate, $L_{\tilde Q}^{\approx}=R_{\tilde Q}$. It does not conjugate the parameter. The form measures the symmetric data; the orientation of a process is in the commutator, not in the form. Self-adjointness for the plain form is not hermiticity, and the observables are not the self-adjoint elements of this family.

**The two-sided pair.** A two-sided operator is a pair $(\tilde A,\tilde B)$ defined up to a common central factor, $(\lambda\tilde A,\lambda^{-1}\tilde B)$. A frame change is specified by an operand and its adjoint operand, and a common phase cancels. The operator is invertible exactly when both parameters are units; the non-invertible two-sided maps are exactly those whose pair meets the cone.

**The monoid is the process–state split.** The acting maps compose; the reversible ones are the units off the cone, and they form a group. The states are the idempotents, which are fixed points and not maps of the same kind. The cone is the boundary between the reversible and the irreversible. The monoid is not a $C^{*}$-algebra, and a kernel is not a measurement.

**The Peirce corners are the state/observable split.** The diagonal corners are the populations and the off-diagonal corners the coherences. Left multiplication preserves the column ideals; right multiplication by the nilpotent moves between them. That is the operator-level reason the mass coupling is a right action.

## The Correspondence Table

| Named object | Four-vector | $2\times2$ element | $4\times4$ left regular | Sandwich operator |
| --- | --- | --- | --- | --- |
| The element | $Q\in\mathbb{C}^4$ | $M\in M_2(\mathbb{C})$ | $M_4^{L}\in M_4(\mathbb{C})$ | $\operatorname{H}_{\tilde Q}\in\operatorname{End}\mathbb{B}$ |
| Identity | $(1,0,0,0)$ | $\mathrm{I}_2$ | $\mathrm{I}_4$ | $\mathrm{id}$ |
| Scalar part | $Q_t$ | $\tfrac12\operatorname{Tr}$ | $\tfrac14\operatorname{Tr}$ | — |
| Weight | — | — | — | $\tfrac14\operatorname{Tr}=\lvert Q_t\rvert^2$ |
| Norm data | $\sum_\mu Q_\mu^2$ | $\det=N$ | $\det=N^2$ | $\det=\lvert N\rvert^4$ |
| Unit group | $N\neq0$ | $\mathrm{GL}(2,\mathbb{C})$ | invertible iff $N\neq0$ | invertible off the cone |
| Centre | $\mathbb{C}e_t$ | scalar matrices | scalar matrices | scalars |
| Material sector | $i\mathbb{R}\oplus\mathbb{R}^3$ | anti-Hermitian matrices | the subspace $Q\,\mathbb{M}_-$ | invariant subspace |
| Informational sector | $\mathbb{R}\oplus i\mathbb{R}^3$ | Hermitian matrices | the subspace $Q\,\mathbb{M}_+$ | invariant subspace |
| Chirality | — | column ideal | block | — |
| Pure state | idempotent | rank-one projection | block projector | rank-one projector |

The table is a dictionary, not a definition. Each row is proved in the mathematics article named in the first table; the physical reading of each row is owned by the sector articles, the state articles and the operator articles. The table's use is to prevent a result proved in one picture from being read in another without translation.

## Limits

The article states the correspondences and no dynamics. It does not derive the Lorentz transformation, the Dirac equation or the measurement update; it supplies the dictionary in which those derivations are written.

The four-vector is read off the action on the material sector, not off the doubled regular picture. The regular picture's two blocks are the two column chiralities, and the four-vector is one element of the material sector, not a pair of columns.

The operator is quadratic in its parameter and phase-blind. It loses the central phase and nothing else: the scale, the boost axis and the rotor are recoverable from the operator up to that phase. A physical statement that needs the phase cannot be read off the operator alone; a statement about the frame can.

The matrix pictures are representations, not the algebra's ontology. The algebra is the same in every picture; the matrices are what a basis makes of it. The choice of picture is a choice of what one wants to see, and the table above says what each picture shows.

## Summary

- One element has three element pictures — the four-vector, the $2\times2$ matrix and the $4\times4$ left regular matrix — and two operator pictures — the $2\times2$ congruence and the $4\times4$ sandwich.
- The element pictures are linear in the element; the operator pictures are quadratic, because the sandwich has two slots.
- The four coefficients carry one material and one informational coordinate each; the scalar coefficient carries the two times.
- The $2\times2$ matrix has trace $2Q_t$ and determinant $N$; it is the spinor picture and the smallest carrier of the state.
- The $4\times4$ left regular matrix has determinant $N^2$ and trace $4Q_t$; it is the spinor picture taken twice, with the two blocks the two column chiralities.
- Left multiplication preserves the column chiralities; right multiplication by a nilpotent moves between them, which is why the mass term is a right action.
- The sandwich is multiplicative in its parameter, $\operatorname{H}_{\tilde Q}\operatorname{H}_{\tilde U}=\operatorname{H}_{\tilde Q\tilde U}$, but quadratic and phase-blind; as an assignment it has kernel the central phase circle on the unit group.
- The $2\times2$ congruence preserves rank and scales the determinant by $|N|^2$ off the cone; on the cone it collapses to a rank-one line.
- The $4\times4$ operator has eigenvalues $\lambda_i\bar\lambda_j$, determinant $|N|^4$, trace $4|Q_t|^2$ and rank $(\operatorname{rank}\mathsf{M}_2)^2$.
- The four-vector operator returns the Euclidean square on the identity, not the interval; the positive weight and the spacetime length are different readings of the same element.
- The determinant's degree and the trace's factor are the bookkeeping in which the standard factor-of-two errors live.
- An element acts in three ways: left multiplication, right multiplication and the sandwich. The one-sided maps are linear and carry an element; the sandwich is quadratic and carries a frame.
- The one-sided composition laws are $L_{\tilde A}L_{\tilde B}=L_{\tilde A\tilde B}$ and $R_{\tilde A}R_{\tilde B}=R_{\tilde B\tilde A}$; the two families commute. The sandwich is multiplicative, $\operatorname{H}_{\tilde Q}\operatorname{H}_{\tilde U}=\operatorname{H}_{\tilde Q\tilde U}$, but not linear.
- The adjoint for the plain form swaps the sides and leaves the parameter alone; self-adjoint one-sided operators are the central multiplications. The orientation is in the commutator, not in the form.
- A two-sided operator is a pair defined up to a common central factor; it is invertible exactly when both parameters are units.
- The sandwich preserves the two sectors, is a congruence, and is self-adjoint for the Hermitian form exactly when a central-phase multiple of its parameter lies in $\mathbb{M}_+$ or $\mathbb{M}_-$. On the $*$-unitary slice it is an inner automorphism.
- The acting maps form a monoid; the reversible maps are the units off the cone, the states are the idempotents, and the cone is the boundary between them.
- The Peirce decomposition gives the four corners: populations on the diagonal, coherences off it.
- No picture is more fundamental than another; each is a choice of what to make visible, and the correspondence table is the translation between them.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the basis, with $\vec e_k^2=-e_t$ and $\vec e_x\vec e_y=\vec e_z$ |
| $Q_\mu$, $Q_t$, $\vec Q$ | the four complex coefficients, the scalar coefficient and the vector part |
| $N=\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2$ | the biquaternion norm, central and multiplicative |
| $\mathsf{M}_2(\tilde Q)$ | the $2\times2$ matrix, $\operatorname{Tr}=2Q_t$, $\det=N$ |
| $\mathsf{M}_4^{L}(\tilde Q)$ | the left regular matrix, $\operatorname{Tr}=4Q_t$, $\det=N^2$ |
| $\mathsf{M}_4^{R}(\tilde Q)$ | the right regular matrix |
| $\operatorname{H}_{\tilde Q}(X)=\tilde Q X\tilde Q^{*}$ | the sandwich, the two-sided operator |
| $L_{\tilde Q}(X)=\tilde Q X$, $R_{\tilde Q}(X)=X\tilde Q$ | the left and right multiplications |
| $T^{\approx}$ | the associate, the adjoint for $\langle X,Y\rangle=\operatorname{Sc}(XY)$ |
| $T^{\dagger}$ | the Hermitian adjoint, the adjoint for $\langle X,Y\rangle_{*}=\operatorname{Sc}(X^{*}Y)$ |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | the material and informational sectors |
| $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$ | the real quaternion and imaginary quaternion subspaces |
| $\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z)$ | the minimal idempotents and the two column chiralities |
| $\lambda_i$ | the eigenvalues of $\mathsf{M}_2(\tilde Q)$ |

## Further Reading

- [$M_2(\mathbb{C})$ Representation : The Matrix Product and the Algebra Structure](../articles_maths/m2c-representation-the-matrix-product-and-the-algebra-structure.html), for the isomorphism, the trace, the determinant and the ideals.
- [$M_4(\mathbb{C})_L$ Representation : The Matrix Product and the Algebra Structure](../articles_maths/m4c-representation-the-matrix-product-and-the-algebra-structure.html), for the regular matrix, its block form and the right matrix.
- [The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure](../articles_maths/the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.html), for the one-sided and two-sided maps, the congruence and the enveloping algebra.
- [One-Sided Operators on the Biquaternion Algebra](../articles_maths/one-sided-operators-on-the-biquaternion-algebra.html), for the kernels, the images and the one-sided types.
- [Two-Sided Operators on the Biquaternion Algebra](../articles_maths/two-sided-operators-on-the-biquaternion-algebra.html), for the pair structure and the type criteria.
- [Association and the Transpose on the Quaternion Algebra](../articles_maths/association-and-the-transpose-on-the-quaternion-algebra.html), for the adjoint that swaps the sides.
- [Two-Sided Operator and the Polar Decomposition of a N-Regular, Spectrally Regular Biquaternion](../articles_maths/two-sided-operator-and-the-polar-decomposition-of-a-n-regular-spectrally-regular-biquaternion.html), for the sandwich on the material sector, the four-vector image and the null cone.
- [Spin and the Three Elementary Carriers](spin-and-the-three-elementary-carriers.html), for the module and Hilbert structures, the second column and the mass coupling.
- [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html) and [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html), for the two sectors read at length.
