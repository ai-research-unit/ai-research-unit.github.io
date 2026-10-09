# __The 4×4 Regular Matrix Operator Representation of Biquaternions__

## Introduction

Physically this is the statement, already made in the element article, that the Lorentz transformation of a four-vector is a product of a left multiplication and a right multiplication in the algebra; what is added here is that the product is a matrix whose invariants are real and non-negative, so that the transformation the algebra performs is measured by two scalars.

The biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ is the four-dimensional complex algebra with basis $e_0 = 1, e_1, e_2, e_3$, where $e_k^2 = -e_0$ and $e_1e_2 = e_3$, with central scalar imaginary $i$, and with general element $\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu$. The left and right regular representations $\rho_L, \rho_R$ of $\mathbb{B}$ on itself, in the coefficient basis $e_0, e_1, e_2, e_3$, are those of *The 4×4 Regular Matrix Element Representation of Biquaternions*.

That article writes an element as an operator by *one* of its two multiplications, and finds the matrix of left multiplication, $\rho_L(\tilde{Q})(\tilde{R}) = \tilde{Q}\tilde{R}$, with $\det\rho_L(\tilde{Q}) = N(\tilde{Q})^{2}$ and $\operatorname{Tr}\rho_L(\tilde{Q}) = 4Q_0$. This article writes the Hermitian sandwich of *Biquaternion Rotations and Lorentz Transformations* in the same basis,

$$
\operatorname{H}_{\tilde{Q}}(\tilde S) = \tilde{Q}\,\tilde S\,\tilde{Q}^{*},
$$

and the first result is that the sandwich needs **both** multiplications at once: it is the left multiplication by $\tilde{Q}$ composed with the right multiplication by $\tilde{Q}^{*}$. The operator is therefore a product of two matrices already in the corpus, and everything about it — the closed form, the determinant, the trace, the spectrum, the rank — is read from that product.

The article owns the composition identity, the closed form of the operator matrix in the coefficient basis, the spectrum $\lambda_i\bar{\lambda}_j$ with the determinant $\lvert N(\tilde{Q})\rvert^{4}$ and the trace $4\lvert Q_0\rvert^{2}$ read off it, the real $8 \times 8$ form, and the separation of the two regimes at matrix level. The component computation of the same operator is *The Four-Vector Operator Representation of Biquaternions*; the congruence picture in the matrix algebra and the module side belong to other coordinate systems and are not repeated here. The spectral theory of the *element* matrix $\rho_L(\tilde{Q})$ — eigenvalues, Cayley–Hamilton, eigenspaces — is *Biquaternion Spectral Theory* and is not repeated here, although the operator's spectrum is stated below because it is a different matrix.

**Conventions.** The regular matrices in the basis $e_0, e_1, e_2, e_3$ are

$$
\rho_L(\tilde{Q}) = \begin{pmatrix}
Q_0 & -Q_1 & -Q_2 & -Q_3 \\
Q_1 & Q_0 & -Q_3 & Q_2 \\
Q_2 & Q_3 & Q_0 & -Q_1 \\
Q_3 & -Q_2 & Q_1 & Q_0
\end{pmatrix}, \qquad
\rho_R(\tilde{Q})(\tilde{R}) = \tilde{R}\tilde{Q},
$$

with $\rho_R(\tilde{Q}) = D\rho_L(\tilde{Q})^{\mathsf T}D$ and $D = \operatorname{diag}(-1,1,1,1)$. Indices are lowered here, as in the element article, and only the coefficient basis is used; the basis elements are the four coefficient directions of the four-vector article, so the four columns of the operator below are attached to $e_0$, the vector directions, and the composite directions.

## The Operator Is a Product of the Two Regular Matrices

**Theorem (composition identity).** For every $\tilde{Q}$,

$$
\operatorname{H}_{\tilde{Q}} = \rho_L(\tilde{Q}) \circ \rho_R(\tilde{Q}^{*}) = \rho_L(\tilde{Q})\,\rho_R(\tilde{Q}^{*}) ,
$$

the product of the left regular matrix of the operand and the right regular matrix of its Hermitian conjugate.

**Proof.** For every $\tilde S$, $\bigl(\rho_L(\tilde{Q}) \circ \rho_R(\tilde{Q}^{*})\bigr)(\tilde S) = \rho_L(\tilde{Q})\bigl(\tilde S\tilde{Q}^{*}\bigr) = \tilde{Q}\bigl(\tilde S\tilde{Q}^{*}\bigr) = \tilde{Q}\tilde S\tilde{Q}^{*} = \operatorname{H}_{\tilde{Q}}(\tilde S)$, the middle step being the definition of the two regular maps and the last the associativity of multiplication.

Two readings of the identity follow, and they explain the whole structure of the operator.

**The operator is a congruence, not a similarity.** If the two factors were $\tilde{Q}$ and $\tilde{Q}^{-1}$ the product would be the conjugation of the regular representation, of determinant $1$ and spectrum invariant under conjugation. With $\tilde{Q}^{*}$ in place of the inverse the product is a congruence: it preserves rank and it scales the determinant, and it preserves the spectrum only on the unitary slice, which is the slice of the rotations. This is the matrix-level reason for the failure of multiplicativity recorded in *Biquaternion Rotations and Lorentz Transformations*.

**The two multiplications commute, and the dagger is not the inverse.** Left and right multiplications by fixed elements commute, so the order of the two factors is immaterial and the operator is also the product $\rho_R(\tilde{Q}^{*})\rho_L(\tilde{Q})$. What matters is the pairing. The one-sided products $\rho_L(\tilde{Q})\rho_L(\tilde{Q}^{*})$, the operator $\tilde S \mapsto \tilde{Q}\tilde{Q}^{*}\tilde S$, and $\rho_R(\tilde{Q})\rho_R(\tilde{Q}^{*})$, the operator $\tilde S \mapsto \tilde S\tilde{Q}\tilde{Q}^{*}$, are different from the sandwich unless $\tilde{Q}\tilde{Q}^{*}$ is central, that is, unless the operand is a central multiple of a real quaternion. And with $\tilde{Q}^{-1}$ in place of $\tilde{Q}^{*}$ the product is the inner automorphism $\tilde S \mapsto \tilde{Q}\tilde S\tilde{Q}^{-1}$, of determinant one. The sandwich is the congruence-shaped pairing of a left multiplication with the right multiplication by the dagger, and that is what makes its invariants real.

**Lemma (the regular matrix respects the dagger).** For every $\tilde{Q}$,

$$
\rho_L(\tilde{Q}^{*}) = \rho_L(\tilde{Q})^{\dagger},
$$

the conjugate transpose of the regular matrix.

**Proof.** Both sides are conjugate-linear in $\tilde{Q}$, so it suffices to check the eight real basis elements. On $e_0$ both sides are $I$; on $ie_0$ both are $-iI$; on $e_k$ the left side is $-\rho_L(e_k)$, whose columns are the products $-e_ke_j$, and the right side is $\rho_L(e_k)^{\dagger} = \rho_L(e_k)^{\mathsf T} = -\rho_L(e_k)$, since left multiplication by a vector unit is skew-symmetric, as the products $e_ke_j$ read off the columns show; on $ie_k$ both sides are $i\rho_L(e_k)$, the transpose identity being applied once more.

**Corollary (closed form on the coefficient space).** Using $\rho_R(\tilde{Q}^{*}) = D\rho_L(\tilde{Q}^{*})^{\mathsf T}D$ and the lemma,

$$
\operatorname{H}_{\tilde{Q}} = \rho_L(\tilde{Q})\,D\,\rho_L(\tilde{Q})^{*}\,D ,
$$

the transpose of the lemma turning the dagger into the entrywise complex conjugate. Every entry of the matrix $\operatorname{H}_{\tilde{Q}}$ is a sesquilinear expression in the four coefficients of $\tilde{Q}$: linear in $Q_\mu$ and linear in $\overline{Q_\nu}$. The operator is therefore **quadratic in the operand** and **linear in the argument**, as the component computation of *The Four-Vector Operator Representation of Biquaternions* shows in the four-vector realization.

## The Determinant and the Trace

**Theorem (the spectrum of the operator).** Suppose $\Phi(\tilde{Q})$ is diagonalisable, with eigenvalues $\lambda_1, \lambda_2$. Then $\operatorname{H}_{\tilde{Q}}$ is diagonalisable and its four eigenvalues are

$$
\lambda_1\bar{\lambda}_1,\quad \lambda_1\bar{\lambda}_2,\quad \lambda_2\bar{\lambda}_1,\quad \lambda_2\bar{\lambda}_2 .
$$

Consequently

$$
\operatorname{Tr}\operatorname{H}_{\tilde{Q}} = 4\lvert Q_0\rvert^{2}, \qquad
\det\operatorname{H}_{\tilde{Q}} = \lvert N(\tilde{Q})\rvert^{4} .
$$

**Proof.** Let $\Phi(\tilde{Q}) = P\,\mathrm{diag}(\lambda_1,\lambda_2)\,P^{-1}$. On the matrix side the operator is $X \mapsto \Phi(\tilde{Q})X\Phi(\tilde{Q})^{\dagger}$, and in the transformed variable $Y = P^{-1}X(P^{-1})^{\dagger}$ it acts as $Y \mapsto \mathrm{diag}(\lambda_1,\lambda_2)\,Y\,\mathrm{diag}(\bar{\lambda}_1,\bar{\lambda}_2)$, which multiplies the matrix unit $E_{ij}$ by $\lambda_i\bar{\lambda}_j$. The four matrix units are therefore eigenvectors. For the trace, $\sum_{ij}\lambda_i\bar{\lambda}_j = \bigl(\textstyle\sum_i\lambda_i\bigr)\bigl(\textstyle\sum_j\bar{\lambda}_j\bigr) = \lvert\lambda_1+\lambda_2\rvert^{2} = \lvert\operatorname{Tr}\Phi(\tilde{Q})\rvert^{2} = \lvert 2Q_0\rvert^{2}$, and $\operatorname{Tr}\Phi(\tilde{Q}) = 2Q_0$ is the trace statement of *The 2×2 Matrix Element Representation of Biquaternions*. For the determinant, the four eigenvalues multiply to $\lvert\lambda_1\rvert^{2}\lvert\lambda_2\rvert^{2}\lvert\lambda_1\bar{\lambda}_2\rvert^{2}$, which simplifies to $\lvert\lambda_1\lambda_2\rvert^{4} = \lvert N(\tilde{Q})\rvert^{4}$; the identification $\lambda_1\lambda_2 = \det\Phi(\tilde{Q}) = N(\tilde{Q})$ is the determinant statement of the same article.

The two invariants are **real and non-negative for every operand**, and they are not the invariants of the element matrix: the element $\rho_L(\tilde{Q})$ has determinant $N(\tilde{Q})^{2}$, which is complex, and trace $4Q_0$, which is complex. The operator has thrown away the phase, exactly as the blindness to the phase of *Biquaternion Rotations and Lorentz Transformations* requires, and what remains is a modulus. The trace has a physical reading: it is four times the squared time coordinate of the operand, so the operator remembers the time component of the element that produces it and the squared modulus of everything else only through the determinant.

**Corollary (the operator is invertible exactly off the light cone).** $\operatorname{H}_{\tilde{Q}}$ is invertible if and only if $N(\tilde{Q}) \neq 0$, and $\lvert\det\operatorname{H}_{\tilde{Q}}\rvert^{1/4} = \lvert N(\tilde{Q})\rvert$.

**Theorem (the rank of the operator).** For every $\tilde{Q}$,

$$
\operatorname{rank}\operatorname{H}_{\tilde{Q}} = \bigl(\operatorname{rank}\Phi(\tilde{Q})\bigr)^{2},
$$

so that $\operatorname{rank}\operatorname{H}_{\tilde{Q}} = 4$ off the light cone, $1$ on it for $\tilde{Q} \neq 0$, and $0$ only at $\tilde{Q} = 0$.

**Proof.** Write the singular value decomposition $\Phi(\tilde{Q}) = P\Sigma V^{\dagger}$ with $P, V$ unitary and $\Sigma = \operatorname{diag}(\sigma_1,\sigma_2)$, $\sigma_j \geq 0$. In the matrix realization the operator is $X \mapsto \Phi(\tilde{Q})X\Phi(\tilde{Q})^{\dagger} = P\Sigma(V^{\dagger}XV)\Sigma P^{\dagger}$. As $X$ runs over $M_2(\mathbb{C})$ so does $V^{\dagger}XV$, and $\Sigma Y\Sigma$ has entries $\sigma_i\sigma_j Y_{ij}$, so the image is exactly the coordinate subspace spanned by the matrix units $E_{ij}$ with $\sigma_i\sigma_j \neq 0$, of complex dimension $(\#\{j : \sigma_j \neq 0\})^{2}$; conjugation by the fixed invertible $P$ does not change that dimension. The number of nonzero singular values is $\operatorname{rank}\Phi(\tilde{Q})$, which is $2$ off the cone, $1$ for a nonzero zero divisor, and $0$ only at $\tilde{Q} = 0$.

## The Case $N(\tilde{Q}) \neq 0$

Off the light cone the results above give a complete picture.

**Theorem (the invertible case).** Let $N(\tilde{Q}) \neq 0$. Then $\operatorname{rank}\operatorname{H}_{\tilde{Q}} = 4$, the operator lies in $GL(4,\mathbb{C})$, it preserves the rank of every argument, and in the coefficient basis it is a congruence by the invertible matrix $\rho_L(\tilde{Q})$. In the notation of the two regular maps,

$$
\operatorname{H}_{\tilde{Q}} \in \rho_L(\mathbb{B})\cdot\rho_R(\mathbb{B}) ,
$$

a product of one left and one right multiplication, both invertible.

**Proof.** The rank statement is the rank theorem above; the invertibility is $\det\operatorname{H}_{\tilde{Q}} = \lvert N(\tilde{Q})\rvert^{4} \neq 0$; the preservation of rank is the elementary fact that a congruence by an invertible matrix has the same rank as its argument, and the invertibility of each factor follows from $\det\rho_L(\tilde{Q}) = N(\tilde{Q})^{2} \neq 0$ and $\det\rho_R(\tilde{Q}^{*}) = N(\tilde{Q}^{*})^{2} = \overline{N(\tilde{Q})}^{2} \neq 0$.

**Example.** For $\tilde{Q} = e_0 + e_1$ one has $N = 2$ and

$$
\operatorname{H}_{\tilde{Q}} = \begin{pmatrix}
2 & 0 & 0 & 0 \\
0 & 2 & 0 & 0 \\
0 & 0 & 0 & -2 \\
0 & 0 & 2 & 0
\end{pmatrix},
\qquad \operatorname{Tr} = 4 = 4\lvert 1\rvert^{2}, \qquad \det = 16 = \lvert 2\rvert^{4} = N^{4}.
$$

The trace and the determinant are real, in agreement with the theorem; the matrix itself is not Hermitian, and its eigenvalues are $\{2, 2, 2i, -2i\}$, which are the four general products $\lambda_i\bar{\lambda}_j$ of the eigenvalues $\lambda = 1 \pm i$ of $\Phi(e_0+e_1)$: $(1+i)(1-i) = 2$ twice, and $(1\pm i)^2 = \pm 2i$.

**Example (a physical boost).** For the rotor $\tilde{Q} = \tfrac53e_0 + \tfrac43ie_3$ of *Biquaternion Rotations and Lorentz Transformations*, of norm one and of rapidity $\psi = 2\ln 3$, the matrix is $\Phi(\tilde{Q}) = \mathrm{diag}(3,\tfrac13)$, so the operator has the four eigenvalues $9, 1, 1, \tfrac19$, of determinant $1 = \lvert N\rvert^{4}$ and trace $\tfrac{100}{9} = 4(\tfrac53)^{2}$; the eigenvalue $9 = e^{\psi}$ is the doubled rapidity, the operand having stored $3 = e^{\psi/2}$.

**The operator group.** Restricted to the unit-norm slice, the set of operators is the image of $SL(2,\mathbb{C})$ and is the Lorentz group with kernel $\{\pm e_0\}$; over all units it is the set of dilated Lorentz transformations $\mathbb{R}_{>0} \times SO^{+}(1,3)$, and it has lost the phase circle. The geometric statement, the action on the six subspaces and the orbits are *Biquaternion Rotations and Lorentz Transformations* and *The Sandwich Action in Subspaces*.

## The Case $N(\tilde{Q}) = 0$

On the light cone the two factors of the product are singular, and the operator collapses.

**Theorem (the singular case).** Let $N(\tilde{Q}) = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = 0$ and $\tilde{Q} \neq 0$. Then $\operatorname{rank}\operatorname{H}_{\tilde{Q}} = 1$, and

$$
\operatorname{H}_{\tilde{Q}} \circ \operatorname{H}_{\tilde{Q}} = 4\lvert Q_0\rvert^{2}\,\operatorname{H}_{\tilde{Q}} .
$$

The image is the single complex line spanned by the Hermitian element $\tilde{Q}\tilde{Q}^{*}$, and its generator, normalised, is a minimal idempotent of $\mathbb{B}$. If $Q_0 = 0$ the operator is nilpotent, $\operatorname{H}_{\tilde{Q}}\circ\operatorname{H}_{\tilde{Q}} = 0$, so all four eigenvalues vanish; if $Q_0 \neq 0$ the operator has the single nonzero eigenvalue $4\lvert Q_0\rvert^{2}$ and is a scaled projection.

**Proof.** The rank is the rank theorem above; for the square, a rank-one endomorphism satisfies $T^{2} = (\operatorname{Tr}T)\,T$ and $\operatorname{Tr}\operatorname{H}_{\tilde{Q}} = 4\lvert Q_0\rvert^{2}$, so $\operatorname{H}_{\tilde{Q}}\circ\operatorname{H}_{\tilde{Q}} = 4\lvert Q_0\rvert^{2}\operatorname{H}_{\tilde{Q}}$. For the eigenvalues: with $\operatorname{rank}\operatorname{H}_{\tilde{Q}} = 1$ the operator is, after a change of basis, a single nonzero entry, hence its eigenvalues are $4\lvert Q_0\rvert^{2}$ once and $0$ three times, the trace being additive. When $Q_0 = 0$ the trace vanishes and one eigenvalue of a rank-one operator is zero, so the operator is nilpotent.

**Example (nilpotent).** For $\tilde{Q} = e_1 + ie_2$, a null operand with $Q_0 = 0$,

$$
\operatorname{H}_{\tilde{Q}} = \begin{pmatrix}
2 & 0 & 0 & 2i \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
2i & 0 & 0 & -2
\end{pmatrix}, \qquad \operatorname{rank} = 1, \qquad \operatorname{Tr} = 0, \qquad \det = 0 .
$$

The two middle columns vanish and the first and fourth are $\pm 2(e_0 + ie_3)$: the image is the line $\mathbb{C}\tilde\Pi_1$ with $\tilde\Pi_1 = \tfrac12(e_0+ie_3)$, and the matrix squares to zero. The four eigenvalues are all zero although the rank is one, which is the sharp statement that a null operator is not diagonalisable: the collapse is not a change of eigenvalue but a loss of rank.

**Example (projection).** For $\tilde{Q} = \tfrac12(e_0 - ie_3) = \tilde\Pi_2$, a null operand with $Q_0 = \tfrac12$,

$$
\operatorname{H}_{\tilde{Q}} = \begin{pmatrix}
\tfrac12 & 0 & 0 & \tfrac{i}{2} \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
-\tfrac{i}{2} & 0 & 0 & \tfrac12
\end{pmatrix}, \qquad \operatorname{rank} = 1, \qquad \operatorname{Tr} = 1, \qquad \det = 0 .
$$

The first column is $\tilde\Pi_2$ and the fourth is $i\tilde\Pi_2$; the single nonzero eigenvalue of the operator is $1 = 4\lvert\tfrac12\rvert^{2}$, so the operator is exactly the projection onto its own image line.

The contrast between the two examples is the whole content of the two regimes at matrix level: both operators have rank one and determinant zero, both send the whole coefficient space onto one line, and they are separated by the single real number $\operatorname{Tr}\operatorname{H}_{\tilde{Q}} = 4\lvert Q_0\rvert^{2}$, which vanishes exactly when the collapse is nilpotent. In the invertible case the determinant is $\lvert N(\tilde{Q})\rvert^{4} \neq 0$ and no collapse occurs at all.

Physically, off the light cone the operand is a legitimate frame change and the operator is invertible; on the light cone the operand is a null direction and its operator is singular, able to create nothing but a single lightlike Hermitian line, so a null element generates no motion. This is the operator form of the identification of the light cone with the zero-divisor locus of the algebra, whose causal use is *Biquaternion Rotations and Lorentz Transformations*.

**Reading (rank is mass, the determinant is the interval).** The matrix $\Phi(\tilde{Q})$ carries two numbers that read as two physical data: its **rank**, which is two for an invertible operand and one for a null one, and its **determinant**, which is the biquaternion norm, $\det\Phi(\tilde{Q}) = N(\tilde{Q})$. Read physically, the rank is the **mass**: rank two is the massive case and rank one the massless case, and the mass shell is the vanishing of the determinant, so that an operand is massless exactly when its matrix loses a dimension. The interval is the **determinantal modulus**, $\lvert\det\Phi(\tilde{Q})\rvert = \lvert N(\tilde{Q})\rvert$, and the determinant of the operator itself is $\lvert N(\tilde{Q})\rvert^{4}$, the fourth power of that modulus. The reading is the matrix form of "mass is $\lvert N\rvert$", and its boundary is that the algebra supplies the rank and the determinant and no mass value: it fixes which operands are massive and which are not, and not the spectrum.

## The Real $8 \times 8$ Form

Regarded over $\mathbb{R}$ in the basis $e_0, e_1, e_2, e_3, ie_0, ie_1, ie_2, ie_3$, the operator is real-linear and is an $8 \times 8$ real matrix; the element article performs the same realification for $\rho_L$. The eight coordinates are the eight real parameters of the framework, so in this form the operator is the transformation of the material and informational four-vectors written as one real linear map.

**Proposition (the realified operator).** The realification of $\operatorname{H}_{\tilde{Q}}$ satisfies

$$
\det_{\mathbb{R}}\bigl(\operatorname{H}_{\tilde{Q}}\bigr) = \lvert N(\tilde{Q})\rvert^{8}, \qquad
\operatorname{Tr}_{\mathbb{R}}\bigl(\operatorname{H}_{\tilde{Q}}\bigr) = 8\lvert Q_0\rvert^{2} .
$$

**Proof.** Realification replaces each complex eigenvalue $\lambda$ of a complex-linear endomorphism by the pair $\lambda, \bar{\lambda}$; the four eigenvalues $\lambda_i\bar{\lambda}_j$ have modulus $\lvert\lambda_i\rvert\lvert\lambda_j\rvert$, each of which is already real, so the eigenvalues occur in conjugate pairs of equal modulus and the real determinant is the square of the complex one, $\lvert N(\tilde{Q})\rvert^{8}$. The real trace is twice the real part of the complex trace, and $\operatorname{Tr}\operatorname{H}_{\tilde{Q}} = 4\lvert Q_0\rvert^{2}$ is real, hence $8\lvert Q_0\rvert^{2}$.

The dimension doubles for the same reason as in the element article: $\mathbb{B}$ is a complex space regarded as a real one by restriction of scalars, and each complex coordinate becomes two real ones. The doubling changes the exponents — $4 \to 8$ on the determinant, the factor $2$ on the trace — and nothing else.

## Physical Readings

The operator reads as a process written as a product of two regular maps, and the reading is that a change of frame is a composition and not an element: the sandwich is the left multiplication by the operand composed with the right multiplication by its adjoint. Read on the monoid, units are reversible processes and zero divisors are the irreversible ones, so this representation is where the direction of a process becomes visible as a failure of invertibility. Read on the two ledgers, the two factors are the two actions, which is the matrix form of the statement that a frame change touches both sectors at once.

## Summary

The sandwich of an element is a product of the two regular maps: $\operatorname{H}_{\tilde{Q}} = \rho_L(\tilde{Q}) \circ \rho_R(\tilde{Q}^{*})$, the left multiplication by the operand composed with the right multiplication by its Hermitian conjugate, which in the coefficient basis is the matrix $\rho_L(\tilde{Q})\,D\,\rho_L(\tilde{Q})^{*}\,D$ with $D = \operatorname{diag}(-1,1,1,1)$. Every entry is sesquilinear in the coefficients, so the operator is quadratic in the operand and linear in the argument. It is a congruence and not a similarity, which is the matrix-level reason it is not multiplicative, and physically it is the product of the two chiral multiplications by which the corpus writes a Lorentz transformation.

Its invariants are real and non-negative in every case. When $\Phi(\tilde{Q})$ is diagonalisable with eigenvalues $\lambda_1, \lambda_2$, the operator is diagonalisable with eigenvalues the four general products $\lambda_i\bar{\lambda}_j$; hence $\operatorname{Tr}\operatorname{H}_{\tilde{Q}} = \lvert\lambda_1+\lambda_2\rvert^{2} = 4\lvert Q_0\rvert^{2}$ and $\det\operatorname{H}_{\tilde{Q}} = \lvert\lambda_1\lambda_2\rvert^{4} = \lvert N(\tilde{Q})\rvert^{4}$. Over $\mathbb{R}$ the operator is $8 \times 8$ with determinant $\lvert N(\tilde{Q})\rvert^{8}$ and trace $8\lvert Q_0\rvert^{2}$. For the boost rotor $\tfrac53e_0 + \tfrac43ie_3$ the four eigenvalues are $9, 1, 1, \tfrac19$, and the eigenvalue $9$ is the doubled rapidity of the motion.

The two regimes are separated by the vanishing of those invariants. Off the light cone the determinant is nonzero, the operator lies in $GL(4,\mathbb{C})$, it is the product of two invertible regular matrices, and it preserves rank; on the unit-norm slice it is the Lorentz group. On the cone the operator has rank one, its image is the line of the Hermitian element $\tilde{Q}\tilde{Q}^{*}$, whose normalisation is a minimal idempotent, and it satisfies $\operatorname{H}_{\tilde{Q}}\circ\operatorname{H}_{\tilde{Q}} = 4\lvert Q_0\rvert^{2}\operatorname{H}_{\tilde{Q}}$. The single number $\operatorname{Tr}\operatorname{H}_{\tilde{Q}} = 4\lvert Q_0\rvert^{2}$ then separates the two faces of the collapse: it vanishes for $\tilde{Q} = e_1+ie_2$, where all four eigenvalues are zero and the operator is nilpotent, and equals $1$ for $\tilde{Q} = \tfrac12(e_0-ie_3)$, where the operator is the projection onto the idempotent that generates its image.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\rho_L(\tilde{Q}), \rho_R(\tilde{Q})$ | left and right regular matrices in the basis $e_0,e_1,e_2,e_3$ |
| $D = \operatorname{diag}(-1,1,1,1)$ | fixed sign matrix, $\rho_R(\tilde{Q}) = D\rho_L(\tilde{Q})^{\mathsf T}D$ |
| $\rho_L(\tilde{Q}^{*}) = \rho_L(\tilde{Q})^{\dagger}$ | the regular matrix respects the dagger |
| $\operatorname{H}_{\tilde{Q}}(\tilde S) = \tilde{Q}\tilde S\tilde{Q}^{*}$ | the Hermitian sandwich, the operator of the operand |
| $\operatorname{H}_{\tilde{Q}} = \rho_L(\tilde{Q})\rho_R(\tilde{Q}^{*})$ | the operator as a product of the two regular maps |
| $\operatorname{H}_{\tilde{Q}} = \rho_L(\tilde{Q})D\rho_L(\tilde{Q})^{*}D$ | closed form in the coefficient basis |
| $\lambda_1,\lambda_2$ | eigenvalues of $\Phi(\tilde{Q})$ |
| $\lambda_i\bar{\lambda}_j$ | eigenvalues of $\operatorname{H}_{\tilde{Q}}$ when $\Phi(\tilde{Q})$ is diagonalisable |
| $\operatorname{Tr}\operatorname{H}_{\tilde{Q}} = 4\lvert Q_0\rvert^{2} = \lvert\operatorname{Tr}\Phi(\tilde{Q})\rvert^{2}$ | trace of the operator, always real |
| $\det\operatorname{H}_{\tilde{Q}} = \lvert N(\tilde{Q})\rvert^{4}$ | determinant of the operator; nonzero exactly off the cone |
| $\operatorname{rank}\operatorname{H}_{\tilde{Q}} = 4$ or $1$ | off the light cone, and on it |
| $\operatorname{H}_{\tilde{Q}}\circ\operatorname{H}_{\tilde{Q}} = 4\lvert Q_0\rvert^{2}\operatorname{H}_{\tilde{Q}}$, $N = 0$ | nilpotent if $Q_0 = 0$, projection up to scale otherwise |
| $\det_{\mathbb{R}} = \lvert N\rvert^{8}$, $\operatorname{Tr}_{\mathbb{R}} = 8\lvert Q_0\rvert^{2}$ | the real $8\times8$ form |
| $\langle\tilde{P},\tilde{Q}\rangle_{\natural}$ | the general quaternionic bilinear form, $\mathrm{Sc}(\tilde{P}^{\natural}\tilde{Q})$; on the diagonal $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=N(\tilde{Q})$ |
| $\langle\tilde{P},\tilde{Q}\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{P}\tilde{Q}^{*})$; on the diagonal $\langle\tilde{Q},\tilde{Q}\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}$ |
| $\langle\tilde{P},\tilde{Q}\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{P}\tilde{Q})$ |

## Further Reading

- Charles W. Curtis and Irving Reiner, *Representation Theory of Finite Groups and Associative Algebras* (Interscience, 1962), for the left and right regular representations and their relation.
- I. Martin Isaacs, *Algebra: A Graduate Course* (Brooks/Cole, 1994), for the regular module, the opposite algebra, and congruences in matrix algebras.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2nd ed. 2013), for congruence, rank preservation, realification, and the eigenvalue products of $X \mapsto MXM^{\dagger}$.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the sandwich written with the two-sided multiplication of a rotor.
