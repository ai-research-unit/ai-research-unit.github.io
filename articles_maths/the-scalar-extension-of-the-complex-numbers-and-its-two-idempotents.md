# __The Scalar Extension of the Complex Numbers and Its Two Idempotents__

## Introduction

The scalar extension of the complex field by itself is the tensor product $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$, taken over the reals, with four real dimensions. It is not a field. It is the product $\mathbb{C}\oplus\mathbb{C}$ of two copies of the field, and the two copies are visible inside the tensor as two elements $u$ and $v$ that multiply to zero and add to the tensor unit. These are the only non-trivial idempotents of the whole complex family, and they exist in the extension for the exact reason they cannot exist in the algebra: $\mathbb{C}$ is a field, and a product of two fields is not.

The article constructs the isomorphism, exhibits $u$ and $v$, proves their properties, reads the two projections and the Peirce decomposition they force, explains why the extension carries them and the algebra does not, gives the tensor reading of the two factors, and compares the count with the split-complex family.

The field and its laws are *Complex Algebra* and *The Specificities of the Complex Algebra*; the absence of a non-trivial idempotent in the algebra is *The Classes of Element of the Complex Algebra*; the collapse of the two-sided action, which reads the same two idempotents, is *The Enveloping Operator Algebra and the Collapse of the Two-Sided Action on the Complex Algebra*; the vector-space side of the extension is *The Two Products of the Complex Space* read with changed scalars, and the Galois reading of the two copies is *Galois Theory of ℂ/ℝ*.

**Interpretation.** The element of the algebra is $Q=q+iq'$, and $1$ is its unit. The extension is written $\mathbb{C}^{\mathrm{e}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$, with the first factor the algebra and the second the scalars; a decomposable tensor is $B\otimes C$, and the multiplication is $(B\otimes C)(B'\otimes C')=BB'\otimes C C'$. The basis of the extension over $\mathbb{R}$ is $1\otimes1$, $1\otimes i$, $i\otimes1$, $i\otimes i$, so every element is a real combination of four tensors.

## The Extension as a Product of Two Fields

**Theorem.** $\mathbb{C}^{\mathrm{e}}\cong\mathbb{C}\oplus\mathbb{C}$ as $\mathbb{R}$-algebras.

*Proof.* Read $\mathbb{C}$ as $\mathbb{R}[x]/(x^{2}+1)$. Then $\mathbb{C}^{\mathrm{e}}\cong\mathbb{C}[x]/(x^{2}+1)$, the polynomial ring over $\mathbb{C}$ modulo the polynomial of the second factor. Over $\mathbb{C}$ the polynomial splits, $x^{2}+1=(x-i)(x+i)$, and the two factors are coprime. The Chinese remainder theorem gives $\mathbb{C}[x]/(x^{2}+1)\cong\mathbb{C}[x]/(x-i)\oplus\mathbb{C}[x]/(x+i)\cong\mathbb{C}\oplus\mathbb{C}$, the two components being the evaluations at $i$ and at $-i$.

**Corollary.** Every element of the extension is a pair of complex numbers, and multiplication is componentwise.

**Remark (the dimension count).** The extension has real dimension four; the product of two copies of the field has real dimension four; the two sides agree, as they must. The count alone does not prove the isomorphism, and the multiplicative statement of the proof is what does.

**Remark (the extension is not a field).** The product $\mathbb{C}\oplus\mathbb{C}$ has zero divisors, so the extension has them too, and the two are exhibited in the next section. The reason is the splitting of $x^{2}+1$ over $\mathbb{C}$: the defining polynomial of the algebra is no longer irreducible once the scalars contain a root of it. This is the standard behaviour of a quadratic extension tensored with itself, and it is why the extension of the complex field is a product and not a field.

## The Two Idempotents

**Definition.** The two elements are

$$
u=\tfrac12\bigl(1\otimes1+i\otimes i\bigr), \qquad v=\tfrac12\bigl(1\otimes1-i\otimes i\bigr).
$$

**Theorem.** The elements $u$ and $v$ are idempotent, orthogonal, and sum to the tensor unit:

$$
u^{2}=u, \qquad v^{2}=v, \qquad uv=0, \qquad u+v=1\otimes1 .
$$

*Proof.* Compute in the tensor: $(i\otimes i)^{2}=i^{2}\otimes i^{2}=(-1)\otimes(-1)=1\otimes1$, so $u^{2}=\tfrac14(1\otimes1+2i\otimes i+1\otimes1)=\tfrac12(1\otimes1+i\otimes i)=u$, and the same with the sign reversed for $v$. For the product, $uv=\tfrac14\bigl(1\otimes1-(i\otimes i)^{2}\bigr)=\tfrac14(1\otimes1-1\otimes1)=0$. The sum is immediate.

**Proposition.** In the two copies the idempotents are $u=(0,1)$ and $v=(1,0)$.

*Proof.* The evaluation at $i$ of $u$ is $\tfrac12(1+i\cdot i)=0$ and its evaluation at $-i$ is $\tfrac12(1+i\cdot(-i))=1$; for $v$ the two values are interchanged.

**Theorem.** The idempotents of the extension are exactly $0$, $u$, $v$ and $1\otimes1$.

*Proof.* In the product $\mathbb{C}\oplus\mathbb{C}$ an idempotent is a pair of idempotents of $\mathbb{C}$, and a field has only $0$ and $1$ as idempotents, since $\Pi^{2}=\Pi$ reads $\Pi(\Pi-1)=0$ and a field has no zero divisor. There are therefore $2\cdot2=4$ idempotents, and the proposition identifies two of the four as $u$ and $v$.

## The Two Projections

### The First Projection

**Proposition.** The multiplication by $v$ in the extension is the projection onto the first copy: $tv=(a,0)$ for $t=(a,b)$.

*Proof.* Multiply componentwise by $(1,0)$.

### The Second Projection

**Proposition.** The multiplication by $u$ in the extension is the projection onto the second copy: $tu=(0,b)$ for $t=(a,b)$.

*Proof.* Multiply componentwise by $(0,1)$.

**Corollary.** The two projections are orthogonal, idempotent, of sum the identity of the extension, and each has for image one of the two copies.

*Proof.* These are the properties of $u$ and $v$ of the preceding section, read as operators.

## The Peirce Decomposition

**Theorem.** With respect to $v$ the Peirce decomposition of the extension is the direct sum of the two copies, and the two mixed pieces vanish:

$$
\mathbb{C}^{\mathrm{e}}=v\mathbb{C}^{\mathrm{e}}v\oplus v\mathbb{C}^{\mathrm{e}}(1-v)\oplus(1-v)\mathbb{C}^{\mathrm{e}}v\oplus(1-v)\mathbb{C}^{\mathrm{e}}(1-v),
$$

with $v\mathbb{C}^{\mathrm{e}}v=\mathbb{C}v$, $(1-v)\mathbb{C}^{\mathrm{e}}(1-v)=\mathbb{C}u$ and the two mixed pieces zero.

*Proof.* Every element is $av+bu$ with $a,b$ complex, so $v\mathbb{C}^{\mathrm{e}}v$ is spanned by $v^{2}=v$, and $(1-v)\mathbb{C}^{\mathrm{e}}(1-v)$ by $u^{2}=u$; the mixed piece $v\mathbb{C}^{\mathrm{e}}(1-v)$ is spanned by $vuv$, which vanishes because $uv=0$.

**Remark (the contrast with the algebra).** In the algebra the Peirce decomposition with respect to the only non-trivial idempotent $1$ is the trivial one, all the content on the diagonal and no off-diagonal space, as *The Classes of Element of the Complex Algebra* records. In the extension the decomposition is again diagonal, but the diagonal now has two summands, so it carries a genuine splitting. The count of the summands is the count of the factors of the product, and the count of the factors is two.

## Why the Extension Carries Them and the Algebra Does Not

**Proposition.** The algebra has no non-trivial idempotent: the only $\Pi$ with $\Pi^{2}=\Pi$ are $0$ and $1$.

*Proof.* $\Pi^{2}=\Pi$ is $\Pi(\Pi-1)=0$, and the field has no zero divisor.

**Proposition.** The extension has two non-trivial idempotents, $u$ and $v$.

*Proof.* This is the theorem of §*The Two Idempotents*.

**Remark (the reason).** The difference is not the size of the algebra, it is the presence of a zero divisor. An idempotent other than $0$ and $1$ splits the algebra into two ideals, and a field has no proper ideal; a product of two fields has exactly two. Hence the idempotents of the extension are the two points of the spectrum of the extension, and the spectrum is the two-point set of the two embeddings of $\mathbb{C}$ into the extension.

**Remark (the strongest objection).** It may be objected that the two idempotents are an artefact of the extension and say nothing about $\mathbb{C}$. The answer is that they say exactly what the extension is for: they are the two points at which the extension sees the algebra, they are exchanged by the conjugation, and they are the two halves of the collapse of the two-sided action, where the multiplication map $\mu$ kills $u$ and fixes $v$. An artefact of the extension that computes the collapse of the two-sided action of the algebra is not an artefact.

## Outside the Image of the Scalars

**Proposition.** Neither $u$ nor $v$ lies in the image of the map $Q\mapsto Q\otimes1$.

*Proof.* In the two copies, $Q\otimes1$ is the pair $(Q,Q)$, because the evaluation at $i$ and at $-i$ of $Q$ are both $Q$. The image is therefore the diagonal, and $u=(0,1)$ and $v=(1,0)$ are not on it.

**Proposition.** The image of $Q\mapsto1\otimes Q$ is the twisted diagonal $Q\mapsto(Q,\bar Q)$.

*Proof.* The evaluation at $i$ of $1\otimes Q$ is $Q$, and the evaluation at $-i$ is $\bar Q$.

### The Two Embeddings

**Remark (two embeddings).** Both maps are ring homomorphisms, so the extension carries two copies of $\mathbb{C}$: the diagonal copy, which is the algebra extended by scalars, and the twisted copy, which is the scalars embedded with the conjugation. The two copies meet in the real line, the fixed set of the conjugation, and together they generate the extension. That is the tensor reading of the two factors: the first factor is the algebra and enters diagonally, the second is the scalars and enters with the twist of the conjugation.

**Remark (the conjugation is the difference).** The two embeddings agree exactly on the real line, which is why the extension of the scalars of a real algebra adds nothing to the real part. The whole content of the extension lies in the imaginary direction of the scalar copy, and that is where the idempotents live.

## The Two Points of the Complex Family

The count of idempotents separates the members of the family, and the table records it.

| the algebra | the ring | idempotents | non-trivial |
|---|---|---|---|
| $\mathbb{C}$ | a field | $0,1$ | none |
| $\mathbb{C}^{\mathrm{e}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ | $\mathbb{C}\oplus\mathbb{C}$ | $0,u,v,1\otimes1$ | two |
| $\mathbb{C}^{\mathrm{spl}}$ | $\mathbb{R}\oplus\mathbb{R}$ | four | two |
| $\mathbb{C}^{\mathrm{spl}}\otimes_{\mathbb{R}}\mathbb{C}^{\mathrm{spl}}$ | $\mathbb{R}^{4}$ | sixteen | fourteen |

**Remark (the split comparison).** The split-complex algebra is already a product of two copies of $\mathbb{R}$, so its own idempotents are the two-point reading in each factor and number four. Its scalar extension is $\mathbb{R}^{4}$, with four primitive idempotents $e_1,e_2,e_3,e_4$ and sixteen idempotents in all. The complex extension has four idempotents and two of them are primitive; the count is the count of the factors, and the difference between the two families is the difference between $\mathbb{C}$ and $\mathbb{R}$ as a factor.

## Summary

The scalar extension $\mathbb{C}^{\mathrm{e}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ is the product $\mathbb{C}\oplus\mathbb{C}$, by the splitting of $x^{2}+1$ over $\mathbb{C}$ and the Chinese remainder theorem. It carries the two idempotents $u=\tfrac12(1\otimes1+i\otimes i)$ and $v=\tfrac12(1\otimes1-i\otimes i)$, orthogonal, of sum the tensor unit, and they are the only non-trivial ones; neither lies in the image of $Q\mapsto Q\otimes1$, whose image is the diagonal, while the scalars enter through $1\otimes Q$ with the conjugation. The two idempotents are the two projections of the extension on its factors and they force a Peirce decomposition with the two mixed pieces zero. The algebra has no non-trivial idempotent because it is a field; the extension has two because it is a product of two fields, and the two are exchanged by the conjugation. Against the split-complex family the count is four idempotents in the extension and sixteen in its tensor square, the two-point reading in each factor.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{C}^{\mathrm{e}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ | the scalar extension of the complex field by itself |
| $B\otimes C$ | a decomposable tensor, $B$ from the algebra and $C$ from the scalars |
| $u=\tfrac12(1\otimes1+i\otimes i)$, $v=\tfrac12(1\otimes1-i\otimes i)$ | the two idempotents, images $(0,1)$ and $(1,0)$ |
| $Q\otimes1$, $1\otimes Q$ | the two embeddings, of images $(Q,Q)$ and $(Q,\bar Q)$ |
| $\mathbb{C}^{\mathrm{spl}}$ | the split-complex algebra, $\mathbb{R}\oplus\mathbb{R}$ |

## Further Reading

- Serge Lang, *Algebra*, Graduate Texts in Mathematics 211 (Springer, third edition, 2002), for the tensor product of algebras, the Chinese remainder theorem and the splitting of a polynomial over a larger field.
- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for the tensor product of commutative rings, idempotents and the decomposition of a product ring.
- Tsit-Yuen Lam, *A First Course in Noncommutative Rings*, Graduate Texts in Mathematics 131 (Springer, second edition, 2001), for idempotents, Peirce decompositions and the structure of a product of rings.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for the behaviour of an algebra with involution under scalar extension and the idempotents that appear.
