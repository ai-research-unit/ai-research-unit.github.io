# __The Enveloping Operator Algebra and the Collapse of the Two-Sided Action on the Split-Complex Ring__

## Introduction

The enveloping algebra of the split-complex ring over $\mathbb{R}$ is $\mathbb{R}^4$, and it acts on the ring by $\sum B_i\otimes C_i:X\mapsto\sum B_iXC_i$. The action collapses: every such operator is the multiplication by a single element, and the map from $\mathbb{R}^4$ to the operators has a kernel of dimension two. This article computes the enveloping algebra, the four idempotents that generate it, the image and the kernel of the action, and the sense in which the two-sided operators add nothing to the one-sided ones.

The claim is that the collapse is exactly commutativity. In a commutative ring the left and the right multiplication by an element agree, so a product $BXC$ depends on $B$ and $C$ only through $BC$; the two-sided family is therefore not a family of two parameters but the image of the multiplication map, and the multiplication map of $\mathbb{R}^4$ onto $\mathbb{R}^2$ loses half the enveloping algebra. Over the biquaternions, where the left and right multiplications differ, no such collapse happens, and that comparison is the sharpest way to see what the split ring is missing.

The ring is *Split-Complex Algebra*, its idempotents are *Ideals and Peirce Decomposition of the Split-Complex Algebra*, the multiplication operators are *Split-Complex Linear Representations*, and the modules on which the algebra acts are *Modules over the Split-Complex Ring*.

## The Enveloping Algebra

### The Definition

**Definition.** The **enveloping algebra** of $\mathbb{C}_{\mathrm{spl}}$ over $\mathbb{R}$ is $E=\mathbb{C}_{\mathrm{spl}}\otimes_{\mathbb{R}}\mathbb{C}_{\mathrm{spl}}$, with the multiplication $(B\otimes C)(B'\otimes C')=BB'\otimes CC'$.

It is a real algebra of dimension four, and it is the algebra whose modules are the bimodules of the ring.

### The Tensor Square Is $\mathbb{R}^4$

**Theorem.** $E\cong\mathbb{R}^4$ as a real algebra.

**Proof.** The ring is $\mathbb{R}^2$ as a real algebra, and the tensor product distributes over the direct sum: $\mathbb{R}^2\otimes\mathbb{R}^2\cong\mathbb{R}^4$, the four summands being $\Pi_i\otimes\Pi_j$ for $i,j\in\{+,-\}$, with the componentwise product.

The four summands are the four lines $\mathbb{R}(\Pi_i\otimes\Pi_j)$, and each is an ideal of $E$ isomorphic to $\mathbb{R}$.

### The Four Idempotents

**Proposition.** The elements

$$
\Pi_+\otimes\Pi_+, \quad \Pi_+\otimes\Pi_-, \quad \Pi_-\otimes\Pi_+, \quad \Pi_-\otimes\Pi_-
$$

are orthogonal idempotents summing to $1\otimes1$, and they are $\tfrac14(1\pm j)\otimes(1\pm j)$.

**Proof.** $(\Pi_i\otimes\Pi_j)^2=\Pi_i^2\otimes\Pi_j^2=\Pi_i\otimes\Pi_j$, and the products of distinct pairs vanish componentwise; the sum of the four is $(\Pi_++\Pi_-)\otimes(\Pi_++\Pi_-)=1\otimes1$. The displayed form is the expansion of $\tfrac14(1\pm j)(1\pm j)$.

So $E$ is the product of four copies of $\mathbb{R}$, and its identity is $1\otimes1$, not $1$. The distinction matters for the action: the idempotent $1\otimes1$ acts as the identity operator, while each of the four small idempotents acts as a multiplication by an idempotent of the ring.

## The Two-Sided Action

### The Definition

**Definition.** The **two-sided action** of $E$ on $\mathbb{C}_{\mathrm{spl}}$ is

$$
\Bigl(\sum_i B_i\otimes C_i\Bigr)\cdot X=\sum_i B_iXC_i .
$$

It is a representation of $E$ on the real vector space of dimension two, and it is the action of the enveloping algebra by which the ring is a bimodule over itself.

### The Collapse

**Theorem.** For every $e=\sum_i B_i\otimes C_i$ and every $X$,

$$
e\cdot X=X\,\sum_i B_iC_i .
$$

**Proof.** $BX$ and $XC$ are products in a commutative ring, so $BXC=XBC$, and the sum gives $X\sum_iB_iC_i$.

Every two-sided operator is therefore a one-sided one: it is the multiplication by the element $m(e)=\sum_iB_iC_i$, on the left and on the right indifferently. The operator depends on $e$ only through $m(e)$, and the two-sided operators are exactly the multiplication operators.

### The Image and the Kernel

**Theorem.** The map $e\mapsto(e\cdot)$ from $E$ to $\operatorname{End}_{\mathbb{R}}(\mathbb{C}_{\mathrm{spl}})$ has image of real dimension two and kernel of real dimension two.

**Proof.** The map factors as $E\to\mathbb{C}_{\mathrm{spl}}\to\operatorname{End}_{\mathbb{R}}(\mathbb{C}_{\mathrm{spl}})$, the first arrow the multiplication $m$ and the second the multiplication operator $L_Q$. The second is injective and its image has dimension two; the first is onto and its kernel has dimension $4-2=2$.

In the four idempotents the kernel is spanned by the two off-diagonal ones, $\Pi_+\otimes\Pi_-$ and $\Pi_-\otimes\Pi_+$: their products $B_+C_-$ and $B_-C_+$ vanish, so they act by zero. The action sees the two diagonal coefficients of the tensor and ignores the two off-diagonal ones; the algebra $E$ is four-dimensional, the operator algebra it generates is two-dimensional, and the loss is exactly the two idempotents that mix the components.

### The Non-Faithfulness

**Corollary.** The action is not faithful, and the ring is not a faithful module over its enveloping algebra.

**Proof.** The kernel is two-dimensional, so two distinct elements of $E$ act by the same operator; and a faithful action has trivial kernel.

The failure is measured by the two off-diagonal idempotents, and it is the module-level statement of the Peirce decomposition: an operator of the enveloping algebra that mixes the two components acts by zero, because the two components of the ring multiply to zero and the two components of $X$ cannot see the mixing.

## The One-Sided Operators

### The Multiplication Operators

The one-sided operators are the maps $X\mapsto AX$ with $A\in\mathbb{C}_{\mathrm{spl}}$, and they form a real vector space of dimension two, isomorphic to the ring itself. In the basis $1,j$ the operator is the matrix

$$
\begin{pmatrix}a&b\\ b&a\end{pmatrix} ,
$$

the matrix of the multiplication by $A=a+bj$, and the space of these matrices is the space of the symmetric $2\times2$ matrices with equal diagonal entries.

### The Two-Sided Operators Add Nothing

**Theorem.** The set of two-sided operators $\{X\mapsto\sum_iB_iXC_i\}$ is the set of one-sided operators, and the left and right multiplications coincide.

**Proof.** The collapse gives $\sum_iB_iXC_i=XM$ with $M=\sum_iB_iC_i$, which is a left multiplication by $M$, and $XM=MX$ in a commutative ring, so it is also a right multiplication by $M$. Conversely every left multiplication is a two-sided operator with a single term, $1\otimes M$.

So the two-sided family is not larger than the one-sided one: it is the same two-dimensional space, reached twice. A bimodule over the split ring is a module, and the bimodule structure carries no information that the module structure does not.

### The Composition

The composition of two-sided operators is again two-sided, and on the parameters it is the multiplication: the operator of $e$ composed with the operator of $f$ is the operator of $m(e)m(f)$, which is the operator of $m(ef)$. The image is therefore a subalgebra of $\operatorname{End}_{\mathbb{R}}(\mathbb{C}_{\mathrm{spl}})$, isomorphic to the ring, and the action is a surjection of $E$ onto that subalgebra with kernel of dimension two.

## The Comparison

### The Complex Case

Over $\mathbb{C}$ the ring is commutative, so the collapse holds there too: $\sum B_iXC_i=X\sum B_iC_i$. The enveloping algebra over $\mathbb{R}$ is $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C}$, of real dimension four, and the action again sees only the product, so again two real parameters survive out of four. The complex case and the split case coincide in this respect, and the coincidence is commutativity and nothing else.

What differs is the arithmetic of the surviving parameters: over $\mathbb{C}$ the multiplication operator $L_Q$ is the multiplication by a complex number and its matrix is a rotation-dilation, invertible for every $Q\neq0$; here the matrix is the one displayed above and it is singular on the two null lines. The collapse of the action is the same, and the invertibility of the collapse is not.

### The Biquaternion Case

Over $\mathbb{B}$ the ring is not commutative, and $BXC$ is not $XBC$. The left multiplication by $B$ and the right multiplication by $C$ are different operators, the map $B\otimes C\mapsto(B\mapsto BXC)$ has no kernel, and the two-sided operators are strictly more than the one-sided ones. The biquaternion enveloping algebra is therefore a genuine operator algebra, and the split ring's is not: the whole difference is the commutativity that the split ring has and $\mathbb{B}$ has not.

### Why the Collapse Happens

The collapse has one cause and one measure. **The cause** is the identity $BXC=XBC$, which is commutativity. **The measure** is the kernel of the multiplication $m:E\to\mathbb{C}_{\mathrm{spl}}$, of dimension two, spanned by the two idempotents that mix the components. Where the ring is a product of two copies of a field, the enveloping algebra is a product of four, and the action of the product is the action of its diagonal: the two off-diagonal factors act by zero.

## Summary

The enveloping algebra of the split ring over $\mathbb{R}$ is $\mathbb{R}^4$, with the four orthogonal idempotents $\Pi_i\otimes\Pi_j$ summing to $1\otimes1$. Its action on the ring by $\sum B_i\otimes C_i:X\mapsto\sum B_iXC_i$ collapses to $X\mapsto X\sum_iB_iC_i$, so every two-sided operator is the multiplication by a single element.

The image of the action has real dimension two and its kernel has real dimension two, spanned by the two off-diagonal idempotents $\Pi_+\otimes\Pi_-$ and $\Pi_-\otimes\Pi_+$; the action is not faithful, and the two-sided operators add nothing to the one-sided ones. The composition of the operators is the multiplication of the parameters, and the image is a copy of the ring inside the endomorphism algebra.

The collapse is commutativity. Over $\mathbb{C}$ it happens as well, the enveloping algebra over $\mathbb{R}$ being $\mathbb{C}\oplus\mathbb{C}$ with two of its four real parameters surviving; over $\mathbb{B}$ it does not happen, because the left and right multiplications differ and the two-sided operators form a strictly larger family.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $E=\mathbb{C}_{\mathrm{spl}}\otimes_{\mathbb{R}}\mathbb{C}_{\mathrm{spl}}$ | The enveloping algebra, isomorphic to $\mathbb{R}^4$ |
| $\Pi_i\otimes\Pi_j$, $i,j\in\{+,-\}$ | The four orthogonal idempotents |
| $e\cdot X=\sum_iB_iXC_i$ | The two-sided action |
| $m(e)=\sum_iB_iC_i$ | The multiplication, the collapse |
| $e\cdot X=Xm(e)$ | The collapsed operator, a multiplication |
| $\dim\ker m=2$ | The two off-diagonal idempotents |
| $L_Q$ | The multiplication operator by $Q$ |
| $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C}$ | The complex enveloping algebra over $\mathbb{R}$ |

## Further Reading

- Frank W. Anderson and Kent R. Fuller, *Rings and Categories of Modules* (Springer, Graduate Texts in Mathematics 13, 2nd ed. 1992), for bimodules, the enveloping algebra and the two-sided action.
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for the tensor product of algebras, the idempotents of a product and the Peirce decomposition.
- N. Bourbaki, *Algebra I*, Chapters 1-3 (Springer, 1989), for the tensor product over a field and its identification with a product of copies of the field.
- Paul M. Cohn, *Basic Algebra: Groups, Rings and Fields* (Springer, 2003), for the left and right regular representations and the module structure of a ring over itself.
- Israel Gelfand and Mark Naimark, *Normed Rings* (Noordhoff, 1964), for the operator algebras generated by multiplications and their faithfulness.
