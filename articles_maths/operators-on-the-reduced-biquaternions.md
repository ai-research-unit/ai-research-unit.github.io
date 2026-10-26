# __Operators on the Reduced Biquaternions__

## Introduction

Each of the four general products of the reduced biquaternion algebra has a **left multiplication operator**, $L^{\circ}_{\breve Q}:\breve Q_{2}\mapsto \breve Q\circ \breve Q_{2}$, and the four operators are collected here and compared. Two of them are complex-linear, those of the two bilinear products; two are conjugate-linear, those of the two sesquilinear products. On the complex basis $1,j$ each is a $2\times2$ matrix, and in the idempotent basis each becomes diagonal or off-diagonal of a simple shape, which makes the trace, the determinant, the eigenvalues and the invertibility visible at once. The multiplication of the algebra is **commutative**, so the left and the right multiplication operators of the plain product coincide; the algebra **has zero divisors**, so an operator may be singular at a non-zero element; and it is **not a division algebra**, so no operator calculus makes it one. The plain operator alone, with its matrix, trace, determinant and adjoints, is *The Multiplication Operators of the Algebra of the Reduced Biquaternions*; this article is the collection and the comparison of the four.

## The Four Left Multiplication Operators

**Definition.** For a product $\circ$ and an element $\breve Q$, the **left multiplication** is the map
$$
L^{\circ}_{\breve Q}:\breve Q_{2}\mapsto \breve Q\circ \breve Q_{2} ,
$$
with the superscript dropped for the plain product, $L_{\breve Q}(\breve Q_{2})=\breve Q \breve Q_{2}$.

### The Matrices on the Complex Basis

**Theorem (the four matrices).** On the complex basis $1,j$, acting on the column $\binom{Q_{2\blacktriangle}}{Q_{2\blacktriangledown}}$ of $\breve Q_{2}=Q_{2\blacktriangle}+jQ_{2\blacktriangledown}$, the four left multiplications are
$$
L_{\breve Q}=\begin{pmatrix}Q_{\blacktriangle}&Q_{\blacktriangledown}\\ Q_{\blacktriangledown}&Q_{\blacktriangle}\end{pmatrix},\qquad
L_{\mathrm{ts},\breve Q}=\begin{pmatrix}Q_{\blacktriangle}&-Q_{\blacktriangledown}\\ -Q_{\blacktriangledown}&Q_{\blacktriangle}\end{pmatrix},
$$
$$
L^{*}_{\breve Q}=\begin{pmatrix}Q_{\blacktriangle}&-Q_{\blacktriangledown}\\ Q_{\blacktriangledown}&-Q_{\blacktriangle}\end{pmatrix}\circ\kappa,\qquad
L_{\mathrm{ts}*,\breve Q}=\begin{pmatrix}Q_{\blacktriangle}&Q_{\blacktriangledown}\\ -Q_{\blacktriangledown}&-Q_{\blacktriangle}\end{pmatrix}\circ\kappa ,
$$
where $\kappa$ is the coefficient conjugation $\kappa\binom{Q_{2\blacktriangle}}{Q_{2\blacktriangledown}}=\binom{\bar Q_{2\blacktriangle}}{\bar Q_{2\blacktriangledown}}$ and $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$.

*Proof.* Read the four coordinate tables. The plain product $\breve Q \breve Q_{2}=(Q_{\blacktriangle}Q_{2\blacktriangle}+Q_{\blacktriangledown}Q_{2\blacktriangledown})+(Q_{\blacktriangle}Q_{2\blacktriangledown}+Q_{\blacktriangledown}Q_{2\blacktriangle})j$ has the columns $\binom{Q_{\blacktriangle}}{Q_{\blacktriangledown}}$ and $\binom{Q_{\blacktriangledown}}{Q_{\blacktriangle}}$, giving the first matrix. The tessarine bilinear product $\breve Q_{\mathrm{ts}}\breve Q_{2}=(Q_{\blacktriangle}Q_{2\blacktriangle}-Q_{\blacktriangledown}Q_{2\blacktriangledown})+(Q_{\blacktriangle}Q_{2\blacktriangledown}-Q_{\blacktriangledown}Q_{2\blacktriangle})j$ has the columns $\binom{Q_{\blacktriangle}}{-Q_{\blacktriangledown}}$ and $\binom{-Q_{\blacktriangledown}}{Q_{\blacktriangle}}$, giving the second. For the two sesquilinear products, $\breve Q_{2}^{*}=\binom{\bar Q_{2\blacktriangle}}{-\bar Q_{2\blacktriangledown}}=\sigma_{3}\kappa\binom{Q_{2\blacktriangle}}{Q_{2\blacktriangledown}}$ with $\sigma_{3}=\operatorname{diag}(1,-1)$, so $L^{*}_{\breve Q}=L_{\breve Q}\sigma_{3}\kappa$ and $L_{\mathrm{ts}*,\breve Q}=L_{\mathrm{ts},\breve Q}\sigma_{3}\kappa$; multiplying the two bilinear matrices into $\sigma_{3}$ gives the last two displays.

**Corollary (linear against conjugate-linear).** The operators $L_{\breve Q}$ and $L_{\mathrm{ts},\breve Q}$ of the bilinear products are **complex-linear**; the operators $L^{*}_{\breve Q}$ and $L_{\mathrm{ts}*,\breve Q}$ of the sesquilinear products are **conjugate-linear**, and are real-linear but not complex-linear.

*Proof.* The bilinear matrices have constant complex entries and act by matrix multiplication, hence are complex-linear; the two sesquilinear operators carry the map $\kappa$, which is conjugate-linear, so they are conjugate-linear.

### The Matrices on the Idempotent Basis

**Theorem (the idempotent form).** In the idempotent basis, acting on the column $\binom{Q_{2+}}{Q_{2-}}$ of $\breve Q_{2}=Q_{2+}\Pi_++Q_{2-}\Pi_-$, the four operators are
$$
\boxed{\;
L_{\breve Q}=\operatorname{diag}(Q_{+},Q_{-}),\qquad
L_{\mathrm{ts},\breve Q}=\operatorname{diag}(Q_{-},Q_{+})
\;},
$$
$$
L^{*}_{\breve Q}=\begin{pmatrix}0&Q_{+}\\ Q_{-}&0\end{pmatrix}\circ\kappa,\qquad
L_{\mathrm{ts}*,\breve Q}=\begin{pmatrix}0&Q_{-}\\ Q_{+}&0\end{pmatrix}\circ\kappa .
$$

*Proof.* In the idempotent coordinates the product is componentwise, $\breve Q \breve Q_{2}=Q_{+}\,Q_{2+}\,\Pi_++Q_{-}\,Q_{2-}\,\Pi_-=L_{\breve Q}(Q_{2+},Q_{2-})=(Q_{+}Q_{2+},Q_{-}Q_{2-})$, which is $\operatorname{diag}(Q_{+},Q_{-})$; and $\breve Q_{\mathrm{ts}}=Q_{-}\Pi_++Q_{+}\Pi_-$, so $\breve Q_{\mathrm{ts}}\breve Q_{2}=(Q_{-} Q_{2+})\Pi_++(Q_{+} Q_{2-})\Pi_-$. For the sesquilinear products, $\breve Q_{2}^{*}=\bar Q_{2-}\Pi_++\bar Q_{2+}\Pi_-$ because the star exchanges the two idempotents, so $\breve Q \breve Q_{2}^{*}=Q_{+}\bar Q_{2-}\Pi_++Q_{-}\bar Q_{2+}\Pi_-$ and $\breve Q_{\mathrm{ts}}\breve Q_{2}^{*}=Q_{-}\bar Q_{2-}\Pi_++Q_{+}\bar Q_{2+}\Pi_-$, which are the two off-diagonal displays.

**Corollary (the plain product is diagonal).** The plain operator is diagonal in the idempotent basis, with the two idempotent coordinates on the diagonal; the tessarine bilinear operator is the same diagonal with the two entries **exchanged**, and the two sesquilinear operators are the two **off-diagonal** matrices with the conjugation. The four operators differ only in the placement of $Q_{+}$ and $Q_{-}$.

*Proof.* Read the four displays: the plain operator has $Q_{+}$ first and $Q_{-}$ second, the tessarine bilinear operator the reverse, and the two sesquilinear operators have zeros on the diagonal and carry $Q_{+},Q_{-}$ on the two off-diagonal entries.

## The Right Multiplication Operators

**The right multiplication operators coincide with the left ones for the plain product and differ for the other three.**

**Theorem.** For the plain product the right multiplication $R_{\breve Q}:\breve Q_{2}\mapsto \breve Q_{2}\breve Q$ equals the left one, $R_{\breve Q}=L_{\breve Q}$, because the multiplication is commutative. For the other three products the right operator is $R^{\circ}_{\breve Q}(\breve Q_{2})=\breve Q_{2}\circ \breve Q$, and in the idempotent coordinates it is the left operator with the involution moved from $\breve Q$ in the left slot to $\breve Q_{2}$ in the right slot: writing $\breve Q=(Q_{+},Q_{-})$ and $\breve Q_{2}=(Q_{2+},Q_{2-})$,
$$
R_{\mathrm{ts},\breve Q}=\begin{pmatrix}0&Q_{+}\\ Q_{-}&0\end{pmatrix},\qquad
R^{*}_{\breve Q}=\operatorname{diag}(\bar Q_{-},\bar Q_{+}),\qquad
R_{\mathrm{ts}*,\breve Q}=\begin{pmatrix}0&\bar Q_{-}\\ \bar Q_{+}&0\end{pmatrix}.
$$

*Proof.* Commutativity gives $\breve Q_{2}\breve Q=\breve Q \breve Q_{2}$, hence $R_{\breve Q}=L_{\breve Q}$. For the other three, evaluate $\breve Q_{2}\circ \breve Q$ in the idempotent coordinates: the tessarine sign sends $\breve Q_{2}=(Q_{2+},Q_{2-})$ to $(Q_{2-},Q_{2+})$, so $R_{\mathrm{ts},\breve Q}(Q_{2+},Q_{2-})=(Q_{2-},Q_{2+})\cdot(Q_{+},Q_{-})=(Q_{+}Q_{2-},Q_{-}Q_{2+})$; the star sends $\breve Q=(Q_{+},Q_{-})$ to $(\bar Q_{-},\bar Q_{+})$, so $R^{*}_{\breve Q}(Q_{2+},Q_{2-})=(Q_{2+},Q_{2-})\cdot(\bar Q_{-},\bar Q_{+})=(Q_{2+}\bar Q_{-},Q_{2-}\bar Q_{+})$; and combining the two, $R_{\mathrm{ts}*,\breve Q}(Q_{2+},Q_{2-})=(Q_{2-}\bar Q_{-},Q_{2+}\bar Q_{+})$. These are the three displays, and they differ from the left operators $L_{\mathrm{ts},\breve Q}=\operatorname{diag}(Q_{-},Q_{+})$, $L^{*}_{\breve Q}=\left(\begin{smallmatrix}0&Q_{+}\\ Q_{-}&0\end{smallmatrix}\right)\circ\kappa$ and $L_{\mathrm{ts}*,\breve Q}=\left(\begin{smallmatrix}0&Q_{-}\\ Q_{+}&0\end{smallmatrix}\right)\circ\kappa$.

**Corollary (the commutant).** The operators commuting with all the left multiplications of the plain product are the right multiplications, which are the left multiplications themselves; so the commutant of the image is the image, and the operator algebra $\{L_{\breve Q}\}$ is a maximal commutative subalgebra of $\operatorname{End}_{\mathbb{C}}(\mathbb{B}_{\mathrm{r}})$ of complex dimension two.

*Proof.* An operator commuting with every $L_{\breve Q}$ commutes in particular with $L_{j}=\operatorname{diag}(1,-1)$, hence is diagonal in the idempotent basis, hence is in the image; and the image is commutative by the commutativity of the algebra.

## Trace, Determinant and Eigenvalues

**The two bilinear operators share the trace $2Q_{\blacktriangle}$, the determinant $\langle \breve Q\rangle_{\mathrm{ts}}$ and the eigenvalues $Q_{+},Q_{-}$; the two sesquilinear operators are conjugate-linear with real determinant $\lvert\langle \breve Q\rangle_{\mathrm{ts}}\rvert^{2}$.**

**Theorem (the invariants).** For $\breve Q=Q_{+}\Pi_++Q_{-}\Pi_-$,
$$
\boxed{\;
\operatorname{tr}L_{\breve Q}=\operatorname{tr}L_{\mathrm{ts},\breve Q}=Q_{+}+Q_{-}=2Q_{\blacktriangle},\qquad
\det L_{\breve Q}=\det L_{\mathrm{ts},\breve Q}=Q_{+}Q_{-}=\langle \breve Q\rangle_{\mathrm{ts}}
\;},
$$
with eigenvalues $Q_{+}$ and $Q_{-}$. The two sesquilinear operators satisfy
$$
(L^{*}_{\breve Q})^{2}=\operatorname{diag}(Q_{+}\bar Q_{-},\ Q_{-}\bar Q_{+}),\qquad
(L_{\mathrm{ts}*,\breve Q})^{2}=\operatorname{diag}(Q_{-}\bar Q_{+},\ Q_{+}\bar Q_{-}),
$$
and their real determinants are
$$
\det_{\mathbb{R}}L^{*}_{\breve Q}=\det_{\mathbb{R}}L_{\mathrm{ts}*,\breve Q}=\lvert Q_{+}Q_{-}\rvert^{2}=\lvert \langle \breve Q\rangle_{\mathrm{ts}}\rvert^{2}.
$$

*Proof.* The trace and the determinant of $\operatorname{diag}(Q_{+},Q_{-})$ and of $\operatorname{diag}(Q_{-},Q_{+})$ are $Q_{+}+Q_{-}$ and $Q_{+}Q_{-}$; in the complex basis the plain matrix $\begin{smallmatrix}Q_{\blacktriangle}&Q_{\blacktriangledown}\\Q_{\blacktriangledown}&Q_{\blacktriangle}\end{smallmatrix}$ has characteristic polynomial $(Q_{\blacktriangle}-\lambda)^{2}-Q_{\blacktriangledown}^{2}$, whose roots are $Q_{\blacktriangle}\pm Q_{\blacktriangledown}=Q_{+},Q_{-}$, and the tessarine bilinear matrix gives the same. For the sesquilinear operators, applying the operator twice conjugates twice and uses the display of §*The Matrices on the Idempotent Basis*: $(Q_{2+},Q_{2-})\mapsto(Q_{+}\bar Q_{2-},Q_{-}\bar Q_{2+})\mapsto(Q_{+}\overline{Q_{-}\bar Q_{2+}},Q_{-}\overline{Q_{+}\bar Q_{2-}})=(Q_{+}\bar Q_{-}\,Q_{2+},Q_{-}\bar Q_{+}\,Q_{2-})$, and symmetrically for the companion. The real determinant of a real-linear operator given by a complex matrix composed with the conjugation is the squared modulus of the complex determinant, $\lvert\det\begin{smallmatrix}0&Q_{+}\\Q_{-}&0\end{smallmatrix}\rvert^{2}=\lvert Q_{+}Q_{-}\rvert^{2}$.

**Corollary (the invertibility is the unit criterion).** Each of the four operators is invertible exactly when $Q_{+}\neq0$ and $Q_{-}\neq0$, that is exactly when $\breve Q$ is a unit; and each is singular at a non-zero element exactly when $\breve Q$ is a zero divisor. The operator picture does not remove the zero divisors: the singular non-zero elements are present in all four.

*Proof.* The determinant of the two bilinear operators is $Q_{+}Q_{-}$ and the real determinant of the two sesquilinear operators is $\lvert Q_{+}Q_{-}\rvert^{2}$, both non-zero exactly for the units of *Norm and Invertibility in the Algebra of the Reduced Biquaternions*.

## The Adjoints and the Involutions

**The adjoint of the plain operator is the conjugate for the definite form and the star-conjugate for the indefinite one.**

**Theorem (the adjoints).** For the definite form $\langle\cdot\rangle_{\mathrm{ts}*}$, the adjoint of the plain multiplication is the bar-conjugate element,
$$
\boxed{\;
(L_{\breve Q})^{K}=L_{\bar{\breve Q}}
\;};
$$
for the indefinite form $\langle\cdot,\cdot\rangle_{*}$, the adjoint is the star-conjugate element,
$$
(L_{\breve Q})^{H}=L_{\breve Q^{*}} .
$$

*Proof.* In the idempotent coordinates, with $\breve Q_{i}=Q_{i+}\Pi_++Q_{i-}\Pi_-$, one has $\langle \breve Q_{1},\breve Q_{2}\rangle_{\mathrm{ts}*}=\tfrac12(Q_{1+}\bar Q_{2+}+Q_{1-}\bar Q_{2-})$ and $H(\breve Q_{1},\breve Q_{2})=\tfrac12(Q_{1+}\bar Q_{2-}+Q_{1-}\bar Q_{2+})$. For $\langle\cdot\rangle_{\mathrm{ts}*}$: $\langle L_{\breve Q}\breve Q_{2},\breve Q_{3}\rangle_{\mathrm{ts}*}=\langle \breve Q \breve Q_{2},\breve Q_{3}\rangle_{\mathrm{ts}*}=\tfrac12(Q_{+}Q_{2+}\bar Q_{3+}+Q_{-}Q_{2-}\bar Q_{3-})$ and $\langle \breve Q_{2},L_{\bar{\breve Q}}\breve Q_{3}\rangle_{\mathrm{ts}*}=\tfrac12(Q_{2+}\overline{\bar Q_{+}Q_{3+}}+Q_{2-}\overline{\bar Q_{-}Q_{3-}})=\tfrac12(Q_{+}Q_{2+}\bar Q_{3+}+Q_{-}Q_{2-}\bar Q_{3-})$, equal. For $H$: $H(\breve Q \breve Q_{2},\breve Q_{3})=\tfrac12(Q_{+}Q_{2+}\bar Q_{3-}+Q_{-}Q_{2-}\bar Q_{3+})$ and $H(\breve Q_{2},\breve Q^{*}\breve Q_{3})$ with $\breve Q^{*}$ of coordinates $(\bar Q_{-},\bar Q_{+})$ gives $\tfrac12(Q_{2+}\overline{\bar Q_{-} Q_{3+}}+Q_{2-}\overline{\bar Q_{+} Q_{3-}})=\tfrac12(Q_{+}Q_{2+}\bar Q_{3-}+Q_{-}Q_{2-}\bar Q_{3+})$, equal. The two adjoint rules are the two rows of the table of the conjugations, the bar for the definite form and the star for the indefinite one.

**Corollary (the involutions act by swapping).** In the idempotent basis the tessarine sign swaps the two diagonal entries, $L_{\breve Q_{\mathrm{ts}}}=\operatorname{diag}(Q_{-},Q_{+})$, and the star conjugates and swaps them, $L_{\breve Q^{*}}=\operatorname{diag}(\bar Q_{-},\bar Q_{+})$; the two are the transposition and the conjugate-transposition of the diagonal model.

*Proof.* The idempotent coordinate of $\breve Q_{\mathrm{ts}}$ are $(Q_{-},Q_{+})$ and those of $\breve Q^{*}$ are $(\bar Q_{-},\bar Q_{+})$, by *Introduction to the $2\times2$ Matrix Element Representation of Reduced Biquaternions*; the operator of $\breve Q_{\mathrm{ts}}$ is $\operatorname{diag}(Q_{-},Q_{+})$ and that of $\breve Q^{*}$ is $\operatorname{diag}(\bar Q_{-},\bar Q_{+})$.

## The Algebra of Operators

**Theorem (the operator algebra).** The map $\breve Q\mapsto L_{\breve Q}$ is an isomorphism of algebras onto the two-dimensional space of operators $\{L_{\breve Q}\}$, and the enveloping algebra generated by the left and the right multiplications acts through the left multiplications alone, its image being $\{L_{\breve Q}\}$ and not the whole of $\operatorname{End}_{\mathbb{C}}(\mathbb{B}_{\mathrm{r}})$.

*Proof.* The multiplicativity $L_{\breve Q_{1}}L_{\breve Q_{2}}=L_{\breve Q_{1}\breve Q_{2}}$ and the injectivity are *Introduction to Reduced Biquaternion Element Representations*; because the algebra is commutative every product $L_{\breve Q_{1}}R_{\breve Q_{2}}=L_{\breve Q_{1}\breve Q_{2}}$ is again a left multiplication, so the image of the enveloping algebra is $\{L_{\breve Q}\}$, of complex dimension two, against the four dimensions of $\operatorname{End}_{\mathbb{C}}(\mathbb{B}_{\mathrm{r}})\cong M_{2}(\mathbb{C})$.

**Corollary (the sandwich operators).** Every sandwich operator is a left multiplication, $\Theta_{\breve Q}(\breve Q_{2})=\breve Q \breve Q_{2}\breve Q=L_{\breve Q^{2}}(\breve Q_{2})$, and the sandwich operators carry no information beyond the left multiplications; in the idempotent basis $\Theta_{\breve Q}=\operatorname{diag}(Q_{+}^{2},Q_{-}^{2})$.

*Proof.* The commutativity gives $\breve Q \breve Q_{2}\breve Q=\breve Q^{2}\breve Q_{2}$, whose operator is $L_{\breve Q^{2}}$ with diagonal form $\operatorname{diag}(Q_{+}^{2},Q_{-}^{2})$.

## Comparison of the Four Products

**The four operators are compared in the table below.**

| product | operator | complex-linear | matrix on $1,j$ | idempotent form | trace | determinant | eigenvalues |
|---|---|---|---|---|---|---|---|
| $\breve Q \breve Q_{2}$ | $L_{\breve Q}$ | **yes** | $\begin{smallmatrix}Q_{\blacktriangle}&Q_{\blacktriangledown}\\Q_{\blacktriangledown}&Q_{\blacktriangle}\end{smallmatrix}$ | $\operatorname{diag}(Q_{+},Q_{-})$ | $Q_{+}+Q_{-}$ | $Q_{+}Q_{-}$ | $Q_{+},Q_{-}$ |
| $\breve Q_{\mathrm{ts}}\breve Q_{2}$ | $L_{\mathrm{ts},\breve Q}$ | **yes** | $\begin{smallmatrix}Q_{\blacktriangle}&-Q_{\blacktriangledown}\\-Q_{\blacktriangledown}&Q_{\blacktriangle}\end{smallmatrix}$ | $\operatorname{diag}(Q_{-},Q_{+})$ | $Q_{+}+Q_{-}$ | $Q_{+}Q_{-}$ | $Q_{+},Q_{-}$ |
| $\breve Q \breve Q_{2}^{*}$ | $L^{*}_{\breve Q}$ | no (conjugate) | $\begin{smallmatrix}Q_{\blacktriangle}&-Q_{\blacktriangledown}\\Q_{\blacktriangledown}&-Q_{\blacktriangle}\end{smallmatrix}\circ\kappa$ | $\begin{smallmatrix}0&Q_{+}\\Q_{-}&0\end{smallmatrix}\circ\kappa$ | — | $\lvert Q_{+}Q_{-}\rvert^{2}$ (real) | real-linear |
| $\breve Q_{\mathrm{ts}}\breve Q_{2}^{*}$ | $L_{\mathrm{ts}*,\breve Q}$ | no (conjugate) | $\begin{smallmatrix}Q_{\blacktriangle}&Q_{\blacktriangledown}\\-Q_{\blacktriangledown}&-Q_{\blacktriangle}\end{smallmatrix}\circ\kappa$ | $\begin{smallmatrix}0&Q_{-}\\Q_{+}&0\end{smallmatrix}\circ\kappa$ | — | $\lvert Q_{+}Q_{-}\rvert^{2}$ (real) | real-linear |

**Theorem (the two pairs).** The two bilinear operators are complex-linear with the same trace and determinant, differing by the exchange of the two idempotent coordinates; the two sesquilinear operators are conjugate-linear with the same real determinant and differ by the same exchange. All four are invertible exactly for the units, and all four are singular at the zero divisors.

*Proof.* The invariants are those of §*Trace, Determinant and Eigenvalues*; the exchange of the two coordinates is the tessarine sign, which is the difference between the plain and the tessarine slot; and the invertibility is the unit criterion.

## Summary

Each of the four general products of the reduced biquaternion algebra has a left multiplication operator, $L_{\breve Q}$, $L_{\mathrm{ts},\breve Q}$, $L^{*}_{\breve Q}$ and $L_{\mathrm{ts}*,\breve Q}$, and the four are collected and compared here. On the complex basis $1,j$ they are the matrices $\begin{smallmatrix}Q_{\blacktriangle}&Q_{\blacktriangledown}\\Q_{\blacktriangledown}&Q_{\blacktriangle}\end{smallmatrix}$, $\begin{smallmatrix}Q_{\blacktriangle}&-Q_{\blacktriangledown}\\-Q_{\blacktriangledown}&Q_{\blacktriangle}\end{smallmatrix}$, $\begin{smallmatrix}Q_{\blacktriangle}&-Q_{\blacktriangledown}\\Q_{\blacktriangledown}&-Q_{\blacktriangle}\end{smallmatrix}\circ\kappa$ and $\begin{smallmatrix}Q_{\blacktriangle}&Q_{\blacktriangledown}\\-Q_{\blacktriangledown}&-Q_{\blacktriangle}\end{smallmatrix}\circ\kappa$; in the idempotent basis they are $\operatorname{diag}(Q_{+},Q_{-})$, $\operatorname{diag}(Q_{-},Q_{+})$ and the two off-diagonal matrices with the conjugation, differing only in the placement of $Q_{+}$ and $Q_{-}$. The two bilinear operators are complex-linear with trace $Q_{+}+Q_{-}=2Q_{\blacktriangle}$, determinant $Q_{+}Q_{-}=\langle \breve Q\rangle_{\mathrm{ts}}$ and eigenvalues $Q_{+},Q_{-}$; the two sesquilinear operators are conjugate-linear, with squares $\operatorname{diag}(Q_{+}\bar Q_{-},Q_{-}\bar Q_{+})$ and $\operatorname{diag}(Q_{-}\bar Q_{+},Q_{+}\bar Q_{-})$ and real determinant $\lvert \langle \breve Q\rangle_{\mathrm{ts}}\rvert^{2}$. Every operator is invertible exactly for the **units** and singular at the **zero divisors**, so the operator picture preserves the absence of division. The adjoint of the plain multiplication is $L_{\bar{\breve Q}}$ for the definite form and $L_{\breve Q^{*}}$ for the indefinite one; the operator image $\{L_{\breve Q}\}$ is a maximal commutative subalgebra of complex dimension two, the right multiplications coincide with the left ones for the plain product, and every sandwich operator is a left multiplication.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L^{\circ}_{\breve Q}$ | the left multiplication $\breve Q_{2}\mapsto \breve Q\circ \breve Q_{2}$ for the product $\circ$ |
| $L_{\breve Q}$ | the plain left multiplication, $\breve Q_{2}\mapsto \breve Q \breve Q_{2}$ |
| $\kappa$ | the coefficient conjugation $\binom{Q_{2\blacktriangle}}{Q_{2\blacktriangledown}}\mapsto\binom{\bar Q_{2\blacktriangle}}{\bar Q_{2\blacktriangledown}}$ |
| $\operatorname{diag}(Q_{+},Q_{-})$, $\operatorname{diag}(Q_{-},Q_{+})$ | the idempotent forms of the two bilinear operators |
| $(L_{\breve Q})^{K}=L_{\bar{\breve Q}}$ | the adjoint of the plain operator for the definite form |
| $(L_{\breve Q})^{H}=L_{\breve Q^{*}}$ | the adjoint of the plain operator for the indefinite form |

## Further Reading

- [The Four Products, Their Forms and Their Algebraic Norms](the-four-products-their-forms-and-their-algebraic-norms-of-the-reduced-biquaternions.html), for the four products and the forms.
- [The Multiplication Operators of the Algebra of the Reduced Biquaternions](the-multiplication-operators-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), for the plain operator alone.
- [Introduction to the $2\times2$ Matrix Element Representation of Reduced Biquaternions](introduction-to-the-2x2-matrix-element-representation-of-reduced-biquaternions.html), for the matrices of the element.
- [Norm and Invertibility in the Algebra of the Reduced Biquaternions](norm-and-invertibility-in-the-general-plain-algebra-of-the-reduced-biquaternions.html), for the invertibility criterion.
- [Modules over the Biquaternion Algebra](modules-over-the-biquaternion-algebra.html), for the non-commutative companion with its one simple module of dimension two.
