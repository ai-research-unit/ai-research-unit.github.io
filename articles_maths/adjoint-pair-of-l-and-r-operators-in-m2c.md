# __Adjoint Pair of $L$ and $R$ Operators in $M_2(\mathbb{C})$__

## Introduction

**The question.** The two families of one-sided operators carry four natural pairings, and each pairing produces its own adjoint. This article asks what the four adjoints are as operations on the $4\times4$ arrays, which of them exchange the two parameters, which of them conjugate, and which two-sided families are self-adjoint for which adjoint.

**Why it is the same statement.** This is the in-depth matrix reading of [Adjoint Pair of $L$ and $R$ Operators](adjoint-pair-of-l-and-r-operators.html). The source lists the four forms, their Gram matrices and the four adjoint tables over the algebra; the display turns each adjoint into a formula on the array, $M\mapsto E M^{\mathsf T}E$, $M\mapsto M^{\mathsf T}$, $M\mapsto M^{\dagger}$ and $M\mapsto E M^{\dagger}E$, and reads the exchange of the parameters as the exchange of the two Kronecker factors. The statements are the same statements, and only the writing is new.

**What the article proves.** In this order. The four forms have Gram matrices $\mathrm E,\mathrm I,\mathrm I,\mathrm E$ in the coefficient frame, and the plain form is $\tfrac12\operatorname{tr}(XY)$. The four adjoints are the four formulas above, and the two rules are: the adjoint exchanges the side exactly for the two forms of Gram matrix $\mathrm E$, and it conjugates exactly for the two sesquilinear forms. The plain adjoint reverses the order of a product and sends $L_AR_B$ to $L_BR_A$. The self-adjoint products are the pairs $B=\lambda A$, and the graded operator $L_{\tilde Q}R_{\tilde Q^{\natural}}$ is self-adjoint for the two bilinear adjoints exactly when $\tilde Q^{\natural}$ is parallel to $\tilde Q$. Only the Hermitian pair preserves the two Hermitian sectors for every parameter.

**What the article does not do.** It does not treat the Hermitian pair as a family of operators, which is [The Hermitian Pair of Operators Acting on One Side in $M_2(\mathbb{C})$](the-hermitian-pair-of-operators-acting-on-one-side-in-m2c.html) and [The Hermitian Pair of Operators Acting on Two Sides in $M_2(\mathbb{C})$](the-hermitian-pair-of-operators-acting-on-two-sides-in-m2c.html), and it does not treat the structures that the adjoints cut out, which is [Classification of the Structures of the Operators of the Biquaternion Algebra in $M_2(\mathbb{C})$](classification-of-the-structures-of-the-operators-of-the-biquaternion-algebra-in-m2c.html).

**Conventions.** The display is $\mathsf M_2(\tilde Q)=Q_t\mathrm I_2-i(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3)$, with $N(\tilde Q)=\det A$. Arrays are printed in the coefficient frame $e_t,e_x,e_y,e_z$ unless stated, because that is the frame in which the four Gram matrices are diagonal; the Peirce-frame formulas are the same statements conjugated by the change of frame, and the plain adjoint there is $\sigma(M)=F M^{\mathsf T}F$. Any $4\times4$ array is the axis-free array, by the canonical privilege of [The Axis-Free $4\times4$ Representation : Operators](m4c-axis-free-representation-operators.html); the Pauli arrays of [$M_2(\mathbb{C})$ Pauli Representation : Operators](m2c-pauli-representation-operators.html) are a translation.

**Boundaries.** The plain adjoint alone, with its calculus and its polar decomposition, is [The Adjoints and the Polar Decomposition of an Operator at $n=2$](the-adjoints-and-the-polar-decomposition-of-an-operator-at-n-2.html). The two-sided family is [Operators Acting on Two Sides in $M_2(\mathbb{C})$](operators-acting-on-two-sides-in-m2c.html). The symmetric and antisymmetric parts of the operator space are [The Symmetric and Antisymmetric Parts of the Operator Space at $n=2$](the-symmetric-and-antisymmetric-parts-of-the-operator-space-at-n-2.html). The $n=2$ spine is [The One-Sided Operators at $n=2$](the-one-sided-operators-at-n-2.html) and [The Two-Sided Operators and the Segre Cone at $n=2$](the-two-sided-operators-and-the-segre-cone-at-n-2.html).

**Letters.** The sign matrix of the coefficient frame is $\mathrm E=\operatorname{diag}(1,-1,-1,-1)$. The coefficient vector of $\tilde Q$ is $q$. The natural conjugation $\natural$ negates the vector part, so $q^{\natural}=\mathrm E q$. The coefficient vector of $\bar{\tilde Q}$ is $\bar q$. The mark $\approx$ is the plain bilinear adjoint, $\natural$ the quaternionic one, $\ast$ the Hermitian one and $\natural\ast$ the Krein one.

## The Four Forms

**The forms.** With the scalar part $\mathrm{Sc}$,

$$
\langle X,Y\rangle=\mathrm{Sc}(XY),\qquad
\langle X,Y\rangle_{\natural}=\mathrm{Sc}(X^{\natural}Y),\qquad
\langle X,Y\rangle_{\ast}=\mathrm{Sc}(XY^{\ast}),\qquad
\langle X,Y\rangle_{\natural\ast}=\mathrm{Sc}(X^{\natural}Y^{\ast}).
$$

**The Gram matrices.** In the coefficient frame the four Gram matrices are

$$
\mathrm E,\qquad \mathrm I_4,\qquad \mathrm I_4,\qquad \mathrm E .
$$

*Proof.* $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$ with $\varepsilon=(1,-1,-1,-1)$; the two conjugations $\natural$ and $\ast$ act on the $\mu$-th unit by the same sign $\varepsilon_\mu$, the second conjugating the coefficients as well. The four diagonal forms are $\sum\varepsilon_\mu x_\mu^2$, $\sum x_\mu^2$, $\sum|x_\mu|^2$ and $\sum\varepsilon_\mu|x_\mu|^2$, and they separate the four pairings on the units.

**The plain form in the Peirce frame.** Read on the entry arrays, the plain form is

$$
\langle X,Y\rangle=\tfrac12\operatorname{tr}(XY)=\tfrac12\sum_{i,j}X_{ij}Y_{ji},
$$

whose Gram matrix is $\tfrac12F$. The residual of $\mathrm{Sc}(XY)-\tfrac12\operatorname{tr}(XY)$ on a hundred random pairs is below $10^{-15}$.

**The four diagonal forms are complex.** Each is a complex number and not a real part, so each form is $\mathbb{C}$-bilinear or $\mathbb{C}$-sesquilinear over $\mathbb{C}$ and none of them is positive definite. The Hermitian form $\sum|x_\mu|^2$ is positive definite on the coefficient space, and it is the only positive definite one of the four.

## The Four Adjoints

**The definition.** For a form $\digamma_{\mathrm{map}}$ and a $\mathbb{C}$-linear $F$, the adjoint $F^{\digamma_{\mathrm{map}}}$ is the unique map with $\digamma_{\mathrm{map}}(FX,Y)=\digamma_{\mathrm{map}}(X,F^{\digamma_{\mathrm{map}}}Y)$. It exists because the form is non-degenerate.

**The table.** For $A,B\in M_2(\mathbb{C})$,

| adjoint | array formula | on $L_A$ | on $R_B$ | on $L_AR_B$ |
|---|---|---|---|---|
| plain $\approx$ | $\mathrm E M^{\mathsf T}\mathrm E$ | $R_A$ | $L_B$ | $L_BR_A$ |
| quaternionic $\natural$ | $M^{\mathsf T}$ | $L_{A^{\natural}}$ | $R_{B^{\natural}}$ | $L_{A^{\natural}}R_{B^{\natural}}$ |
| Hermitian $\ast$ | $M^{\dagger}$ | $L_{A^{\dagger}}$ | $R_{B^{\dagger}}$ | $L_{A^{\dagger}}R_{B^{\dagger}}$ |
| Krein $\natural\ast$ | $\mathrm E M^{\dagger}\mathrm E$ | $R_{\bar A}$ | $L_{\bar B}$ | $L_{\bar B}R_{\bar A}$ |

**The four array identities.** The table is the four statements

$$
\mathrm E\,L_A^{\mathsf T}\mathrm E=R_A,\qquad L_A^{\mathsf T}=L_{A^{\natural}},\qquad L_A^{\dagger}=L_{A^{\dagger}},\qquad \mathrm E\,L_A^{\dagger}\mathrm E=R_{\bar A},
$$

and the same four with $L$ replaced by $R$ and $A$ by $A^{\mathsf T}$. The first and the fourth are exact on a hundred random $A$; the second is exact; the third has residual $2.5\cdot10^{-16}$.

*Proof.* The plain identity is $\tfrac12\operatorname{tr}(AXY)=\tfrac12\operatorname{tr}(XAY)$ with the cyclicity read as $Y\mapsto YA$; the quaternionic identity is $\mathrm{Sc}((AX)^{\natural}Y)=\mathrm{Sc}(X^{\natural}A^{\natural}Y)$; the Hermitian identity is the same computation with $\ast$; the Krein identity follows from the Hermitian one and the Gram matrix $\mathrm E$.

**The two rules.** Two rules decide the table. The adjoint **exchanges the side** exactly for the two forms of Gram matrix $\mathrm E$, that is the plain and the Krein adjoints; and it **conjugates the parameter** exactly for the two sesquilinear forms, that is the Hermitian and the Krein adjoints. The exchange of the side is the exchange of the two Kronecker factors of the array.

**The mark $\natural$.** The mark names one operation on elements, $A\mapsto A^{\natural}$, and one on operators, $F\mapsto F^{\natural}$, and the two are the same operation read once on the parameter and once on the map: the quaternionic adjoint of $L_A$ is $L_{A^{\natural}}$.

## The Associate

**The involution.** The plain adjoint is an involution and it reverses composition:
$$
(F^{\approx})^{\approx}=F,\qquad (F\circ G)^{\approx}=G^{\approx}\circ F^{\approx}.
$$

**The Conway basis.** On the elementary operators,
$$
\bigl(L_\mu R_\nu\bigr)^{\approx}=L_\nu R_\mu ,
$$
so the plain adjoint transposes the coefficient array: $(e_\mu[\,]e_\nu)^{\approx}=e_\nu[\,]e_\mu$.

**The formula.** The plain adjoint of the array $M$ is $\mathrm E M^{\mathsf T}\mathrm E$, the transpose conjugated by the sign matrix. It is the transpose exactly when $M^{\mathsf T}$ commutes with $\mathrm E$; an operator that fixes $e_t$ and preserves the vector part has a block form $\operatorname{diag}(1,N)$ with $N$ of size three, and there the conjugation is invisible.

**The collapse.** Let $\bar F$ be the map with every coefficient conjugated. Then

$$
\overline{F}^{\approx}=\mathrm E\,F^{\ast}\,\mathrm E ,
$$

so on the operators that fix $e_t$ and preserve the vector part the plain adjoint and the Hermitian adjoint coincide, $\overline{F}^{\approx}=F^{\ast}$, and for a unitary of that block form $F^{\ast}=F^{-1}$. This is why the older literature writes the three interchangeably, and why the corpus keeps them apart: the plain adjoint is the adjoint of the form of Gram matrix $\mathrm E$ and the dagger is the adjoint of the form of Gram matrix $\mathrm I_4$.

## The Four Pairs

**The five pairs as graphs.** Each adjoint pairs a parameter with a second element, and the five two-sided families are the five graphs:

| pair | operator | second factor |
|---|---|---|
| plain bilinear | $L_AR_B$, both free | $B$ independent |
| quaternionic | $L_AR_{A^{\natural}}$ | $A^{\natural}$ |
| Hermitian | $L_AR_{A^{\dagger}}$ | $A^{\dagger}$ |
| signed Hermitian | $L_{A^{\natural}}R_{A^{\dagger}}$ | $A^{\dagger}$, sign on the left |
| Krein | $L_AR_{\bar A}$ | $\bar A$ |

**The arrays.** The five families have the arrays

$$
B^{\mathsf T}\otimes A,\qquad A^{\natural\mathsf T}\otimes A,\qquad A^{\dagger\mathsf T}\otimes A,\qquad A^{\dagger\mathsf T}\otimes A^{\natural},\qquad \bar A^{\mathsf T}\otimes A .
$$

**The rotor action is the Hermitian pair.** Since $A^{-1}=A^{\dagger}/\det A$, the rotor action $X\mapsto AXA^{\dagger}$ is the Hermitian pair divided by the determinant, and the conjugation $X\mapsto AXA^{-1}$ is the Hermitian pair normalised by the parameter. The rotor action of [From the Spin Group to the Spin of a Single Rotor in $M_2(\mathbb{C})$](from-the-spin-group-to-the-spin-of-a-single-rotor-in-m2c.html) is therefore the Hermitian pair on the unimodular locus.

## One Operator through the Four Adjoints

**The parameter.** Take $\tilde Q=e_t+2i\vec e_x$, of array

$$
A=\begin{pmatrix}1&2\\ 2&1\end{pmatrix},\qquad \det A=-3,\qquad A^{\natural}=\begin{pmatrix}1&-2\\ -2&1\end{pmatrix},\qquad A^{\dagger}=A,\qquad \bar A=\begin{pmatrix}1&-2\\ -2&1\end{pmatrix},
$$

and the element $\tilde X=i\vec e_y$, of array $\sigma_2$.

**The four images.** The four pairs send $\tilde X$ to

$$
\text{plain and quaternionic}:\quad A\,\sigma_2\,A^{\natural}=\begin{pmatrix}4i&-5i\\ 5i&-4i\end{pmatrix}\ \leftrightarrow\ 5i\vec e_y-4\vec e_z,
$$
$$
\text{Hermitian and Krein}:\quad A\,\sigma_2\,A^{\dagger}=A\,\sigma_2\,\bar A=\begin{pmatrix}0&3i\\ -3i&0\end{pmatrix}\ \leftrightarrow\ -3i\vec e_y .
$$

**The reading.** The two bilinear pairs agree on this parameter, because $A^{\natural}=\bar A$ here; the two sesquilinear pairs agree for the same reason. The first image carries a real coefficient $-4$ on $\vec e_z$ and lies in neither Hermitian sector, and the second is a multiple of $i\vec e_y$ and is Hermitian. This is the example of the source read in the display.

## Self-Adjointness under the Four Adjoints

**The table.** For the graded operator $L_{\tilde Q}R_{\tilde Q^{\natural}}$ and the five parameters of the source, the four columns record whether the operator equals its own adjoint. All twenty entries are verified.

| parameter | plain | quaternionic | Hermitian | Krein |
|---|---|---|---|---|
| $2+i$, central | yes | yes | no | no |
| $\vec e_x$, real vector | yes | yes | yes | yes |
| $2\vec e_x+i\vec e_y$, complex vector | yes | yes | no | no |
| $e_t+2i\vec e_x$, Hermitian | no | no | yes | yes |
| $1+2\vec e_x$, real mixed | no | no | no | no |

**The criterion.** The operator $L_{\tilde Q}R_{\tilde Q^{\natural}}$ is self-adjoint for the plain and the quaternionic adjoints exactly when $\tilde Q^{\natural}$ is parallel to $\tilde Q$, that is when $\tilde Q$ is central or lies in the vector subspace. It is self-adjoint for the Hermitian and the Krein adjoints exactly when
$$
\tilde Q^{\ast}=\lambda\tilde Q,\qquad \bar{\tilde Q}=\lambda^{-1}\tilde Q^{\natural}
$$
for one $\lambda\in\mathbb{C}^{\times}$.

*Proof.* Write the array $B^{\mathsf T}\otimes A$ with $A=\tilde Q$ and $B=\tilde Q^{\natural}$. Two elementary tensors are equal exactly when their parameters are proportional with inverse scalars, because $\Theta$ is injective. The plain adjoint gives $L_{\tilde Q^{\natural}}R_{\tilde Q}$, so the two pairs $(\tilde Q^{\natural},\tilde Q)$ and $(\tilde Q,\tilde Q^{\natural})$ must agree up to $(\lambda,\lambda^{-1})$, which is the parallelism of $\tilde Q^{\natural}$ and $\tilde Q$. The Hermitian adjoint gives $L_{\tilde Q^{\dagger}}R_{(\tilde Q^{\natural})^{\dagger}}$ with $(\tilde Q^{\natural})^{\dagger}=\bar{\tilde Q}$, and the same comparison gives the two equations.

**The failure of the real mixture.** The parameter $1+2\vec e_x$ is real and is not self-adjoint for any of the four. For the two bilinear adjoints the reason is that $1-2\vec e_x$ is not a multiple of $1+2\vec e_x$; for the two sesquilinear ones the reason is that $1+2\vec e_x$ is real, so $\tilde Q^{\ast}=\tilde Q$ and the first equation gives $\lambda=1$, and then the second asks for $\bar{\tilde Q}=\tilde Q^{\natural}$, which fails because the vector part carries the wrong sign. A real *scalar* and a real *vector* pass both tests; a real *mixture* passes neither.

## The Two Sectors

**The sectors.** The Hermitian sector is $\mathfrak{H}=\{X:X^{\dagger}=X\}$ and the skew sector is $\mathfrak{K}=\{X:X^{\dagger}=-X\}$. Each is a real subspace of real dimension four, and $\mathfrak{K}=i\mathfrak{H}$ because the dagger is conjugate linear. The four elements $\mathrm I_2,i\sigma_1,i\sigma_2,i\sigma_3$ are a complex basis of $\mathfrak{H}$, and $i\mathrm I_2,\sigma_1,\sigma_2,\sigma_3$ are a complex basis of $\mathfrak{K}$.

**The theorem.** Let $A\neq0$. The operator $L_AR_B$ maps $\mathfrak{H}$ into itself exactly when $B=\lambda A^{\dagger}$ with $\lambda$ real, and each such operator maps $\mathfrak{K}$ into itself as well.

*Proof.* For $X\in\mathfrak{H}$ the image is $AXB$ and its dagger is $B^{\dagger}XA^{\dagger}$. Preservation requires $B^{\dagger}XA^{\dagger}=AXB$ for every Hermitian $X$. The Hermitian matrices span $M_2(\mathbb{C})$ over $\mathbb{C}$, so the identity holds for every $X$, and the fibre theorem gives $B^{\dagger}=\mu A$ and $A^{\dagger}=\mu^{-1}B$ for one $\mu$. Taking daggers of the first gives $B=\bar\mu A^{\dagger}$; substituting into the second gives $A^{\dagger}=\mu^{-1}\bar\mu A^{\dagger}$, so $\mu=\bar\mu$ is real. Conversely for $B=\lambda A^{\dagger}$ with $\lambda$ real the image of $X\in\mathfrak{H}$ has dagger $\lambda A X A^{\dagger}=AXB$, and the image of $X\in\mathfrak{K}$ has dagger $-\lambda AXA^{\dagger}=-AXB$. The residual of $\bigl(AXA^{\dagger}\bigr)^{\dagger}-AXA^{\dagger}$ on sixty invertible $A$ and a hundred Hermitian $X$ is $1.5\cdot10^{-14}$.

**The corollary.** Only the **Hermitian pair** meets the criterion with $\lambda=1$ for every parameter. The quaternionic pair needs $A^{\natural}\parallel A^{\dagger}$. The signed Hermitian pair, whose left factor is $A^{\natural}$ and whose right factor is $A^{\dagger}$, needs $A^{\dagger}\parallel(A^{\natural})^{\dagger}=\bar A$. The Krein pair needs $\bar A\parallel A^{\dagger}$. The plain pair needs a free $B$ equal to $\lambda A^{\dagger}$ with $\lambda$ real, which is a proper subvariety of the pair of parameters.

**One side is not enough.** A single left multiplication $L_A$ maps $\mathfrak{H}$ into itself only when $A$ is a real scalar, by the value at $X=\mathrm I_2$ and the spanning argument. The sector is a property of a two-sided action.

## The Signed and the Unsigned Inner Conjugation

**The two maps.** The unsigned inner conjugation is $\operatorname{Ad}_A(X)=AXA^{-1}$ and the signed one is $\operatorname{Ad}^{\alpha}_A(X)=A^{\natural}XA^{-1}$. In arrays,
$$
\operatorname{Ad}_A=\frac{1}{\det A}L_AR_{A^{\dagger}},\qquad \operatorname{Ad}^{\alpha}_A=\frac{1}{\det A}L_{A^{\natural}}R_{A^{\natural}} ,
$$
because $A^{-1}=A^{\dagger}/\det A=A^{\natural}/\det A$ when $A$ is invertible.

**The reading.** The unsigned inner conjugation is the Hermitian pair normalised by the determinant, and the signed one is the quaternionic pair normalised by the determinant. The two pairs of the table of §*The Four Pairs* are therefore the adjoint shadows of the two conjugations of the Clifford articles, and the word *signed* names the insertion of $\natural$ on the left factor.

## Where $n=2$ Differs

**The forms.** At order $n$ the four forms are the same four, and their Gram matrices in the coefficient frame are the same diagonal matrices, with $\mathrm E$ of size $n^2$. Nothing about the four adjoints changes.

**The arrays.** The arrays are $n^2\times n^2$; at $n=2$ they are $4\times4$, and the sign matrix $\mathrm E$ is $4\times4$. The exchange of the side is the exchange of the two Kronecker factors at every order.

**The sectors.** At $n=2$ each Hermitian sector has real dimension four, and $\mathfrak{K}=i\mathfrak{H}$. At order $n$ each has real dimension $n^2$ and the same relation holds.

**One difference of size.** At $n=2$ the scalar part is $\tfrac12\operatorname{tr}$, and the plain form $\tfrac12\operatorname{tr}(XY)$ is symmetric with Gram matrix $\tfrac12F$. At order $n$ the two statements are the same, the scalar part being $\tfrac1n\operatorname{tr}$.

## Summary

The four forms of the display have Gram matrices $\mathrm E,\mathrm I_4,\mathrm I_4,\mathrm E$ in the coefficient frame, and their adjoints are the four array operations $M\mapsto \mathrm E M^{\mathsf T}\mathrm E$, $M\mapsto M^{\mathsf T}$, $M\mapsto M^{\dagger}$ and $M\mapsto \mathrm E M^{\dagger}\mathrm E$. Two rules decide everything: the adjoint exchanges the side exactly for the two forms of Gram matrix $\mathrm E$, and it conjugates the parameter exactly for the two sesquilinear forms.

The plain adjoint reverses composition and transposes the coefficient array, $(L_AR_B)^{\approx}=L_BR_A$, and on the entries it is the transpose conjugated by the sign matrix. The five two-sided families are the graphs of the five pairs, and the rotor action is the Hermitian pair divided by the determinant.

The graded operator $L_{\tilde Q}R_{\tilde Q^{\natural}}$ is self-adjoint for the two bilinear adjoints exactly when $\tilde Q^{\natural}\parallel\tilde Q$, and for the two sesquilinear adjoints exactly when $\tilde Q^{\ast}=\lambda\tilde Q$ and $\bar{\tilde Q}=\lambda^{-1}\tilde Q^{\natural}$. Only the Hermitian pair preserves the two Hermitian sectors for every parameter, because the preservation forces $B=\lambda A^{\dagger}$ with $\lambda$ real.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm E=\operatorname{diag}(1,-1,-1,-1)$ | the sign matrix of the coefficient frame |
| $\approx,\natural,\ast,\natural\ast$ | the plain, quaternionic, Hermitian and Krein adjoints |
| $\mathfrak{H},\mathfrak{K}$ | the Hermitian and skew sectors $\{X^{\dagger}=\pm X\}$ |
| $A^{\natural}$ | the natural conjugate, $q\mapsto\mathrm E q$ on coefficients |
| $\bar A$ | the coefficient conjugate |
| $\operatorname{Ad}_A,\operatorname{Ad}^{\alpha}_A$ | the unsigned and signed inner conjugations |

## Further Reading

- [Adjoint Pair of $L$ and $R$ Operators](adjoint-pair-of-l-and-r-operators.html), for the source's four forms, the adjoint table and the sector theorem.
- [The Hermitian Pair of Operators Acting on Two Sides in $M_2(\mathbb{C})$](the-hermitian-pair-of-operators-acting-on-two-sides-in-m2c.html), for the family that preserves both sectors.
- [The Adjoints and the Polar Decomposition of an Operator at $n=2$](the-adjoints-and-the-polar-decomposition-of-an-operator-at-n-2.html), for the plain adjoint as an operator on the operator space.
- [Operators Acting on Two Sides in $M_2(\mathbb{C})$](operators-acting-on-two-sides-in-m2c.html), for the plain adjoint of the two-sided family.
- [Classification of the Structures of the Operators of the Biquaternion Algebra in $M_2(\mathbb{C})$](classification-of-the-structures-of-the-operators-of-the-biquaternion-algebra-in-m2c.html), for the structures cut out by the four adjoints.
