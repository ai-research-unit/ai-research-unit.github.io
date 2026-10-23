# __The Eigenvalue Decomposition with respect to a Degree-2 Form__

## Introduction

A **sesqualgebra with a form** is a unital associative algebra $A$ over a field $F$ with an involution $\varsigma$, a $\varsigma$-semilinear involution $*$, and a Hermitian form $h$ tied to the product by the compatibility

$$
h(xy,z)=h(y,x^{*}z).
$$

The form is the **degree-2 datum** of the category: it is the quadratic structure $q(x)=h(x,x)$ read on the algebra, and it is the structure with respect to which the left multiplications are adjoint. This article reads the **eigenvalue decomposition** of a Hermitian element $a=a^{*}$ through that datum. The element has the Hermitian spectral resolution

$$
a=\sum_{i=1}^{r}\lambda_{i}e_{i}
$$

of *The Eigenvalue Decomposition of a Hermitian Element*, with $\lambda_{i}\in F_{0}=F^{\varsigma}$ and $e_{i}$ Hermitian idempotents. The form adds three statements: the eigenprojectors are pairwise orthogonal, the eigenspaces are the left ideals $Ae_{i}$ and are pairwise orthogonal and non-degenerate, and the eigenvalues are the Rayleigh quotients of $a$ on those eigenspaces. The first two are the form-level content of the resolution; the third is the formula that recovers the eigenvalue from the form.

The compatibility is from *Sesqualgebras with a Form*, §*The Object*; the radical and its one-sided ideal property are from that article, §*The Radical Is an Ideal*; the Hermitian idempotents and the Peirce decomposition are *Hermitian Idempotents and the Peirce Decomposition*; the Hermitian spectral resolution is *The Eigenvalue Decomposition of a Hermitian Element*; the Jordan spectral theorem behind it is *The Eigenvalue Decomposition in a Jordan Algebra*; the form-theoretic orthogonality of the idempotents is the subject of the present article; and the positive definite case is the Hilbert-space spectral theorem of Part II.

## The Setting

### The Form and the Adjoint

Let $F$ be a field of characteristic not two, $\varsigma$ an involution of $F$, $F_{0}=F^{\varsigma}$, $A$ a finite-dimensional unital associative $F$-algebra, $*$ a $\varsigma$-semilinear involution, and $h:A\times A\to F$ a Hermitian form satisfying

$$
h(xy,z)=h(y,x^{*}z), \qquad h(x,yz)=h(y^{*}x,z).
$$

The two identities are equivalent, by *Sesqualgebras with a Form*, §*The Compatibility*. They say that the left multiplication $L_{x}$ and the left multiplication $L_{x^{*}}$ are adjoint:

$$
h(L_{x}y,z)=h(y,L_{x^{*}}z).
$$

The form is assumed **non-degenerate**: $h(x,y)=0$ for all $y$ forces $x=0$. The radical is then zero, and the adjoint of an operator is unique. The form is **Hermitian**, so $h(x,x)\in F_{0}$ and $h(y,x)=\varsigma(h(x,y))$.

### The Hermitian Element

Let $a\in H(A)$, $a^{*}=a$. The operator $L_{a}$ is self-adjoint:

$$
h(L_{a}x,y)=h(ax,y)=h(x,a^{*}y)=h(x,ay)=h(x,L_{a}y),
$$

by the compatibility with $(x,y,z)$ replaced by $(a,x,y)$. This is the single most important consequence of the compatibility for the spectral theory: the element is Hermitian exactly when its left multiplication is self-adjoint for the form.

The Hermitian spectral resolution of $a$ is

$$
a=\sum_{i=1}^{r}\lambda_{i}e_{i},
$$

with $\lambda_{i}\in F_{0}$ distinct and $e_{i}$ nonzero Hermitian idempotents, pairwise orthogonal and summing to $1$. It exists exactly when the common minimal polynomial of $a$ splits over $F_{0}$ with distinct roots, by *The Eigenvalue Decomposition of a Hermitian Element*, §*The Existence Theorem*. The idempotents are the Lagrange polynomials in $a$ with coefficients in $F_{0}$, and the resolution is unique.

### The Eigenspaces as Left Ideals

The **eigenspace** of $\lambda_{i}$ for the operator $L_{a}$ is

$$
E_{i}=\ker(L_{a}-\lambda_{i})=\{x:ax=\lambda_{i}x\}.
$$

**Proposition.** $E_{i}=Ae_{i}$, and $A=\bigoplus_{i=1}^{r}Ae_{i}$ is a direct sum.

*Proof.* If $x=x'e_{i}$, then $ax=x'ae_{i}=x'\lambda_{i}e_{i}=\lambda_{i}x$, so $Ae_{i}\subseteq E_{i}$. Conversely, if $ax=\lambda_{i}x$, write $x=\sum_{j}xe_{j}$, which uses $\sum_{j}e_{j}=1$. Since $a$ commutes with each $e_{j}$ and $ae_{j}=\lambda_{j}e_{j}$,

$$
0=(L_{a}-\lambda_{i})x=\sum_{j}(\lambda_{j}-\lambda_{i})xe_{j}.
$$

The summand $xe_{j}$ lies in $Ae_{j}$, and the sum $A=\sum_{j}Ae_{j}$ is direct because the $e_{j}$ are orthogonal idempotents: if $\sum_{j}y_{j}=0$ with $y_{j}\in Ae_{j}$, then multiplying on the right by $e_{k}$ gives $y_{k}=0$. Hence each summand $(\lambda_{j}-\lambda_{i})xe_{j}$ vanishes, and for $j\neq i$ one gets $xe_{j}=0$. Thus $x=xe_{i}\in Ae_{i}$.

**Remark.** The eigenspaces are the left ideals $Ae_{i}$, not the corners $e_{i}Ae_{i}$. The corner is the part of the eigenspace on which the right multiplication by $e_{i}$ also acts as the identity; the left ideal is the full eigenspace. The distinction matters for the form: the left ideal is non-degenerate, while the corner may be degenerate.

## Orthogonality

### The Eigenprojectors

**Theorem.** The eigenprojectors are pairwise orthogonal for $h$:

$$
\boxed{\;h(e_{i},e_{j})=0 \quad (i\neq j)\;}.
$$

*Proof.* For $i\neq j$, $e_{i}e_{j}=0$ and $e_{i}^{*}=e_{i}$. By the compatibility,

$$
h(e_{i},e_{j})=h(e_{i}^{2},e_{j})=h(e_{i},e_{i}^{*}e_{j})=h(e_{i},e_{i}e_{j})=0 .
$$

**Remark.** The proof uses only the Hermitian character of $e_{i}$ and the orthogonality of the idempotents, not the non-degeneracy of $h$. The eigenprojectors therefore form an orthogonal family for any compatible form, degenerate or not.

### The Orthogonality of the Eigenspaces

**Theorem.** The eigenspaces are pairwise orthogonal for $h$:

$$
h(Ae_{i},Ae_{j})=0 \quad (i\neq j).
$$

*Proof.* Let $x\in Ae_{i}$ and $y\in Ae_{j}$. Then $L_{a}x=\lambda_{i}x$ and $L_{a}y=\lambda_{j}y$. Since $L_{a}$ is self-adjoint,

$$
\lambda_{i}h(x,y)=h(L_{a}x,y)=h(x,L_{a}y)=\lambda_{j}h(x,y),
$$

so $(\lambda_{i}-\lambda_{j})h(x,y)=0$. The eigenvalues are distinct, hence $h(x,y)=0$.

**Corollary.** The algebra splits as an orthogonal direct sum of left ideals,

$$
A=\bigoplus_{i=1}^{r}Ae_{i}, \qquad h(Ae_{i},Ae_{j})=0 \quad (i\neq j),
$$

and each $Ae_{i}$ is non-degenerate.

*Proof.* The direct sum is the proposition of §*The Eigenspaces as Left Ideals*, and the orthogonality is the theorem. For the non-degeneracy, let $x\in Ae_{i}$ with $h(x,Ae_{i})=0$. For $y=\sum_{j}y_{j}$ with $y_{j}\in Ae_{j}$,

$$
h(x,y)=\sum_{j}h(x,y_{j})=h(x,y_{i})=0,
$$

because $h(x,y_{j})=0$ for $j\neq i$ by orthogonality and $h(x,y_{i})=0$ by the assumption. Hence $x$ is orthogonal to all of $A$, and $x=0$ by non-degeneracy. So the radical of $Ae_{i}$ is zero.

**Remark.** The corollary is the form-theoretic form of the spectral theorem. The element $a$ acts on each summand by the scalar $\lambda_{i}$, and the summands are orthogonal and non-degenerate. The decomposition is a **simultaneous diagonalisation** of the multiplication by $a$ and of the form: the operator is scalar on each block, and the form is block-diagonal with no cross terms.

### The Distinction from the Corner

The corner $e_{i}Ae_{i}$ is a subspace of the non-degenerate left ideal $Ae_{i}$, but it need not be non-degenerate itself: a subspace of a non-degenerate space can be degenerate. The projector $e_{i}$ is the unit of the corner, and $h(e_{i},e_{i})$ can vanish. When it does, the spectral idempotent is **isotropic**; the corner itself may nevertheless be non-degenerate, as the example below shows. The left ideal $Ae_{i}$ is still non-degenerate, and the eigenvalue is still visible on the vectors of $Ae_{i}$ of nonzero norm; only the projector itself fails to have nonzero norm.

**Example.** Let $A=M_{2}(\mathbb{C})$ with the form $h(X,Y)=\tau(XGY^{*})$, $G=\operatorname{diag}(1,-1)$, and the conjugate transpose as involution. The identity $1$ is a Hermitian idempotent, and

$$
h(1,1)=\tau(G)=1-1=0 .
$$

The scalar element $a=1$ has the one-term resolution $1=1\cdot1$, with the eigenprojector $1$ isotropic. The eigenspace $A1=A$ is the whole algebra, which is non-degenerate, and the eigenvalue $1$ is visible at any $X$ with $h(X,X)\neq0$, for instance $X=E_{11}$, where $h(E_{11},E_{11})=1$ and the Rayleigh quotient is $1$. The example shows that the non-degeneracy of the eigenspaces does not force the projectors to be non-isotropic.

## The Eigenvalue Formula

### The Rayleigh Quotient

**Theorem.** Let $x\in Ae_{i}$ with $h(x,x)\neq0$. Then

$$
\boxed{\;\lambda_{i}=\frac{h(ax,x)}{h(x,x)}\;} .
$$

In particular, if $h(e_{i},e_{i})\neq0$, then

$$
\lambda_{i}=\frac{h(ae_{i},e_{i})}{h(e_{i},e_{i})}.
$$

*Proof.* Since $x\in Ae_{i}$, $ax=\lambda_{i}x$. Then $h(ax,x)=\lambda_{i}h(x,x)$, and the quotient gives $\lambda_{i}$. The second formula is the case $x=e_{i}$.

**Remark.** The quotient lies in $F_{0}$: the numerator is $h(ax,x)=\varsigma(h(x,ax))=\varsigma(h(a^{*}x,x))=\varsigma(h(ax,x))$, so it is fixed by $\varsigma$, and the denominator $h(x,x)$ is fixed by $\varsigma$ as well. The formula is the form-level reconstruction of the eigenvalue, and it is the reason the eigenvalue is a scalar of the fixed field and not an arbitrary element of $F$.

**Corollary.** If $h$ is positive definite, then $h(e_{i},e_{i})>0$ for every nonzero $e_{i}$, and the eigenvalue is the Rayleigh quotient at the projector,

$$
\lambda_{i}=\frac{h(ae_{i},e_{i})}{h(e_{i},e_{i})}.
$$

If $a$ is a positive element, then $\lambda_{i}\geq0$.

*Proof.* Positive definiteness gives $h(e_{i},e_{i})>0$, and the formula applies. If $a$ is positive, $a=b^{2}$ with $b$ Hermitian, and $h(ae_{i},e_{i})=h(b^{2}e_{i},e_{i})=h(be_{i},be_{i})\geq0$, so $\lambda_{i}\geq0$.

### The Diagonalisation of the Form

Let $q(x)=h(x,x)$ be the quadratic form of the datum. On the commutative algebra $F_{0}[a]=\bigoplus_{i}F_{0}e_{i}$, an element is $x=\sum_{i}\mu_{i}e_{i}$ with $\mu_{i}\in F_{0}$, and

$$
q(x)=h\left(\sum_{i}\mu_{i}e_{i},\sum_{j}\mu_{j}e_{j}\right)
=\sum_{i,j}\mu_{i}\mu_{j}h(e_{i},e_{j})
=\sum_{i}\mu_{i}^{2}h(e_{i},e_{i}),
$$

because the cross terms vanish by the orthogonality of the projectors. The restriction of $q$ to $F_{0}[a]$ is therefore the diagonal quadratic form

$$
q|_{F_{0}[a]}=\sum_{i=1}^{r}h(e_{i},e_{i})X_{i}^{2},
$$

in the coordinates $x=\sum_{i}X_{i}e_{i}$. The spectral resolution diagonalises the form on the algebra generated by $a$, and the diagonal entries are the values of the form on the eigenprojectors.

**Remark.** The diagonal form may be degenerate even when $h$ is non-degenerate, because some of the diagonal entries $h(e_{i},e_{i})$ may vanish; the example of §*The Distinction from the Corner* is the case $r=1$ with $h(1,1)=0$. The eigenspaces $Ae_{i}$ are non-degenerate, but the projector lines $\mathbb{C}e_{i}$ need not be. The two statements are compatible: the form is non-degenerate on the whole eigenspace, and it may vanish on the particular vector $e_{i}$.

**Corollary.** If $h$ is positive definite, the restriction of $q$ to $F_{0}[a]$ is positive definite, and the spectral resolution is an orthogonal diagonalisation of $q$ with positive diagonal entries. If $h$ is indefinite and the diagonal entries are all nonzero, the diagonal entries have signs, and the signature of $q$ on $F_{0}[a]$ is the signature of the diagonal form $\sum_{i}h(e_{i},e_{i})X_{i}^{2}$; if some entry vanishes, the restriction is degenerate and one records the nullity as well.

*Proof.* The diagonal formula and the positivity or indefiniteness of the entries. The signature statement is Sylvester's law read on the diagonal form, in the non-degenerate case.

## The Peirce Decomposition

### The Involution on the Corners

The eigenprojectors are Hermitian, so the Peirce decomposition of *Hermitian Idempotents and the Peirce Decomposition* applies to each of them and to the family. For the family $\{e_{i}\}$,

$$
A=\bigoplus_{i,j}e_{i}Ae_{j}, \qquad (e_{i}Ae_{j})^{*}=e_{j}Ae_{i},
$$

the diagonal corners are $*$-subalgebras with units $e_{i}$, and the off-diagonal corners are exchanged in pairs. The Hermitian part splits as

$$
H(A)=\bigoplus_{i}H(e_{i}Ae_{i})\oplus\bigoplus_{i<j}H(e_{i}Ae_{j}\oplus e_{j}Ae_{i}).
$$

### The Form on the Peirce Spaces

The left ideal $Ae_{i}$ is the direct sum of the Peirce spaces $e_{j}Ae_{i}$ over $j$; the eigenspace is not a single corner. The form is non-degenerate on the whole left ideal, but its restrictions to the individual corners need not be. The diagonal corner $e_{i}Ae_{i}$ is the part of the eigenspace on which the right multiplication by $e_{i}$ acts as the identity. Its form is the restriction of $h$ to the corner.

**Remark.** The corner and the projector carry two different notions of non-degeneracy. The corner is non-degenerate when its radical vanishes; the projector is non-isotropic when $h(e_{i},e_{i})\neq0$. Neither condition implies the other in general. A non-degenerate corner can contain the isotropic vector $e_{i}$, as a hyperbolic plane contains an isotropic line; an isotropic projector can sit in a corner whose form is otherwise non-degenerate. What the spectral theorem uses is the non-degeneracy of the left ideal $Ae_{i}$, which is the corollary of §*The Eigenspaces as Left Ideals*, not the non-degeneracy of the corner.

**Example.** In the matrix algebra of §*The Distinction from the Corner*, the corner of the identity is the whole algebra, which is non-degenerate, and the projector $1$ is isotropic. The example separates the two notions: the corner is non-degenerate, and the projector is not.

## The Positive Definite Case

### The Spectral Theorem

In this section $F$ is an ordered field, for instance $\mathbb{R}$, and $h$ is positive definite.

**Theorem.** Let $h$ be positive definite, so that $h(x,x)>0$ for every nonzero $x$. Then:

1. every nonzero Hermitian idempotent has $h(e,e)>0$;
2. every eigenspace $Ae_{i}$ is positive definite;
3. the eigenvalues are the Rayleigh quotients at the projectors;
4. the spectral resolution is an orthogonal direct sum of positive definite left ideals.

*Proof.* The first clause is the definition of positive definiteness applied to the nonzero vector $e$. The second is the restriction of a positive definite form to a subspace. The third is the Rayleigh theorem with $h(e_{i},e_{i})>0$. The fourth is the corollary of §*The Eigenspaces as Left Ideals* together with the second clause.

**Corollary.** Let $h$ be positive definite and let $a$ be Hermitian. Then $a$ lies in the positive cone $H(A)_{+}$ if and only if all its eigenvalues are non-negative. The spectral resolution is the classical spectral theorem of the Hilbert algebra, and the operator norm of $L_{a}$ for the norm $\lVert x\rVert=h(x,x)^{1/2}$ is the spectral radius,

$$
\lVert L_{a}\rVert=\max_{i}\lvert\lambda_{i}\rvert .
$$

*Proof.* Positive definiteness makes $H(A)$ formally real: for Hermitian $x$, $h(x^{2},1)=h(x,x^{*})=h(x,x)$, so a vanishing sum of squares has every term zero. The positivity criterion is then the positive-cone corollary of *The Eigenvalue Decomposition in a Jordan Algebra*, read in $H(A)$. The norm identity is the standard consequence of the orthogonal diagonalisation: the operator is multiplication by $\lambda_{i}$ on the orthogonal summand $Ae_{i}$, and the norm of the direct sum is the maximum of the norms of the summands.

**Remark.** The positive definite case is the case in which the form and the spectral resolution are in complete harmony: the projectors are non-isotropic, the diagonal form on $F_{0}[a]$ is positive definite, and the eigenspaces are positive definite. The indefinite case loses the first and the third clauses but keeps the orthogonal decomposition and the non-degeneracy of the eigenspaces; the difference is the subject of §*The Indefinite Case*.

### The Hermitian Matrices

Let $A=M_{n}(\mathbb{C})$ with the conjugate transpose and the trace form

$$
h(X,Y)=\tau(XY^{*}),
$$

which is positive definite and compatible with the product. A Hermitian matrix $a$ has the spectral resolution $a=\sum_{i}\lambda_{i}P_{i}$ with real eigenvalues and orthogonal projections $P_{i}$; the eigenspace $AP_{i}$ is the space of matrices whose columns lie in the eigenspace of $\lambda_{i}$, and the form restricts to it as the positive definite trace form. The eigenprojectors are pairwise orthogonal, $h(P_{i},P_{j})=\tau(P_{i}P_{j})=\delta_{ij}\operatorname{rank}P_{i}$, and the Rayleigh quotient at $P_{i}$ is $\lambda_{i}$. The spectral resolution is the orthogonal direct sum of the spaces $AP_{i}$, and the form is block-diagonal on them.

### The Group Algebra

Let $A=\mathbb{C}[G]$ for a finite group $G$, with the involution $g^{*}=g^{-1}$ and the form

$$
h(x,y)=\tau(xy^{*}),
$$

the $L^{2}$ form of *Group Algebras*. It is positive definite, and a self-adjoint element is a function $f$ with $f(g^{-1})=\overline{f(g)}$. The left regular representation decomposes into the isotypic components of the irreducible representations. For a central self-adjoint element $f$, the spectral resolution is the Fourier decomposition: the eigenvalues are the scalars by which $f$ acts on the irreducible components, and the eigenprojectors are the central idempotents of the isotypic components. For a general self-adjoint $f$, the resolution refines the isotypic decomposition inside each component, and the eigenprojectors are matrix projections there. The form is orthogonal on the projectors, and the Rayleigh quotient gives the eigenvalue on each spectral block.

## The Indefinite Case

### The Isotropic Projector

**Example.** Let $A=M_{2}(\mathbb{C})$ with the form $h(X,Y)=\tau(XGY^{*})$, $G=\operatorname{diag}(1,-1)$, and the conjugate transpose as involution. The form is non-degenerate and compatible, but it is indefinite. The identity is a Hermitian idempotent with

$$
h(1,1)=\tau(G)=0,
$$

so the eigenprojector of the scalar element $a=1$ is isotropic. The one-term resolution $1=1\cdot1$ is the spectral resolution, the eigenspace $A1=A$ is non-degenerate, and the eigenvalue $1$ is visible at $X=E_{11}$, where $h(E_{11},E_{11})=1$ and the Rayleigh quotient is $1$. The diagonal form on $F_{0}[a]=\mathbb{C}1$ is $q(X1)=h(1,1)X^{2}=0$: it is identically zero, although the ambient form is non-degenerate. The example shows that the restriction of a non-degenerate form to the algebra generated by a Hermitian element can be degenerate, and that the eigenvalue need not be visible at the projector.

**Remark.** The eigenspaces $Ae_{i}$ remain non-degenerate in the indefinite case; the corollary of §*The Eigenspaces as Left Ideals* uses only the non-degeneracy of $h$ and the orthogonality of the spectral resolution. What fails is the non-isotropy of the projectors and the positive definiteness of the diagonal form. The eigenvalue is reconstructed from any vector of the eigenspace of nonzero norm, not necessarily from the projector.

### The Signature of the Form

In this section $F=\mathbb{R}$.

**Theorem.** Let $h$ be non-degenerate and let $a$ be Hermitian with the spectral resolution $a=\sum_{i}\lambda_{i}e_{i}$. Then the form is the orthogonal direct sum of its restrictions to the eigenspaces,

$$
h=\bigoplus_{i=1}^{r}h|_{Ae_{i}},
$$

and the signature of $h$ is the sum of the signatures of the restrictions,

$$
\boxed{\;\operatorname{sig}(h)=\sum_{i=1}^{r}\operatorname{sig}(h|_{Ae_{i}})\;}.
$$

*Proof.* The eigenspaces are pairwise orthogonal and sum directly to $A$; the form is block-diagonal with respect to the decomposition. Each restriction is non-degenerate by §*The Eigenspaces as Left Ideals*, so each has a signature, and the signature of an orthogonal direct sum of non-degenerate forms is the sum of the signatures.

**Remark.** The theorem is the form-level content of the spectral resolution: the element $a$ and the form are simultaneously decomposed into the same blocks, the element acting by $\lambda_{i}$ on the $i$-th block and the form restricting to it. The eigenvalues are the labels of the blocks, and the signatures are the form's data on them. The two are independent: the eigenvalues do not determine the signatures, and the signatures do not determine the eigenvalues.

### The Degenerate Form

If $h$ is degenerate, the radical $\operatorname{rad}(A)$ is a nonzero left ideal, by *Sesqualgebras with a Form*, §*The Radical Is an Ideal*. The spectral resolution of a Hermitian element still exists in the algebra, but the corollary that the eigenspaces are non-degenerate fails: an eigenspace can meet the radical, and the vectors of the radical carry no form-theoretic information. The eigenvalues are then reconstructed only on the non-radical part of each eigenspace, and the radical is invisible to the form. The study of the quotient $A/\operatorname{rad}(A)$ is the subject of *Hermitian Algebras* and of the topological layer; the present article assumes non-degeneracy and does not develop the quotient.

## Summary

Let $(A,*,h)$ be a sesqualgebra with a non-degenerate Hermitian form, and let $a=a^{*}$ have the Hermitian spectral resolution $a=\sum_{i}\lambda_{i}e_{i}$. The eigenprojectors are pairwise orthogonal for $h$; the eigenspaces are the left ideals $Ae_{i}$; they are pairwise orthogonal, their sum is direct, and each is non-degenerate. The eigenvalue is the Rayleigh quotient

$$
\lambda_{i}=\frac{h(ax,x)}{h(x,x)}
$$

on any vector of $Ae_{i}$ of nonzero norm, and in particular at the projector when $h(e_{i},e_{i})\neq0$. On the commutative algebra $F_{0}[a]=\bigoplus_{i}F_{0}e_{i}$ the quadratic form $q(x)=h(x,x)$ is diagonal,

$$
q|_{F_{0}[a]}=\sum_{i}h(e_{i},e_{i})X_{i}^{2},
$$

and the spectral resolution diagonalises both the multiplication by $a$ and the form. The diagonal entries may vanish even when $h$ is non-degenerate; the projector is then isotropic, although the eigenspace remains non-degenerate. In the positive definite case the projectors are non-isotropic, the eigenspaces are positive definite, the eigenvalues are the Rayleigh quotients at the projectors, and the resolution is the classical spectral theorem. In the indefinite case the signatures of the eigenspaces add to the signature of $h$, and the eigenvalues and the signatures are independent data. In the degenerate case the radical is a left ideal, and the form sees only the quotient.

The compatibility and the radical are *Sesqualgebras with a Form*; the Hermitian idempotents and the Peirce decomposition are *Hermitian Idempotents and the Peirce Decomposition*; the Hermitian spectral resolution is *The Eigenvalue Decomposition of a Hermitian Element*; the Jordan spectral theorem is *The Eigenvalue Decomposition in a Jordan Algebra*; and the positive definite topological layer is Part II.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F$ | a field of characteristic not two |
| $\varsigma$ | an involution of $F$ |
| $F_{0}=F^{\varsigma}$ | the fixed field |
| $A$ | a finite-dimensional unital associative $F$-algebra |
| $*$ | a $\varsigma$-semilinear involution of $A$ |
| $h$ | a Hermitian form, $h(y,x)=\varsigma(h(x,y))$ |
| $q(x)=h(x,x)$ | the quadratic form of the datum |
| $L_{a}$ | the left multiplication by $a$ |
| $a=\sum_{i}\lambda_{i}e_{i}$ | the Hermitian spectral resolution |
| $\lambda_{i}\in F_{0}$ | the eigenvalues |
| $e_{i}$ | the Hermitian eigenprojectors |
| $E_{i}=Ae_{i}$ | the eigenspace of $\lambda_{i}$ |
| $h(Ae_{i},Ae_{j})=0$ | the orthogonality of the eigenspaces |
| $h|_{Ae_{i}}$ | the non-degenerate restriction to the eigenspace |
| $\operatorname{sig}(h)$ | the signature of the form |
| $\operatorname{rad}(A)$ | the radical, a left ideal |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Peirce decomposition, the idempotents and the matrix examples.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for the Hermitian Jordan algebra and its spectral theory.
- Jacques Faraut and Adam Korányi, *Analysis on Symmetric Cones* (Oxford University Press, 1994), for the positive definite case, the Rayleigh quotient and the symmetric cones.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the Hermitian forms and the involutions.
- Israel Nathan Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the Hermitian elements and the form-theoretic orthogonality.
