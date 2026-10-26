# __The Element and Operator Representations__

## Introduction

One biquaternion can be written in five standard matrix-shaped ways, and the five divide into two kinds. The **element representations** answer what the element is: the four-vector of complex coefficients, the $2\times2$ complex matrix $\mathsf{M}_2(\tilde Q)$, and the $4\times4$ left regular matrix $\mathsf{M}_4^{L}(\tilde Q)$. The **operator representations** answer what the element does: the $2\times2$ congruence $X\mapsto \mathsf{M}_2(\tilde Q)X\mathsf{M}_2(\tilde Q)^{\dagger}$ and the $4\times4$ sandwich. The first kind is linear in the element; the second is quadratic. That difference is the whole content of the article.

The physical stake is a distinction that is easy to lose. A state is carried by an element representation, a transformation by an operator representation. A spinor is a two-component column on which the $2\times2$ matrix acts; a four-vector is an element of the material sector on which the sandwich acts. Reading the determinant of the regular matrix as the norm, or the sandwich as a linear map of its parameter, or the doubled regular picture as two particles, are the three standard errors that the distinction prevents.

The article is a reader and owns no new theorem. Each result is stated in a sentence, the mathematics article that proves it is linked, and the physical reading is given with its boundary. It is the entry of the *Element and Operator Representations* group that fixes the vocabulary the other representation articles use.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The coefficient space and the norm | [The Biquaternion Algebra and Its Vector Spaces](../articles_maths/the-biquaternion-algebra-and-its-vector-spaces.html) |
| The algebra isomorphism $\mathsf{M}_2$, the trace, the determinant, the sectors and the ideals | [$M_2(\mathbb{C})$ Representation : The Matrix Product and the Algebra Structure](../articles_maths/m2c-representation-the-matrix-product-and-the-algebra-structure.html) |
| The left regular matrix, its determinant $N^2$, its trace $4Q_t$ and its block decomposition | [Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions](../articles_maths/introduction-to-the-4x4-matrix-element-representation-of-biquaternions.html) |
| The right regular matrix and its relation to the left one | [Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions](../articles_maths/introduction-to-the-4x4-matrix-element-representation-of-biquaternions.html) |
| The congruence, the two-sided maps and the enveloping operator algebra | [The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure](../articles_maths/the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.html) |
| The sandwich, its spectrum, determinant, trace and rank | [Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions](../articles_maths/introduction-to-the-4x4-matrix-element-representation-of-biquaternions.html), §*The Sandwich in the Regular Basis*, for the matrix, the determinant and the trace; [Two-Sided Operator and the Polar Decomposition](../articles_maths/two-sided-operator-and-the-polar-decomposition.html), §*The Spectrum of the Sandwich*, for the spectrum, and §*The Vanishing of the Modulus*, for the rank |
| The module structure and the Hilbert structure of the spinor space | [Modules over the Biquaternion Algebra](../articles_maths/modules-over-the-biquaternion-algebra.html) |
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

The congruence is a completely positive map with a single Kraus operator. It is trace-preserving exactly when $M$ is unitary, that is for the unitary elements; otherwise it rescales the trace. On the cone it is a destructive map: it projects every operand onto one line and erases the distinctions between them. The algebra supplies the shape of a quantum channel and of a measurement; it does not supply the probability rule for the outcomes.

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

## Physical Readings

**The spinor and the regular picture.** The $2\times2$ picture is the spinor picture: a biquaternion acts on a two-component column. The $4\times4$ picture is that same action written on the algebra itself, and it is the spinor picture taken twice. The two blocks are the two column chiralities, not two particles; the doubling is the dimension of the module, not a doubling of the physical state space. The column chirality is not the module chirality: the two ideals are isomorphic, while the module chiral halves are $S$ and its conjugate module $\bar S$, which are inequivalent as complex modules and isomorphic only as real representations. *The Complementary Ideal and the Second State Space* states the same warning.

**The double cover.** The norm-one group is $\mathrm{SL}(2,\mathbb{C})=\mathrm{Spin}(1,3)$, and it covers the proper orthochronous Lorentz group two-to-one with kernel $\{\pm \mathrm{I}_2\}$. A rotation through $2\pi$ gives $-\mathrm{I}_2$ and a rotation through $4\pi$ gives $\mathrm{I}_2$. The sign is the sign of the spinor, and it is the discrete difference between the spinor picture and the four-vector picture.

**The mass coupling.** Left multiplication preserves each column chirality, so a mass term that couples the two column chiralities cannot be a left multiplication. It is a right multiplication by a nilpotent element, which maps one minimal left ideal onto the other and annihilates the second. In the $4\times4$ picture this is the off-diagonal block that the left regular matrix does not have; in the $2\times2$ picture it is the right action that the column picture does not show.

**The central phase.** A central phase is a scalar matrix. It multiplies the element matrix, it multiplies the determinant by $\lambda^2$, and it disappears from the sandwich. The element picture sees the phase; the operator picture does not. This is why the polar word carries the phase and the sandwich does not.

**The degree of the determinant.** The $2\times2$ determinant is $N$, the $4\times4$ determinant is $N^2$, and the operator determinant is $|N|^4$. Only the zero sets agree. A computation that reads a determinant must say which picture it is in.

**The trace factor.** The trace of the $2\times2$ matrix is $2Q_t$, the trace of the regular matrix is $4Q_t$, and the trace of the operator is $4|Q_t|^2$. The factor two is the number of column chiralities; the factor four is the dimension of the regular module or the number of matrix units. The factors are bookkeeping, not physics, but they are the bookkeeping in which the factor-of-two errors of the corpus live.

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
| $\mathbb{M}_-$, $\mathbb{M}_+$ | the material and informational sectors |
| $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$ | the real quaternion and imaginary quaternion subspaces |
| $\tilde\Pi_\pm=\tfrac12(e_t\pm i\vec e_z)$ | the minimal idempotents and the two column chiralities |
| $\lambda_i$ | the eigenvalues of $\mathsf{M}_2(\tilde Q)$ |

## Further Reading

- [$M_2(\mathbb{C})$ Representation : The Matrix Product and the Algebra Structure](../articles_maths/m2c-representation-the-matrix-product-and-the-algebra-structure.html), for the isomorphism, the trace, the determinant and the ideals.
- [Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions](../articles_maths/introduction-to-the-4x4-matrix-element-representation-of-biquaternions.html), for the regular matrix, its block form and the right matrix.
- [The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure](../articles_maths/the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.html), for the one-sided and two-sided maps, the congruence and the enveloping algebra.
- [Two-Sided Operator and the Polar Decomposition](../articles_maths/two-sided-operator-and-the-polar-decomposition.html), for the sandwich on the material sector, the four-vector image and the null cone.
- [The Spinor Module and Its Two Structures](the-spinor-module-and-its-two-structures.html), for the module and Hilbert structures that the $2\times2$ picture carries.
- [The Complementary Ideal and the Second State Space](the-complementary-ideal-and-the-second-state-space.html), for the second column and the mass coupling.
- [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html) and [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html), for the two sectors read at length.
