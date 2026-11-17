# __$M_2(\mathbb{C})$ Pauli Representation : Products, Forms and Norms__

## Introduction

**The subject.** The matrix expression, at the element size, of every quantity of the algebra that involves two elements: the product, the symmetric and the antisymmetric part of a product, the four forms, the four norms, the trace and the determinant.

**Why two elements.** *$M_2(\mathbb{C})$ Pauli Representation* reads one block: the entries $P_\pm$ and $X_\pm$, the images of the four units, the trace $2Q_t$, the determinant $\langle\tilde Q\rangle_{\natural}$, the eigenvalues, the adjugate and the four norms. It never writes a word in two blocks. This article does, and its subject is what an operation on two elements becomes as an operation on their two blocks.

**The order of the article.** The block and its three companions come first (§*The Element on One Plane*, §*The Three Companions*). The product and the split of a product follow (§*The Product*, §*The Symmetric and the Antisymmetric Part*), then the twelve products in one table (§*The Twelve Products*). The four forms and their Gram matrices on the plane come next, with the observation that three of the four are degenerate there (§*The Four Forms*). The trace, the determinant and the four norms follow (§*The Trace*, §*The Determinant*, §*The Four Norms*), the constants are counted (§*The Factors*), and the two statements that no block can carry are named at the end (§*What the Element Size Gives*).

**The concrete setting.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ on $(e_t,\vec e_x,\vec e_y,\vec e_z)$, with $\vec e_k^2=-e_t$ and $\vec e_x\vec e_y=\vec e_z$, $\vec e_y\vec e_z=\vec e_x$, $\vec e_z\vec e_x=\vec e_y$; the central scalar imaginary is $i$. The left ideal is
$$
S_+=\mathbb{B}\tilde\Pi_+=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_+,
\qquad
\tilde\Pi_+=\tfrac12(e_t+i\vec e_z),\quad\vec\Upsilon_+=\tfrac12(i\vec e_x+\vec e_y),
$$
and in the basis $(\tilde\Pi_+,\vec\Upsilon_+)$ left multiplication by $\tilde Q$ has the matrix
$$
A=\mathsf M_2(\tilde Q)=\begin{pmatrix}P_+&X_-\\X_+&P_-\end{pmatrix},\qquad
P_\pm=Q_t\mp iQ_z,\quad X_\pm=-iQ_x\pm Q_y,
$$
as in §*The Left and Right Matrices* of *$M_2(\mathbb{C})$ Pauli Representation*. Write $A_1$ and $A_2$ for the blocks of $\tilde Q_1$ and $\tilde Q_2$, and $\tilde Q_a=Q_{at}e_t+\vec Q_a$, $B_a^2=Q_{ax}^2+Q_{ay}^2+Q_{az}^2$.

**The result in one line.** The four forms are the four half-traces $\tfrac12\operatorname{Tr}(A_1A_2)$, $\tfrac12\operatorname{Tr}(A_1^{\natural}A_2)$, $\tfrac12\operatorname{Tr}(A_1A_2^{\dagger})$ and $\tfrac12\operatorname{Tr}(A_1^{\natural}A_2^{\dagger})$, where $A^{\natural}=\sigma_2A^{\mathsf T}\sigma_2$ is the adjugate; the antisymmetric parts of the products are traceless; the quaternionic norm is the determinant and also the eigenvalue of $A^{\natural}A$; and on the plane $S_+$ three of the four forms degenerate, so only the Hermitian one is a Gram matrix there.

**Boundaries.** The block, the two ideals and the stitch are *$M_2(\mathbb{C})$ Pauli Representation*; this article takes the block and does not rebuild it. The four general products are *The Four General Products and Their Relations over the Biquaternion Algebra*, and the twelve products are *Symmetric and Antisymmetric Decomposition of the Four General Products*. The four forms and the four norms without matrices are *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*. The same content at the $4\times4$ size is *$M_4(\mathbb{C})$ Pauli Representation : Products, Forms and Norms* and *$M_4(\mathbb{C})$ Axis-Free Representation : Products, Forms and Norms*. The six subspaces are *Subspaces and Decompositions of the Biquaternion Algebra*; the zero-divisor cone is *Zero Divisors and Invertibles in the Biquaternion Algebra*.

## The Element on One Plane

**The block is the element.** The block $A$ has four complex entries and the element has four complex coordinates, so the map is an isomorphism of complex vector spaces. On this plane the multiplication by $\tilde Q$ is the multiplication by $A$, and every statement about one element of the algebra is a statement about its block.

**The block in the Pauli basis.** The four units have the four blocks
$$
\mathsf M_2(e_t)=\mathrm I_2,\qquad
\mathsf M_2(\vec e_x)=-i\sigma_1,\qquad
\mathsf M_2(\vec e_y)=-i\sigma_2,\qquad
\mathsf M_2(\vec e_z)=-i\sigma_3,
$$
so every block is
$$
A=Q_t\mathrm I_2-i\bigl(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3\bigr)=Q_t\mathrm I_2-iW(\tilde Q),\qquad
W(\tilde Q)=Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3 .
$$
The display is the four-unit table of *$M_2(\mathbb{C})$ Pauli Representation* written as one formula.

**The block is a quaternion-like number.** The three Pauli matrices are Hermitian, of square $\mathrm I_2$, pairwise anticommuting, so
$$
W(\tilde Q)^2=(\vec Q,\vec Q)\,\mathrm I_2=B^2\mathrm I_2,\qquad W(\tilde Q^{\natural})=-W(\tilde Q) .
$$
The block is therefore a number of the form $a+cW$ with $W^2=B^2$, and the rules of such numbers apply without any further computation: the conjugate is $a-cW$, the product is $(ab+cdB^2)+(ad+bc)W$, and the norm is $a^2-c^2B^2$. With $a=Q_t$ and $c=-i$ the norm is $Q_t^2+B^2$, the plus sign coming from $c^2=(-i)^2=-1$ and from the minus sign of the rule. This is the whole reason the quaternionic norm is the determinant of the block, and it is the reading of $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong M_2(\mathbb{C})$ on one block.

**The trace and the determinant.** From the display,
$$
\operatorname{Tr}A=2Q_t,\qquad
\det A=Q_t^2+B^2=\langle\tilde Q\rangle_{\natural}=N(\tilde Q),\qquad
\chi_A(\lambda)=\lambda^2-2Q_t\lambda+\langle\tilde Q\rangle_{\natural},
$$
with eigenvalues $Q_t\pm iB$. The trace reads the scalar part and the determinant reads the quaternionic norm; neither sees the direction of the vector part.

## The Three Companions

**The three conjugations, at the element size.**
$$
A^{\natural}:=\mathsf M_2(\tilde Q^{\natural})=\sigma_2A^{\mathsf T}\sigma_2=\operatorname{adj}A,\qquad
A^{c}:=\mathsf M_2(\bar{\tilde Q})=\sigma_2\overline{A}\sigma_2,\qquad
A^{*}:=\mathsf M_2(\tilde Q^{*})=A^{\dagger}.
$$
The first is the adjugate, the second is the congruence of the entrywise conjugate, and the third is the adjoint with no congruence. All three are proved in §*The Stitch Between the Left and the Right* and §*The Adjugate and the Inverse* of *$M_2(\mathbb{C})$ Pauli Representation*, and §*The Two Elements in the Peirce Frame* of *$M_4(\mathbb{C})$ Pauli Representation : Products, Forms and Norms* repeats them at the full size.

**The adjugate.** For a $2\times2$ matrix,
$$
\operatorname{adj}\begin{pmatrix}a&b\\c&d\end{pmatrix}=\begin{pmatrix}d&-b\\-c&a\end{pmatrix},\qquad
\operatorname{adj}A\,A=A\operatorname{adj}A=(\det A)\mathrm I_2,
$$
and the congruence $\sigma_2A^{\mathsf T}\sigma_2$ reproduces the four entries with their signs. The identity is the reason the quaternionic conjugation is the useful one: it is the map $A\mapsto(\det A)A^{-1}$, it exists for every matrix including the singular ones, and it multiplies the eigenvalues by nothing, since $\operatorname{adj}A$ has eigenvalues $\lambda_2$ and $\lambda_1$ when $A$ has $\lambda_1$ and $\lambda_2$. The trace of the adjugate is the trace of $A$ and its determinant is the determinant of $A$.

**What the adjugate buys.** Two statements of §*The Four Norms* and §*The Determinant* become one line each:
$$
A^{\natural}A=N(\tilde Q)\mathrm I_2,\qquad \tfrac12\operatorname{Tr}(A^{\natural}A)=N(\tilde Q),
$$
the first because $\operatorname{adj}A\,A=\det A\,\mathrm I_2$ and $\det A=N$, the second because the trace of a scalar matrix is twice the scalar. The quaternionic norm is therefore the determinant, read as a trace word, and it is also an eigenvalue of $A^{\natural}A$.

**The other two.** The entrywise conjugate costs the congruence $\sigma_2$ because the two Peirce coordinates $P_\pm$ and $X_\pm$ are complex-linear combinations of the coefficients with the imaginary unit in them: conjugating the coefficients does not conjugate the entries. The adjoint costs nothing because the two frame vectors $\tilde\Pi_+$ and $\vec\Upsilon_+$ are orthogonal for the Hermitian form and have the same norm $\tfrac12$, as §*The Stitch Between the Left and the Right* of *$M_2(\mathbb{C})$ Pauli Representation* computes.

**The two compositions.** The three conjugations compose to three words,
$$
(A^{c})^{\natural}=\overline{A}^{\mathsf T},\qquad (A^{\natural})^{c}=\overline{A}^{\mathsf T},\qquad (A^{c})^{*}=\overline{A}^{\dagger},
$$
the first two because the congruence and the conjugation commute and $\sigma_2^2=\mathrm I_2$. The first identity is the one used in the quaternionic sesquilinear split of §*The Symmetric and the Antisymmetric Part*.

## The Product

**The word of a product is the product of the blocks.** For all $\tilde Q_1,\tilde Q_2$,
$$
\mathsf M_2(\tilde Q_1\tilde Q_2)=A_1A_2,\qquad \mathsf M_2(\tilde Q^n)=A^n,\qquad \mathsf M_2(\tilde Q^{-1})=A^{-1},
$$
the last when $N(\tilde Q)\neq0$. The first is the multiplicativity of the block model, which is the statement that the compression is a homomorphism of $\mathbb{B}$ into $M_2(\mathbb{C})$; the two others follow by induction and by the inverse of a product.

**The product is bilinear and associative.** The two identities
$$
\mathsf M_2\bigl((\tilde Q_1+\tilde Q_2)\tilde Q_3\bigr)=(A_1+A_2)A_3,\qquad
\mathsf M_2(\tilde Q_1\tilde Q_2\tilde Q_3)=A_1A_2A_3
$$
are the linearity of the compression and its multiplicativity applied twice. Every word in three elements is therefore a word in three blocks in the same order.

**The trace of a product.** For all $\tilde Q_1,\tilde Q_2$,
$$
\operatorname{Tr}(A_1A_2)=2\bigl(Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2)\bigr)=2P(\tilde Q_1,\tilde Q_2),
$$
by the cyclicity of the trace, the linearity, and $\operatorname{Tr}(W_1W_2)=2(\vec Q_1,\vec Q_2)$, which is the trace of a product of two Pauli combinations. The trace of a product is the plain form up to the factor $2$, and it is not the product of the traces, since that would be $4Q_{1t}Q_{2t}$.

**The product with the transpose.** For all $\tilde Q_1,\tilde Q_2$,
$$
\operatorname{Tr}(A_1A_2^{\mathsf T})=2\mathrm{Sc}\bigl(\tilde Q_1\varrho(\tilde Q_2)\bigr),\qquad \varrho=\operatorname{diag}(1,-1,1,-1),
$$
as §*The Product* of *$M_2(\mathbb{C})$ Pauli Representation* computes. The reflection $\varrho$ is not the quaternion conjugation and not the identity, and the value is not $2P$ and not $2N$. This is the element-size shadow of the missing mixed trace: at the $4\times4$ size the same product of the two families gives $4Q_{1t}Q_{2t}$, and one block cannot separate the two tensor factors that produce it.

**The two sides do not commute.** At this size the left action lives on $S_+$ and the right action on $T_+$, two different planes, so no statement $A_1A_2^{\mathsf T}=A_2^{\mathsf T}A_1$ holds and none is expected. The companion article exhibits the failure on $\vec\Upsilon_+$. At the $4\times4$ size the two actions live on one space and commute, and the difference is the content of §*What the Element Size Gives*.

## The Symmetric and the Antisymmetric Part

**The two exchanges.** The bilinear products are split by the interchange of the arguments and the sesquilinear ones by the interchange followed by the coefficientwise conjugation of the value,
$$
f^{\mathrm{s}}=\tfrac12\bigl(f(\tilde Q_1,\tilde Q_2)+f(\tilde Q_2,\tilde Q_1)\bigr),\qquad
g^{\mathrm{s}}=\tfrac12\bigl(g(\tilde Q_1,\tilde Q_2)+\overline{g(\tilde Q_2,\tilde Q_1)}\bigr),
$$
with the antisymmetric parts defined by the differences, as in *Symmetric and Antisymmetric Decomposition of the Four General Products*.

**The plain bilinear split.** For all $\tilde Q_1,\tilde Q_2$,
$$
\mathsf M_2(\tilde Q_1\bullet\tilde Q_2)=\tfrac12(A_1A_2+A_2A_1),\qquad
\mathsf M_2(\tilde Q_1\wedge\tilde Q_2)=\tfrac12(A_1A_2-A_2A_1),
$$
and the two add up to $A_1A_2$. The words are the anticommutator and the commutator of the two blocks, and this is the only one of the four splits that is written with no matrix other than $A_1$ and $A_2$.

**The plain antisymmetric part is a cross product.** By the expansion in the scalar and the vector parts,
$$
\tilde Q_1\bullet\tilde Q_2=(Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2))+(Q_{1t}\vec Q_2+Q_{2t}\vec Q_1),\qquad
\tilde Q_1\wedge\tilde Q_2=\vec Q_1\times\vec Q_2,
$$
so the antisymmetric part is a pure vector and its block is traceless. At the block level the same statement reads
$$
\operatorname{Tr}\tfrac12(A_1A_2-A_2A_1)=0,\qquad
\det\tfrac12(A_1A_2-A_2A_1)=(\vec Q_1\times\vec Q_2,\vec Q_1\times\vec Q_2),
$$
the second because the commutator is the block of the pure vector $\vec Q_1\times\vec Q_2$, whose block is $-iW$ with $W^2$ the dot square and whose determinant is the quaternionic norm of that vector.

**The quaternionic bilinear split.** With the first slot read through the adjugate,
$$
\mathsf M_2(\tilde Q_1\bullet_{\natural}\tilde Q_2)=\tfrac12\bigl(A_1^{\natural}A_2+A_2^{\natural}A_1\bigr)=N(\tilde Q_1,\tilde Q_2)\,\mathrm I_2,
$$
$$
\mathsf M_2(\tilde Q_1\wedge_{\natural}\tilde Q_2)=\tfrac12\bigl(A_1^{\natural}A_2-A_2^{\natural}A_1\bigr)=\tfrac12\bigl(\operatorname{adj}A_1\,A_2-\operatorname{adj}A_2\,A_1\bigr).
$$
The symmetric part collapses to a scalar matrix. The identity is the element identity $\tfrac12(\tilde Q_1^{\natural}\tilde Q_2+\tilde Q_2^{\natural}\tilde Q_1)=N(\tilde Q_1,\tilde Q_2)e_t$ read through $\mathsf M_2$: the two vector parts enter with opposite signs and cancel, and the two scalar parts add. The antisymmetric part is not a commutator of the two blocks, because $\operatorname{adj}A_1$ is not $A_1$; it is traceless for the reason the symmetric part is scalar.

**The plain sesquilinear split.** With the two terms of the exchange,
$$
\mathsf M_2(\tilde Q_1\bullet_*\tilde Q_2)=\tfrac12\bigl(A_1A_2^{\dagger}+\sigma_2\overline{A_2}A_1^{\mathsf T}\sigma_2\bigr),\qquad
\mathsf M_2(\tilde Q_1\wedge_*\tilde Q_2)=\tfrac12\bigl(A_1A_2^{\dagger}-\sigma_2\overline{A_2}A_1^{\mathsf T}\sigma_2\bigr),
$$
the first term being the block of $\tilde Q_1\tilde Q_2^{*}$ and the second the block of $\overline{\tilde Q_2\tilde Q_1^{*}}=\bar{\tilde Q}_2\tilde Q_1^{\natural}$, whose block is $A_2^{c}A_1^{\natural}=\sigma_2\overline{A_2}A_1^{\mathsf T}\sigma_2$ because $\sigma_2^2=\mathrm I_2$ cancels the two inner factors.

**The quaternionic sesquilinear split.** The same with both slots of the first product conjugated,
$$
\mathsf M_2(\tilde Q_1\bullet_{\natural*}\tilde Q_2)=\tfrac12\bigl(A_1^{\natural}A_2^{\dagger}+\overline{A_2}^{\mathsf T}A_1^{\natural}\bigr),\qquad
\mathsf M_2(\tilde Q_1\wedge_{\natural*}\tilde Q_2)=\tfrac12\bigl(A_1^{\natural}A_2^{\dagger}-\overline{A_2}^{\mathsf T}A_1^{\natural}\bigr),
$$
the second term simplifying because $(A_2^{c})^{\natural}=\overline{A_2}^{\mathsf T}$.

**The trace splits cleanly.** For each of the four products,
$$
\operatorname{Tr}\mathsf M_2(f^{\mathrm{a}}(\tilde Q_1,\tilde Q_2))=0,\qquad
\operatorname{Tr}\mathsf M_2(f^{\mathrm{s}}(\tilde Q_1,\tilde Q_2))=\operatorname{Tr}\mathsf M_2(f(\tilde Q_1,\tilde Q_2)),
$$
the first because the antisymmetric parts have zero scalar part and the trace is twice the scalar part, the second by subtraction. The four forms of §*The Four Forms* are therefore forms on the symmetrised products, and the antisymmetric four carry none.

**The equal-argument case.** At $\tilde Q_1=\tilde Q_2=\tilde Q$ the bilinear antisymmetric parts vanish and the square is the symmetric part alone. The sesquilinear antisymmetric part does not vanish there: it is the coefficientwise imaginary part of $A A^{\dagger}$, of zero trace and of nonzero traceless part as soon as $AA^{\dagger}$ is not fixed by the coefficient conjugation. At $A=\mathrm I_2$ it vanishes; at $A=\sigma_1$ it does not.

## The Twelve Products

**The table.** Each row is one product, its block, and its trace. The trace column is the $2\times2$ one; the $4\times4$ article has the same column with every entry doubled.

| Product | Block | Trace |
|---|---|---|
| $\tilde Q_1\tilde Q_2$ | $A_1A_2$ | $2P$ |
| $\tilde Q_1^{\natural}\tilde Q_2$ | $A_1^{\natural}A_2$ | $2N$ |
| $\tilde Q_1\tilde Q_2^{*}$ | $A_1A_2^{\dagger}$ | $2H$ |
| $\tilde Q_1^{\natural}\tilde Q_2^{*}$ | $A_1^{\natural}A_2^{\dagger}$ | $2\mathrm{Kr}$ |
| $\tilde Q_1\bullet\tilde Q_2$ | $\tfrac12(A_1A_2+A_2A_1)$ | $2P$ |
| $\tilde Q_1\bullet_{\natural}\tilde Q_2$ | $\tfrac12(A_1^{\natural}A_2+A_2^{\natural}A_1)=N\mathrm I_2$ | $2N$ |
| $\tilde Q_1\bullet_*\tilde Q_2$ | $\tfrac12(A_1A_2^{\dagger}+\sigma_2\overline{A_2}A_1^{\mathsf T}\sigma_2)$ | $2H$ |
| $\tilde Q_1\bullet_{\natural*}\tilde Q_2$ | $\tfrac12(A_1^{\natural}A_2^{\dagger}+\overline{A_2}^{\mathsf T}A_1^{\natural})$ | $2\mathrm{Kr}$ |
| $\tilde Q_1\wedge\tilde Q_2$ | $\tfrac12(A_1A_2-A_2A_1)$ | $0$ |
| $\tilde Q_1\wedge_{\natural}\tilde Q_2$ | $\tfrac12(A_1^{\natural}A_2-A_2^{\natural}A_1)$ | $0$ |
| $\tilde Q_1\wedge_*\tilde Q_2$ | $\tfrac12(A_1A_2^{\dagger}-\sigma_2\overline{A_2}A_1^{\mathsf T}\sigma_2)$ | $0$ |
| $\tilde Q_1\wedge_{\natural*}\tilde Q_2$ | $\tfrac12(A_1^{\natural}A_2^{\dagger}-\overline{A_2}^{\mathsf T}A_1^{\natural})$ | $0$ |

**What the table shows.** Eight rows repeat the four forms and four rows vanish under the trace. Four rows carry no matrix other than $A_1$ and $A_2$: the plain product, its two halves, and the plain sesquilinear product. Eight carry either $\operatorname{adj}A$ or $\sigma_2\overline{A}\sigma_2$, and those eight are exactly the rows whose first or second slot is conjugated.

**The one scalar row.** The symmetric quaternionic product is the only row whose matrix is a scalar multiple of the identity. Its trace, $2N$, is the trace of $N\mathrm I_2$, and the identity is stronger than the trace identity: the whole matrix is the form. The single-element version is $A^{\natural}A=N(\tilde Q)\mathrm I_2$ of §*The Three Companions*.

## The Four Forms

**The four words.** The scalar part of an element is half the trace of its block,
$$
\operatorname{Sc}\tilde X=\tfrac12\operatorname{Tr}\mathsf M_2(\tilde X),
$$
because the trace is $2Q_t$. Applying the identity to the four products gives the four forms,
$$
P=\tfrac12\operatorname{Tr}(A_1A_2),\qquad
N=\tfrac12\operatorname{Tr}(A_1^{\natural}A_2),\qquad
H=\tfrac12\operatorname{Tr}(A_1A_2^{\dagger}),\qquad
\mathrm{Kr}=\tfrac12\operatorname{Tr}(A_1^{\natural}A_2^{\dagger}),
$$
with the letters and the names of *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*. The first two are bilinear and the last two sesquilinear; the adjugate appears in the two quaternionic rows and the dagger in the two sesquilinear ones.

**The words in the Pauli display.** Substituting $A=Q_t\mathrm I_2-iW$ and $\operatorname{adj}A=Q_t\mathrm I_2+iW$ gives the four forms as traces of Pauli combinations,
$$
P=\tfrac12\operatorname{Tr}\bigl((Q_{1t}\mathrm I_2-iW_1)(Q_{2t}\mathrm I_2-iW_2)\bigr),\qquad
N=\tfrac12\operatorname{Tr}\bigl((Q_{1t}\mathrm I_2+iW_1)(Q_{2t}\mathrm I_2-iW_2)\bigr),
$$
$$
H=\tfrac12\operatorname{Tr}\bigl((Q_{1t}\mathrm I_2-iW_1)(\overline{Q_{2t}}\mathrm I_2+iW_2^{\dagger})\bigr),\qquad
\mathrm{Kr}=\tfrac12\operatorname{Tr}\bigl((Q_{1t}\mathrm I_2+iW_1)(\overline{Q_{2t}}\mathrm I_2+iW_2^{\dagger})\bigr),
$$
and the four reduce to the four coordinate expressions $Q_{1t}Q_{2t}\mp(\vec Q_1,\vec Q_2)$ and their conjugates by $\operatorname{Tr}W_1W_2=2(\vec Q_1,\vec Q_2)$ and $\operatorname{Tr}\mathrm I_2=2$. The signs of the four rows are the four ways of signing the vector part, which is the content of the table of *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*, read as a trace.

**The four Gram matrices on the plane.** The Gram matrix of a form in the basis $(\tilde\Pi_+,\vec\Upsilon_+)$ is the array of its values on the two vectors, and the four arrays are
$$
[P]_{S_+}=\begin{pmatrix}\tfrac12&0\\0&0\end{pmatrix},\qquad
[N]_{S_+}=\begin{pmatrix}0&0\\0&0\end{pmatrix},\qquad
[H]_{S_+}=\begin{pmatrix}\tfrac12&0\\0&\tfrac12\end{pmatrix},\qquad
[\mathrm{Kr}]_{S_+}=\begin{pmatrix}0&0\\0&-\tfrac12\end{pmatrix}.
$$
They are computed from the four words on the two vectors, or equivalently as the top-left blocks of the four Gram matrices of the $4\times4$ article.

**Three of the four degenerate on the plane.** The plain form vanishes on $\vec\Upsilon_+$, the quaternionic form vanishes on both vectors, and the Krein form vanishes on $\tilde\Pi_+$. The reason is the coordinates of the two frame vectors: $\tilde\Pi_+$ has $Q_t=\tfrac12$ and $Q_z=\tfrac i2$, and $\vec\Upsilon_+$ has $Q_x=\tfrac i2$ and $Q_y=\tfrac12$. Then $P(\vec\Upsilon_+)=0-(\tfrac i2)^2-(\tfrac12)^2=0$, while $N(\tilde\Pi_+)=\tfrac14+(\tfrac i2)^2=0$ and $N(\vec\Upsilon_+)=(\tfrac i2)^2+(\tfrac12)^2=0$. Both frame vectors are therefore null for the quaternionic form, the first through the scalar part and the second through the vector part, and $\mathrm{Kr}(\tilde\Pi_+)=\tfrac14-\tfrac14=0$ with $\mathrm{Kr}(\vec\Upsilon_+)=-\tfrac14-\tfrac14=-\tfrac12$.

**What that means.** The plane $S_+$ carries one non-degenerate form, the Hermitian one, and it carries it as the scalar $\tfrac12$ times the identity. The other three are read on the plane as trace words of block products, not as Gram matrices of a form on the plane. This is the sharp form of the statement that the block is the compression of the action and not a representation of the forms: a form on the algebra needs two elements, and one plane holds one of the two, so three of the four restrictions degenerate.

**The Hermitian form is the plane's own form.** On $S_+$,
$$
H(\tilde Q_1,\tilde Q_2)=\tfrac12\operatorname{Tr}(A_1A_2^{\dagger})=\tfrac12\langle A_1,A_2\rangle_{\mathrm{HS}},
$$
which is the Hermitian inner product of the two blocks, positive definite on the plane. The identity is the Hilbert–Schmidt inner product divided by two, and the two frame vectors have norm $\tfrac12$ and are orthogonal, which is the display $[H]_{S_+}=\tfrac12\mathrm I_2$.

**The form sees the symmetric part.** For each of the four products,
$$
\operatorname{Sc}f(\tilde Q_1,\tilde Q_2)=\operatorname{Sc}f^{\mathrm{s}}(\tilde Q_1,\tilde Q_2),\qquad
\operatorname{Sc}f^{\mathrm{a}}(\tilde Q_1,\tilde Q_2)=0,
$$
so the four upper rows of §*The Twelve Products* repeat the four forms and the four lower rows carry none of them. The matrix reading is the tracelessness of the four antisymmetric words.

## The Trace

**The trace of one block.** For every $\tilde Q$,
$$
\operatorname{Tr}A=2Q_t,\qquad \operatorname{Tr}A^{\natural}=\operatorname{Tr}A,\qquad \operatorname{Tr}A^{\dagger}=\overline{\operatorname{Tr}A},
$$
the first because the two diagonal entries are $Q_t-iQ_z$ and $Q_t+iQ_z$, the second because the adjugate has the same trace, the third by the definition of the adjoint.

**The trace of a word of two.** The four products have the four traces
$$
\operatorname{Tr}(A_1A_2)=2P,\qquad \operatorname{Tr}(A_1^{\natural}A_2)=2N,\qquad
\operatorname{Tr}(A_1A_2^{\dagger})=2H,\qquad \operatorname{Tr}(A_1^{\natural}A_2^{\dagger})=2\mathrm{Kr},
$$
each twice the corresponding form. The identities are the four words of §*The Four Forms* multiplied by two, and the factor is the dimension of the plane.

**The trace is not multiplicative.** The two sides are $2(Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2))$ and $4Q_{1t}Q_{2t}$, and they differ by $2(3Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2))$. The trace of the identity is $2$ and not $1$, so no choice of frame and no normalisation of the block repairs the failure; only the determinant, which is normalised at the identity, multiplies.

**The trace does not commute with the square.** For the plain and the quaternionic rows,
$$
\operatorname{Tr}(A_1A_2)\operatorname{Tr}(A_2A_1)=4P(\tilde Q_1,\tilde Q_2)^2,\qquad
\operatorname{Tr}(A_1A_2A_1A_2)\neq4P(\tilde Q_1,\tilde Q_2)^2,
$$
the second being the trace of the matrix of $(\tilde Q_1\tilde Q_2)^2$. The gap is $2P(\tilde Q_1\tilde Q_2)-4P(\tilde Q_1,\tilde Q_2)^2$, a variant of the defect of the plain norm of §*The Four Norms*: the plain norm fails multiplicativity by $P(\tilde Q_1\tilde Q_2)-P(\tilde Q_1)P(\tilde Q_2)$, and here the second term is squared and the first is not.

**What the trace cannot see.** The trace sees $Q_t$ of an element and the symmetric part of a product. It sees neither the direction of the vector part of an element nor any of the four antisymmetric products. The four zeros of §*The Twelve Products* and the identity $\operatorname{Tr}A=2Q_t$ are the two statements of this blindness.

## The Determinant

**The determinant of one block.** For every $\tilde Q$,
$$
\det A=Q_t^2+B^2=N(\tilde Q),\qquad \chi_A(\lambda)=\lambda^2-2Q_t\lambda+N(\tilde Q),
$$
with eigenvalues $Q_t\pm iB$. The determinant is the quaternionic norm, and the characteristic polynomial is the one of *$M_2(\mathbb{C})$ Pauli Representation*, of roots the two eigenvalues of the block.

**The determinant is the trace of the adjugate product.** From $\operatorname{adj}A\,A=(\det A)\mathrm I_2$,
$$
\tfrac12\operatorname{Tr}(A^{\natural}A)=\tfrac12\operatorname{Tr}\bigl((\det A)\mathrm I_2\bigr)=\det A=N(\tilde Q),
$$
which is the statement that the quaternionic form on the diagonal is the determinant. The computation is one line, and it identifies the third of the four norms with the determinant of the block; the $4\times4$ article needs the square for the same identification, because there the block is repeated.

**The determinant of a product of matrices.** For all $\tilde Q_1,\tilde Q_2$,
$$
\det(A_1A_2)=\det A_1\det A_2,\qquad\text{that is}\qquad N(\tilde Q_1\tilde Q_2)=N(\tilde Q_1)N(\tilde Q_2).
$$
The identity is the multiplicativity of the determinant of matrices, and the reading on the right is the multiplicativity of the quaternionic norm, which is the only multiplicative norm of the four. At this size the statement is exact and not up to sign, because one block is the element.

**The determinant of the other rows.** With $\det\operatorname{adj}A=\det A$, $\det A^{\mathsf T}=\det A$ and $\det A^{\dagger}=\overline{\det A}$,
$$
\det(A_1^{\natural}A_2)=N(\tilde Q_1)N(\tilde Q_2),\qquad
\det(A_1A_2^{\dagger})=\det(A_1^{\natural}A_2^{\dagger})=N(\tilde Q_1)\overline{N(\tilde Q_2)} .
$$
The last two pair the determinant with its conjugate, so the two sesquilinear rows are conjugate-multiplicative. This is the element-size form of the same statement in the $4\times4$ articles.

**The rank.** The block has rank $2$ when $N(\tilde Q)\neq0$, rank $1$ when $N(\tilde Q)=0$ and $A\neq0$, and rank $0$ when $A=0$. The middle case is the zero-divisor cone of *Zero Divisors and Invertibles in the Biquaternion Algebra*: the block is a nonzero matrix of zero determinant, so its two columns are dependent, and the element is a zero divisor, whose two one-sided annihilators are planes and whose two-sided annihilator is the line $\mathbb{C}\tilde Q^{\natural}$.

**The determinant is the only quadratic word that factors.** Of the four quadratic words $\tfrac12\operatorname{Tr}(A^2)$, $\det A$, $\tfrac12\operatorname{Tr}(A^{\dagger}A)$ and $\tfrac12\operatorname{Tr}(A^{\natural}A^{\dagger})$, only $\det A$ is multiplicative across a product with no conjugation, and it is also the second of the four. The plain word does not factor and its defect is computed in §*The Four Norms*.

## The Four Norms

**The four words at two equal arguments.**
$$
P=\tfrac12\operatorname{Tr}(A^2),\qquad N=\tfrac12\operatorname{Tr}(A^{\natural}A)=\det A,\qquad
H=\tfrac12\operatorname{Tr}(A^{\dagger}A),\qquad \mathrm{Kr}=\tfrac12\operatorname{Tr}(A^{\natural}A^{\dagger}).
$$
The four letters, the four coordinate expressions and the four inertias are those of *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*. Each word is the half-trace of a product of the block with one of its three companions.

**The plain norm.** From $A=Q_t\mathrm I_2-iW$ with $W^2=B^2\mathrm I_2$,
$$
A^2=(Q_t^2-B^2)\mathrm I_2-2iQ_tW,\qquad
P(\tilde Q)=\tfrac12\operatorname{Tr}(A^2)=Q_t^2-B^2,
$$
so the plain norm is the trace half of a matrix which is not scalar, and the traceless part $-2iQ_tW$ is the obstruction. It is indefinite on the real algebra and it is not multiplicative.

**The quaternionic norm.** The same display with the adjugate,
$$
A^{\natural}=Q_t\mathrm I_2+iW,\qquad
A^{\natural}A=(Q_t^2+B^2)\mathrm I_2=N(\tilde Q)\mathrm I_2,\qquad
N(\tilde Q)=\det A,
$$
so the quaternionic norm is at once the determinant, the eigenvalue of $A^{\natural}A$, and the value of the second form on the diagonal. It is the only one of the four that is a scalar matrix, and it is the only one that is multiplicative.

**The Hermitian norm.** Since $\operatorname{Tr}(A^{\dagger}A)=\sum_{ij}|A_{ij}|^2$,
$$
H(\tilde Q)=\tfrac12\operatorname{Tr}(A^{\dagger}A)=\tfrac12\lVert A\rVert^2_{\mathrm{HS}}=\sum_\mu|Q_\mu|^2,
$$
the last equality because the four matrices $\mathrm I_2$, $-i\sigma_1$, $-i\sigma_2$, $-i\sigma_3$ are orthogonal for the Hilbert–Schmidt product and of square norm $2$ each. It is positive definite, of inertia $(8,0)$ on the real algebra, and it is not multiplicative.

**The Krein norm.** The fourth word pairs the adjugate with the adjoint,
$$
\mathrm{Kr}(\tilde Q)=\tfrac12\operatorname{Tr}(A^{\natural}A^{\dagger})=\sum_\mu\varepsilon_\mu|Q_\mu|^2,\qquad \varepsilon_t=1,\quad\varepsilon_x=\varepsilon_y=\varepsilon_z=-1,
$$
of inertia $(2,6)$ on the real algebra. It is the Hermitian norm with the sign of the vector part reversed, and like the plain norm it is neither definite nor multiplicative.

**The multiplicativity table.**

| Norm | Word | Multiplicative | Definite | Value ring |
|---|---|---|---|---|
| $P$ | $\tfrac12\operatorname{Tr}(A^2)$ | no | no | $\mathbb{C}$ |
| $N$ | $\tfrac12\operatorname{Tr}(A^{\natural}A)=\det A$ | yes | no | $\mathbb{C}$ |
| $H$ | $\tfrac12\operatorname{Tr}(A^{\dagger}A)$ | no | yes | $\mathbb{R}$ |
| $\mathrm{Kr}$ | $\tfrac12\operatorname{Tr}(A^{\natural}A^{\dagger})$ | no | no | $\mathbb{R}$ |

**The defect of the plain norm.** Write $\tilde Q_a=s_a+\vec Q_a$ with $s_a=Q_{at}$. Then
$$
P(\tilde Q_1\tilde Q_2)-P(\tilde Q_1)P(\tilde Q_2)
=-2(\vec Q_1\times\vec Q_2,\vec Q_1\times\vec Q_2)-4s_1s_2(\vec Q_1,\vec Q_2),
$$
by the expansion of the two squares in the scalar and the vector parts. The defect is minus twice the square of the cross product, minus four times the two scalar parts times the dot product; the first term is minus twice the norm of the antisymmetric part, and the second vanishes when either element is a pure vector.

**The two other defects, by witness.** The Hermitian norm fails on $\vec e_x+i\vec e_y$, of block
$$
A=\begin{pmatrix}0&-2i\\0&0\end{pmatrix},\qquad \det A=0,\qquad H(\tilde Q)=2,
$$
so $H(\tilde Q^2)=0\neq H(\tilde Q)^2$. The Krein norm fails on $e_t+\vec e_x$, of block
$$
A=\begin{pmatrix}1&-i\\-i&1\end{pmatrix},\qquad \det A=2,\qquad \mathrm{Kr}(\tilde Q)=0,
$$
and a multiplicative $\mathrm{Kr}$ would give $\mathrm{Kr}(e_t)=\mathrm{Kr}(\tilde Q)\mathrm{Kr}(\tilde Q^{-1})=0$ against $\mathrm{Kr}(e_t)=1$. The first witness is a zero divisor, as the vanishing of $N$ requires; the second is invertible, which is what makes the Krein defect a defect and not a coincidence.

**Why only the quaternionic word collapses.** The product $A^{\natural}A$ is scalar because $\operatorname{adj}A$ is the cofactor matrix of $A$ and the cofactor identity is $(\operatorname{adj}A)A=(\det A)\mathrm I_2$. The other three words contain $A$ itself, $A^{\dagger}$ and $A^{\natural}A^{\dagger}$, and none of the three has a cofactor identity. The frame's contribution is that the adjugate here is the congruence $\sigma_2A^{\mathsf T}\sigma_2$, so the collapse is written with the transpose of the block and one Pauli matrix.

## The Factors

**One factor.** Every trace identity of this article carries the factor $\tfrac12$ or $2$, and both are the trace of the two-dimensional identity:
$$
\operatorname{Tr}\mathrm I_2=2,\qquad \operatorname{Sc}\tilde X=\tfrac12\operatorname{Tr}A .
$$

| Quantity | Word | Factor |
|---|---|---|
| scalar part | $\tfrac12\operatorname{Tr}A$ | $1/2$ |
| trace of an element | $2Q_t$ | $2$ |
| form | $\tfrac12\operatorname{Tr}(A_1A_2)$ | $1/2$ |
| norm | $\tfrac12\operatorname{Tr}(A^{\natural}A)$ | $1/2$ |
| the determinant of the image | $\det A$ | no factor |
| determinant of the identity | $\det\mathrm I_2=1$ | no factor |

**Against the two other sizes.** At the $4\times4$ size the same identities carry $4$ and $\tfrac14$, and at this size $2$ and $\tfrac12$. The ratio is the trace of the identity of the carrier, which is the dimension of the space the matrices act on: four for the algebra and two for the plane. The determinant carries no factor at any size, because it is normalised at the identity of each size.

**The square root of the $4\times4$ statement.** Every identity of *$M_4(\mathbb{C})$ Pauli Representation : Products, Forms and Norms* halves under the compression and every determinant takes its square root. The two sizes are read side by side below.

| Quantity | $4\times4$ | One block |
|---|---|---|
| trace of an element | $4Q_t$ | $2Q_t$ |
| form | $\tfrac14\operatorname{Tr}(L_1L_2)$ | $\tfrac12\operatorname{Tr}(A_1A_2)$ |
| the determinant of the image | $N^2$ | $N$ |
| rank | $0,2,4$ | $0,1,2$ |

and the pattern is the same in each row: the trace halves, the determinant takes the square root, and the rank halves.

## What the Element Size Gives

**What is gained.** The block is the element, so the determinant is the quaternionic norm without a square, the norm is an eigenvalue, the conjugation is the adjugate, and four of the twelve words are the plain operations of $M_2(\mathbb{C})$. The four forms are half-traces of products of the block with the block, the adjugate, the adjoint and the adjugate of the adjoint, and no tensor factor intervenes.

**What is lost, and why.** Two statements of the $4\times4$ size have no block version. The mixed trace $\operatorname{Tr}(L_1R_2)=4Q_{1t}Q_{2t}$ is a statement about the two tensor factors at once, and one block keeps only one of them: the closest block statement is $\operatorname{Tr}(A_1A_2^{\mathsf T})=2\mathrm{Sc}(\tilde Q_1\varrho(\tilde Q_2))$, which is a different number. The commutation $L_1R_2=R_2L_1$ is the same kind of statement, and the two actions at this size live on two different planes, so there is nothing to commute. Both are named in §*The Compression and the Switch* of *$M_2(\mathbb{C})$ Pauli Representation*.

**What is neither gained nor lost.** The four forms, the four norms, the twelve products, the trace and the determinant are the same numbers at the two sizes up to the factor of the trace of the identity. The comparison is a check: an identity of this article multiplied by the appropriate power of $2$ is the identity of the $4\times4$ article, and the four Gram matrices of §*The Four Forms* are the top-left blocks of the four Gram matrices there.

**The three frames in one sentence each.** At the element size the twelve words are $2\times2$ words in the block and its adjugate, the four forms are half-traces, and the factor is $\tfrac12$; at the $4\times4$ size the same words are $\mathrm I_2$ times the same blocks, the factor is $\tfrac14$, and two statements about the two tensor factors appear that no block can hold; in the axis-free frame the same words are $4\times4$ words in the matrix and its transpose, with no congruence and no tensor factor.

## Summary

The four forms are the four half-traces $\tfrac12\operatorname{Tr}(A_1A_2)$, $\tfrac12\operatorname{Tr}(A_1^{\natural}A_2)$, $\tfrac12\operatorname{Tr}(A_1A_2^{\dagger})$ and $\tfrac12\operatorname{Tr}(A_1^{\natural}A_2^{\dagger})$; the plain product is $A_1A_2$, its symmetric part the anticommutator and its antisymmetric part the commutator; the four antisymmetric parts are traceless, so the trace and the four forms see the four products and their symmetrisations and nothing of the four antisymmetrisations. The quaternionic symmetric part is the form times the identity, $\tfrac12(A_1^{\natural}A_2+A_2^{\natural}A_1)=N(\tilde Q_1,\tilde Q_2)\mathrm I_2$.

The block has three companions and they are not of one kind: the quaternion conjugation is the adjugate $\sigma_2A^{\mathsf T}\sigma_2$, the coefficient conjugation is the congruence $\sigma_2\overline{A}\sigma_2$, and the Hermitian conjugation is the adjoint $A^{\dagger}$ with no congruence. The adjugate is what makes the quaternionic row scalar, since $\operatorname{adj}A\,A=(\det A)\mathrm I_2$; and with $\det A=N(\tilde Q)$ it makes the quaternionic norm the determinant, of word $\tfrac12\operatorname{Tr}(A^{\natural}A)=\det A$.

The determinant is the only quadratic word that factors, and at this size it factors exactly, $N(\tilde Q_1\tilde Q_2)=N(\tilde Q_1)N(\tilde Q_2)$, without the square that the $4\times4$ article needs. The other three norms fail, the Hermitian one on a zero divisor and the Krein one on an invertible element, and the plain one fails by minus twice the square of the antisymmetric part plus a scalar-vector cross term.

The plane carries one non-degenerate form and three degenerate restrictions: $[H]_{S_+}=\tfrac12\mathrm I_2$ while the plain, the quaternionic and the Krein restrictions have zero eigenvalues. The factor $\tfrac12$ of every word is $1/\dim S_+$, the determinants carry no factor, and the two statements of the $4\times4$ size that no block can hold are the mixed trace and the commutation of the two families.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S_+$ | the left ideal $\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_+$, the plane of the block |
| $A_a$ | $\mathsf M_2(\tilde Q_a)$, the block of $\tilde Q_a$, $a=1,2$ |
| $A_a^{\natural}$ | $\sigma_2A_a^{\mathsf T}\sigma_2=\operatorname{adj}A_a$, the quaternion conjugate |
| $A_a^{c}$ | $\sigma_2\overline{A_a}\sigma_2$, the coefficient conjugate |
| $A_a^{*}$ | $A_a^{\dagger}$, the Hermitian conjugate |
| $P_\pm$, $X_\pm$ | $Q_t\mp iQ_z$ and $-iQ_x\pm Q_y$, the four Peirce coordinates |
| $\sigma_k$ | the three Pauli matrices, of square $\mathrm I_2$ and pairwise anticommuting |
| $W(\tilde Q)$ | $Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3$, of square $B^2\mathrm I_2$ |
| $\varrho$ | $\operatorname{diag}(1,-1,1,-1)$, the reflection of the mixed trace |
| $\tilde Q_1\bullet\tilde Q_2$, $\tilde Q_1\wedge\tilde Q_2$ | the symmetric and antisymmetric plain bilinear products |
| $\tilde Q_1\bullet_{\natural}\tilde Q_2$, $\tilde Q_1\wedge_{\natural}\tilde Q_2$ | the quaternionic bilinear pair, the first a scalar equal to $N$ |
| $\tilde Q_1\bullet_*\tilde Q_2$, $\tilde Q_1\wedge_*\tilde Q_2$ | the plain sesquilinear pair |
| $\tilde Q_1\bullet_{\natural*}\tilde Q_2$, $\tilde Q_1\wedge_{\natural*}\tilde Q_2$ | the quaternionic sesquilinear pair |
| $P$, $N$, $H$, $\mathrm{Kr}$ | the plain, quaternionic, Hermitian and Krein forms and norms |
| $[\,\cdot\,]_{S_+}$ | the Gram matrix of a form in the basis $(\tilde\Pi_+,\vec\Upsilon_+)$ |

## Further Reading

- [$M_2(\mathbb{C})$ Pauli Representation](m2c-pauli-representation.html), for the block, the two ideals, the stitch and the adjugate.
- [$M_4(\mathbb{C})$ Pauli Representation : Products, Forms and Norms](m4c-pauli-representation-products-forms-norms.html), for the same content with the two tensor factors separated.
- [$M_4(\mathbb{C})$ Axis-Free Representation : Products, Forms and Norms](m4c-axis-free-representation-products-forms-norms.html), for the same content in the coefficient basis, where the transpose is the conjugation.
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the four forms and the four norms without matrices.
- [Symmetric and Antisymmetric Decomposition of the Four General Products](symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html), for the two exchanges and the twelve products.
- [The Four General Products and Their Relations over the Biquaternion Algebra](the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html), for the four products.
- [Zero Divisors and Invertibles in the Biquaternion Algebra](zero-divisors-and-invertibles.html), for the cone $\langle\tilde Q\rangle_{\natural}=0$ and the three ranks.
- [Subspaces and Decompositions of the Biquaternion Algebra](subspaces-and-decompositions-of-the-biquaternion-algebra.html), for the six subspaces.
- [The Biquaternion Algebra](the-biquaternion-algebra.html), for the algebra and the multiplication table.
