# __Operators on the Reduced Biquaternions__

## Introduction

Each of the four general products of the reduced biquaternion algebra has a **left multiplication operator**, $L^{\circ}_{X}:W\mapsto X\circ W$, and the four operators are collected here and compared. Two of them are complex-linear, those of the two bilinear products; two are conjugate-linear, those of the two sesquilinear products. On the complex basis $1,j$ each is a $2\times2$ matrix, and in the idempotent basis each becomes diagonal or off-diagonal of a simple shape, which makes the trace, the determinant, the eigenvalues and the invertibility visible at once. The multiplication of the algebra is **commutative**, so the left and the right multiplication operators of the plain product coincide; the algebra **has zero divisors**, so an operator may be singular at a non-zero element; and it is **not a division algebra**, so no operator calculus makes it one. The plain operator alone, with its matrix, trace, determinant and adjoints, is *The Multiplication Operators of the General Plain Algebra of the Reduced Biquaternions*; this article is the collection and the comparison of the four.

**Conventions.** The basis is $1,i,j,ij$ with $i^{2}=-1$, $j^{2}=+1$, $ji=ij$; the element is $T=A+Bj$ with $A=a+ia'$, $B=b+ib'$; the idempotents are $\Pi_{1,2}=\tfrac12(1\pm j)$ and the idempotent coordinates are $q_1=A+B$, $q_2=A-B$, with $T=q_1\Pi_{1}+q_2\Pi_{2}$. The four general products are the general plain bilinear $TW$, the general quaternionic bilinear $T^{\natural}W$, the general plain sesquilinear $TW^{*}$ and the general quaternionic sesquilinear $T^{\natural}W^{*}$, with the forms $B,N,H,K$ of *The Four Products, Their Forms and Their Algebraic Norms*. The element glyph is $T$, without a tilde; a product written $\circ$ is generic and its identity is stated at each use.

**Boundaries.** The four products and their forms are *The Four Products, Their Forms and Their Algebraic Norms*, and the forms are *The Forms of the General Plain Algebra of the Reduced Biquaternions*; the plain operator alone is *The Multiplication Operators of the General Plain Algebra of the Reduced Biquaternions*; the idempotent splitting is *Ideals and Peirce Decomposition of the General Plain Algebra of the Reduced Biquaternions*; the invertibility criterion is *Norm and Invertibility in the General Plain Algebra of the Reduced Biquaternions*; and the matrices of the element are *Introduction to the $2\times2$ Matrix Element Representation of Reduced Biquaternions*. The biquaternion counterpart is *Operators on the Biquaternions*.

## The Four Left Multiplication Operators

**Definition.** For a product $\circ$ and an element $X$, the **left multiplication** is the map
$$
L^{\circ}_{X}:W\mapsto X\circ W ,
$$
with the superscript dropped for the plain product, $L_{X}(W)=XW$.

### The Matrices on the Complex Basis

**Theorem (the four matrices).** On the complex basis $1,j$, acting on the column $\binom{C}{D}$ of $W=C+Dj$, the four left multiplications are
$$
L_{X}=\begin{pmatrix}A&B\\ B&A\end{pmatrix},\qquad
L^{\natural}_{X}=\begin{pmatrix}A&-B\\ -B&A\end{pmatrix},
$$
$$
L^{*}_{X}=\begin{pmatrix}A&-B\\ B&-A\end{pmatrix}\circ\kappa,\qquad
L^{\natural*}_{X}=\begin{pmatrix}A&B\\ -B&-A\end{pmatrix}\circ\kappa ,
$$
where $\kappa$ is the coefficient conjugation $\kappa\binom{C}{D}=\binom{\bar C}{\bar D}$ and $X=A+Bj$.

*Proof.* Read the four coordinate tables. The plain product $XW=(AC+BD)+(AD+BC)j$ has the columns $\binom{A}{B}$ and $\binom{B}{A}$, giving the first matrix. The quaternionic bilinear product $X^{\natural}W=(AC-BD)+(AD-BC)j$ has the columns $\binom{A}{-B}$ and $\binom{-B}{A}$, giving the second. For the two sesquilinear products, $W^{*}=\binom{\bar C}{-\bar D}=\sigma_{3}\kappa\binom{C}{D}$ with $\sigma_{3}=\operatorname{diag}(1,-1)$, so $L^{*}_{X}=L_{X}\sigma_{3}\kappa$ and $L^{\natural*}_{X}=L^{\natural}_{X}\sigma_{3}\kappa$; multiplying the two bilinear matrices into $\sigma_{3}$ gives the last two displays.

**Corollary (linear against conjugate-linear).** The operators $L_{X}$ and $L^{\natural}_{X}$ of the bilinear products are **complex-linear**; the operators $L^{*}_{X}$ and $L^{\natural*}_{X}$ of the sesquilinear products are **conjugate-linear**, and are real-linear but not complex-linear.

*Proof.* The bilinear matrices have constant complex entries and act by matrix multiplication, hence are complex-linear; the two sesquilinear operators carry the map $\kappa$, which is conjugate-linear, so they are conjugate-linear.

### The Matrices on the Idempotent Basis

**Theorem (the idempotent form).** In the idempotent basis, acting on the column $\binom{m}{n}$ of $W=m\Pi_{1}+n\Pi_{2}$, the four operators are
$$
L_{X}=\operatorname{diag}(q_1,q_2),\qquad
L^{\natural}_{X}=\operatorname{diag}(q_2,q_1),
$$
$$
L^{*}_{X}=\begin{pmatrix}0&q_1\\ q_2&0\end{pmatrix}\circ\kappa,\qquad
L^{\natural*}_{X}=\begin{pmatrix}0&q_2\\ q_1&0\end{pmatrix}\circ\kappa .
$$

*Proof.* In the idempotent coordinates the product is componentwise, $XW=q_1\,m\,\Pi_{1}+q_2\,n\,\Pi_{2}=L_{X}(m,n)=(um,vn)$, which is $\operatorname{diag}(q_1,q_2)$; and $X^{\natural}=q_2\Pi_{1}+q_1\Pi_{2}$, so $X^{\natural}W=(q_2 m)\Pi_{1}+(q_1 n)\Pi_{2}$. For the sesquilinear products, $W^{*}=\bar n\Pi_{1}+\bar m\Pi_{2}$ because the star exchanges the two idempotents, so $XW^{*}=q_1\bar n\Pi_{1}+q_2\bar m\Pi_{2}$ and $X^{\natural}W^{*}=q_2\bar n\Pi_{1}+q_1\bar m\Pi_{2}$, which are the two off-diagonal displays.

**Corollary (the plain product is diagonal).** The plain operator is diagonal in the idempotent basis, with the two idempotent coordinates on the diagonal; the quaternionic bilinear operator is the same diagonal with the two entries **exchanged**, and the two sesquilinear operators are the two **off-diagonal** matrices with the conjugation. The four operators differ only in the placement of $q_1$ and $q_2$.

*Proof.* Read the four displays: the plain operator has $q_1$ first and $q_2$ second, the quaternionic bilinear operator the reverse, and the two sesquilinear operators have zeros on the diagonal and carry $q_1,q_2$ on the two off-diagonal entries.

## The Right Multiplication Operators

**The right multiplication operators coincide with the left ones for the plain product and differ for the other three.**

**Theorem.** For the plain product the right multiplication $R_{X}:W\mapsto WX$ equals the left one, $R_{X}=L_{X}$, because the multiplication is commutative. For the other three products the right operator is $R^{\circ}_{X}(W)=W\circ X$, and in the idempotent coordinates it is the left operator with the involution moved from $X$ in the left slot to $W$ in the right slot: writing $X=(q_1,q_2)$ and $W=(m,n)$,
$$
R^{\natural}_{X}=\begin{pmatrix}0&q_1\\ q_2&0\end{pmatrix},\qquad
R^{*}_{X}=\operatorname{diag}(\bar q_2,\bar q_1),\qquad
R^{\natural*}_{X}=\begin{pmatrix}0&\bar q_2\\ \bar q_1&0\end{pmatrix}.
$$

*Proof.* Commutativity gives $WX=XW$, hence $R_{X}=L_{X}$. For the other three, evaluate $W\circ X$ in the idempotent coordinates: the natural sign sends $W=(m,n)$ to $(p,q)$, so $R^{\natural}_{X}(m,n)=(n,m)\cdot(q_1,q_2)=(un,vm)$; the star sends $X=(q_1,q_2)$ to $(\bar q_2,\bar q_1)$, so $R^{*}_{X}(m,n)=(m,n)\cdot(\bar q_2,\bar q_1)=(m\bar q_2,n\bar q_1)$; and combining the two, $R^{\natural*}_{X}(m,n)=(n\bar q_2,m\bar q_1)$. These are the three displays, and they differ from the left operators $L^{\natural}_{X}=\operatorname{diag}(q_2,q_1)$, $L^{*}_{X}=\left(\begin{smallmatrix}0&q_1\\ q_2&0\end{smallmatrix}\right)\circ\kappa$ and $L^{\natural*}_{X}=\left(\begin{smallmatrix}0&q_2\\ q_1&0\end{smallmatrix}\right)\circ\kappa$.

**Corollary (the commutant).** The operators commuting with all the left multiplications of the plain product are the right multiplications, which are the left multiplications themselves; so the commutant of the image is the image, and the operator algebra $\{L_{X}\}$ is a maximal commutative subalgebra of $\operatorname{End}_{\mathbb{C}}(\mathbb{B}_{\mathrm{r}})$ of complex dimension two.

*Proof.* An operator commuting with every $L_{X}$ commutes in particular with $L_{j}=\operatorname{diag}(1,-1)$, hence is diagonal in the idempotent basis, hence is in the image; and the image is commutative by the commutativity of the algebra.

## Trace, Determinant and Eigenvalues

**The two bilinear operators share the trace $2A$, the determinant $N$ and the eigenvalues $q_1,q_2$; the two sesquilinear operators are conjugate-linear with real determinant $\lvert N\rvert^{2}$.**

**Theorem (the invariants).** For $X=q_1\Pi_{1}+q_2\Pi_{2}$,
$$
\operatorname{tr}L_{X}=\operatorname{tr}L^{\natural}_{X}=q_1+q_2=2A,\qquad
\det L_{X}=\det L^{\natural}_{X}=q_1q_2=\langle X\rangle_{\natural},
$$
with eigenvalues $q_1$ and $q_2$. The two sesquilinear operators satisfy
$$
(L^{*}_{X})^{2}=\operatorname{diag}(q_1\bar q_2,\ q_2\bar q_1),\qquad
(L^{\natural*}_{X})^{2}=\operatorname{diag}(q_2\bar q_1,\ q_1\bar q_2),
$$
and their real determinants are
$$
\det_{\mathbb{R}}L^{*}_{X}=\det_{\mathbb{R}}L^{\natural*}_{X}=\lvert q_1q_2\rvert^{2}=\lvert \langle X\rangle_{\natural}\rvert^{2}.
$$

*Proof.* The trace and the determinant of $\operatorname{diag}(q_1,q_2)$ and of $\operatorname{diag}(q_2,q_1)$ are $q_1+q_2$ and $q_1q_2$; in the complex basis the plain matrix $\begin{smallmatrix}A&B\\B&A\end{smallmatrix}$ has characteristic polynomial $(A-\lambda)^{2}-B^{2}$, whose roots are $A\pm B=q_1,q_2$, and the quaternionic bilinear matrix gives the same. For the sesquilinear operators, applying the operator twice conjugates twice and uses the display of §*The Matrices on the Idempotent Basis*: $(m,n)\mapsto(q_1\bar n,q_2\bar m)\mapsto(q_1\overline{q_2\bar m},q_2\overline{q_1\bar n})=(q_1\bar q_2\,m,q_2\bar q_1\,n)$, and symmetrically for the companion. The real determinant of a real-linear operator given by a complex matrix composed with the conjugation is the squared modulus of the complex determinant, $\lvert\det\begin{smallmatrix}0&q_1\\v&0\end{smallmatrix}\rvert^{2}=\lvert q_1q_2\rvert^{2}$.

**Corollary (the invertibility is the unit criterion).** Each of the four operators is invertible exactly when $q_1\neq0$ and $q_2\neq0$, that is exactly when $X$ is a unit; and each is singular at a non-zero element exactly when $X$ is a zero divisor. The operator picture does not remove the zero divisors: the singular non-zero elements are present in all four.

*Proof.* The determinant of the two bilinear operators is $q_1q_2$ and the real determinant of the two sesquilinear operators is $\lvert q_1q_2\rvert^{2}$, both non-zero exactly for the units of *Norm and Invertibility in the General Plain Algebra of the Reduced Biquaternions*.

## The Adjoints and the Involutions

**The adjoint of the plain operator is the conjugate for the definite form and the star-conjugate for the indefinite one.**

**Theorem (the adjoints).** For the definite form $\langle\cdot\rangle_{\natural*}$, the adjoint of the plain multiplication is the bar-conjugate element,
$$
(L_{X})^{K}=L_{\bar X};
$$
for the indefinite form $\langle\cdot,\cdot\rangle_{*}$, the adjoint is the star-conjugate element,
$$
(L_{X})^{H}=L_{X^{*}} .
$$

*Proof.* In the idempotent coordinates \langle X,Y\rangle_{\natural*}=\tfrac12(m_{X}\bar m_{Y}+n_{X}\bar n_{Y})$ and $H(X,Y)=\tfrac12(m_{X}\bar n_{Y}+n_{X}\bar m_{Y})$. For $\langle\cdot\rangle_{\natural*}$: \langle L_{X}W,Y\rangle_{\natural*}=K(XW,Y)=\tfrac12(q_{1,X}q_{1,W}\bar q_{1,Y}+q_{2,X}q_{2,W}\bar q_{2,Y})$ and \langle W,L_{\bar X}Y\rangle_{\natural*}=\tfrac12(q_{1,W}\overline{\bar q_{1,X}q_{1,Y}}+q_{2,W}\overline{\bar q_{2,X}q_{2,Y}})=\tfrac12(q_{1,X}q_{1,W}\bar q_{1,Y}+q_{2,X}q_{2,W}\bar q_{2,Y})$, equal. For $H$: $H(XW,Y)=\tfrac12(q_{1,X}q_{1,W}\bar q_{2,Y}+q_{2,X}q_{2,W}\bar q_{1,Y})$ and $H(W,X^{*}Y)$ with $X^{*}$ of coordinates $(\bar q_2,\bar q_1)$ gives $\tfrac12(q_{1,W}\overline{\bar q_2 q_{1,Y}}+q_{2,W}\overline{\bar q_1 q_{2,Y}})=\tfrac12(q_{1,X}q_{1,W}\bar q_{2,Y}+q_{2,X}q_{2,W}\bar q_{1,Y})$, equal. The two adjoint rules are the two rows of the table of the conjugations, the bar for the definite form and the star for the indefinite one.

**Corollary (the involutions act by swapping).** In the idempotent basis the natural sign swaps the two diagonal entries, $L_{X^{\natural}}=\operatorname{diag}(q_2,q_1)$, and the star conjugates and swaps them, $L_{X^{*}}=\operatorname{diag}(\bar q_2,\bar q_1)$; the two are the transposition and the conjugate-transposition of the diagonal model.

*Proof.* The idempotent coordinate of $X^{\natural}$ are $(q_2,q_1)$ and those of $X^{*}$ are $(\bar q_2,\bar q_1)$, by *Introduction to the $2\times2$ Matrix Element Representation of Reduced Biquaternions*; the operator of $X^{\natural}$ is $\operatorname{diag}(q_2,q_1)$ and that of $X^{*}$ is $\operatorname{diag}(\bar q_2,\bar q_1)$.

## The Algebra of Operators

**Theorem (the operator algebra).** The map $X\mapsto L_{X}$ is an isomorphism of algebras onto the two-dimensional space of operators $\{L_{X}\}$, and the enveloping algebra generated by the left and the right multiplications acts through the left multiplications alone, its image being $\{L_{X}\}$ and not the whole of $\operatorname{End}_{\mathbb{C}}(\mathbb{B}_{\mathrm{r}})$.

*Proof.* The multiplicativity $L_{X}L_{Y}=L_{XY}$ and the injectivity are *Introduction to Reduced Biquaternion Element Representations*; because the algebra is commutative every product $L_{X}R_{Y}=L_{XY}$ is again a left multiplication, so the image of the enveloping algebra is $\{L_{X}\}$, of complex dimension two, against the four dimensions of $\operatorname{End}_{\mathbb{C}}(\mathbb{B}_{\mathrm{r}})\cong M_{2}(\mathbb{C})$.

**Corollary (the sandwich operators).** Every sandwich operator is a left multiplication, $\Theta_{X}(W)=XWX=L_{X^{2}}(W)$, and the sandwich operators carry no information beyond the left multiplications; in the idempotent basis $\Theta_{X}=\operatorname{diag}(q_1^{2},q_2^{2})$.

*Proof.* The commutativity gives $XWX=X^{2}W$, whose operator is $L_{X^{2}}$ with diagonal form $\operatorname{diag}(q_1^{2},q_2^{2})$.

## Comparison of the Four Products

**The four operators are compared in the table below.**

| product | operator | complex-linear | matrix on $1,j$ | idempotent form | trace | determinant | eigenvalues |
|---|---|---|---|---|---|---|---|
| $XW$ | $L_{X}$ | **yes** | $\begin{smallmatrix}A&B\\B&A\end{smallmatrix}$ | $\operatorname{diag}(q_1,q_2)$ | $q_1+q_2$ | $q_1q_2$ | $q_1,q_2$ |
| $X^{\natural}W$ | $L^{\natural}_{X}$ | **yes** | $\begin{smallmatrix}A&-B\\-B&A\end{smallmatrix}$ | $\operatorname{diag}(q_2,q_1)$ | $q_1+q_2$ | $q_1q_2$ | $q_1,q_2$ |
| $XW^{*}$ | $L^{*}_{X}$ | no (conjugate) | $\begin{smallmatrix}A&-B\\B&-A\end{smallmatrix}\circ\kappa$ | $\begin{smallmatrix}0&q_1\\v&0\end{smallmatrix}\circ\kappa$ | — | $\lvert q_1q_2\rvert^{2}$ (real) | real-linear |
| $X^{\natural}W^{*}$ | $L^{\natural*}_{X}$ | no (conjugate) | $\begin{smallmatrix}A&B\\-B&-A\end{smallmatrix}\circ\kappa$ | $\begin{smallmatrix}0&q_2\\u&0\end{smallmatrix}\circ\kappa$ | — | $\lvert q_1q_2\rvert^{2}$ (real) | real-linear |

**Theorem (the two pairs).** The two bilinear operators are complex-linear with the same trace and determinant, differing by the exchange of the two idempotent coordinates; the two sesquilinear operators are conjugate-linear with the same real determinant and differ by the same exchange. All four are invertible exactly for the units, and all four are singular at the zero divisors.

*Proof.* The invariants are those of §*Trace, Determinant and Eigenvalues*; the exchange of the two coordinates is the natural sign, which is the difference between the plain and the quaternionic slot; and the invertibility is the unit criterion.

## Summary

Each of the four general products of the reduced biquaternion algebra has a left multiplication operator, $L_{X}$, $L^{\natural}_{X}$, $L^{*}_{X}$ and $L^{\natural*}_{X}$, and the four are collected and compared here. On the complex basis $1,j$ they are the matrices $\begin{smallmatrix}A&B\\B&A\end{smallmatrix}$, $\begin{smallmatrix}A&-B\\-B&A\end{smallmatrix}$, $\begin{smallmatrix}A&-B\\B&-A\end{smallmatrix}\circ\kappa$ and $\begin{smallmatrix}A&B\\-B&-A\end{smallmatrix}\circ\kappa$; in the idempotent basis they are $\operatorname{diag}(q_1,q_2)$, $\operatorname{diag}(q_2,q_1)$ and the two off-diagonal matrices with the conjugation, differing only in the placement of $q_1$ and $q_2$. The two bilinear operators are complex-linear with trace $q_1+q_2=2A$, determinant $q_1q_2=\langle X\rangle_{\natural}$ and eigenvalues $q_1,q_2$; the two sesquilinear operators are conjugate-linear, with squares $\operatorname{diag}(q_1\bar q_2,q_2\bar q_1)$ and $\operatorname{diag}(q_2\bar q_1,q_1\bar q_2)$ and real determinant $\lvert \langle X\rangle_{\natural}\rvert^{2}$. Every operator is invertible exactly for the **units** and singular at the **zero divisors**, so the operator picture preserves the absence of division. The adjoint of the plain multiplication is $L_{\bar X}$ for the definite form and $L_{X^{*}}$ for the indefinite one; the operator image $\{L_{X}\}$ is a maximal commutative subalgebra of complex dimension two, the right multiplications coincide with the left ones for the plain product, and every sandwich operator is a left multiplication.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L^{\circ}_{X}$ | the left multiplication $W\mapsto X\circ W$ for the product $\circ$ |
| $L_{X}$ | the plain left multiplication, $W\mapsto XW$ |
| $\kappa$ | the coefficient conjugation $\binom{C}{D}\mapsto\binom{\bar C}{\bar D}$ |
| $\operatorname{diag}(q_1,q_2)$, $\operatorname{diag}(q_2,q_1)$ | the idempotent forms of the two bilinear operators |
| $(L_{X})^{K}=L_{\bar X}$ | the adjoint of the plain operator for the definite form |
| $(L_{X})^{H}=L_{X^{*}}$ | the adjoint of the plain operator for the indefinite form |

## Further Reading

- *The Four Products, Their Forms and Their Algebraic Norms* (`articles_maths/the-four-products-their-forms-and-their-algebraic-norms-of-the-reduced-biquaternions.md`), for the four products and the forms.
- *The Multiplication Operators of the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/the-multiplication-operators-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the plain operator alone.
- *Introduction to the $2\times2$ Matrix Element Representation of Reduced Biquaternions* (`articles_maths/introduction-to-the-2x2-matrix-element-representation-of-reduced-biquaternions.md`), for the matrices of the element.
- *Norm and Invertibility in the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/norm-and-invertibility-in-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the invertibility criterion.
- *Introduction to Biquaternion Element Representations* (`articles_maths/introduction-to-biquaternion-element-representations.md`), for the non-commutative companion with its one simple module of dimension two.
