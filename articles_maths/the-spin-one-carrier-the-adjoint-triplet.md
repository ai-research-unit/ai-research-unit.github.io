# __The Spin-One Carrier: the Adjoint Triplet__

## Introduction

**The subject.** Of the four carriers of the operator space, one has label one. It is three-dimensional over the complex numbers, its weight string is $1,0,-1$, and it is the Lie algebra of the copy. This article identifies it, produces its three generators from the one-sided operators, and proves that it is the only carrier of positive label that is closed under the commutator.

**The order of the article.** *The Carrier of Label One* locates the triplet in the series of the operator space. *The Three Generators* builds it from the difference of the left and the right multiplication. *The Brackets Close* proves the closure and the structure constants. *Two Occurrences* compares the triplet as a summand with the triplet as the space of commutators. *The Dual and the Tangent Space* proves that the triplet is its own dual and that it is the tangent space of the group.

**It assumes** *The Carriers, the Representation, the Spin and the Closure*, *The Spin-One Anti-Hermitian Subspace* and *The One-Sided Operators of the Biquaternion Algebra*. **The row of the elements is** where the same label one occurs as the traceless part of the algebra, of complex dimension three.

**The result in one line.** The spin-one carrier is the adjoint triplet, spanned by the three commutators $\tfrac12(L_{\vec e_k}-R_{\vec e_k})$, with weights $1,0,-1$ and brackets $[J_1,J_2]=J_3$ and its cyclic images.

**Boundaries.** The form on the triplet is *The Spin-One Carrier and the Trace Form*; its spectrum and its rank strata are *The Spin-One Carrier and the Spectral Strata* and *The Spin-One Carrier and the Rank Strata*; the label two and label three carriers are treated with the principal reading of the operator space.

Nothing below is a statement of physics. The units are $e_t,\vec e_x,\vec e_y,\vec e_z$ with $\vec e_k^2=-e_t$ and the products cyclic, $\vec e_x\vec e_y=\vec e_z$ and its cyclic images; the algebra is $\mathbb{B}$; the module of the operators is $V=V_{3/2}$ of complex dimension four; the one-sided operators are $L_a(X)=aX$ and $R_b(X)=Xb$; the star is $\natural$; and $\langle S,T\rangle=\operatorname{tr}(S^{\natural}T)$ is the trace form.

## The Carrier of Label One

**Definition.** The operator space is $\operatorname{End}(\mathbb{B})$, of complex dimension sixteen. Its **carriers** are the irreducible pieces of its decomposition under the action of the copy, and the one of largest weight one is written $V_1$, the **adjoint triplet**.

**Proposition.** $V_1$ has complex dimension three and weight string $1,0,-1$; the raising operator carries the coefficient $\sqrt2$ on each of the two steps; and the principal reading of the operator space is

$$
16=7+5+3+1,\qquad \operatorname{End}(\mathbb{B})=V_3\oplus V_2\oplus V_1\oplus V_0 .
$$

*Proof.* The dimension of an irreducible carrier of largest weight $s$ is $2s+1$, which is three at $s=1$; the two steps of the string carry $\sqrt{(1-m)(1+m+1)}$ at $m=0$ for the first, and the same for the second by symmetry. The four numbers add to sixteen, so the sum is the whole space.

**Corollary.** The triplet is the smallest carrier of positive label, and it is the only one whose dimension is odd and less than five.

*Proof.* The dimensions $7,5,3,1$ are the four values, and only three is odd and below five.

**The reading.** The label one is forced by the arithmetic of the row: seven plus five plus three plus one is sixteen, and the four summands are the four carriers. The triplet is the one that sits in the middle of the list.

## The Three Generators

**Definition.** For $k=x,y,z$ put

$$
J_k=\tfrac12\bigl(L_{\vec e_k}-R_{\vec e_k}\bigr)=\tfrac12\operatorname{ad}_{\vec e_k},
\qquad J_k(X)=\tfrac12\bigl(\vec e_kX-X\vec e_k\bigr).
$$

**Proposition.** The three operators $J_k$ lie in $V_1$, they span it, and each is anti-Hermitian for the star, $J_k^{\natural}=-J_k$.

*Proof.* A commutator with an element of the algebra lies in the image of the copy, and the three commutators are independent: their images on the algebra are the three generators of the conjugation action. The star reverses the order of a product, so $L_a^{\natural}=L_{a^{\natural}}$ and $R_b^{\natural}=R_{b^{\natural}}$; with $\vec e_k^{\natural}=-\vec e_k$ the two signs give $J_k^{\natural}=\tfrac12(-L_{\vec e_k}+R_{\vec e_k})=-J_k$.

**Corollary.** The triplet is the complexification of the space of anti-Hermitian elements of the copy, of real dimension three, and the exponential of that space is the group of the copy.

*Proof.* An anti-Hermitian element of the copy is a real combination of the $J_k$ with imaginary coefficients, so the real space is three-dimensional; the exponential of a Lie algebra of anti-Hermitian operators is a group of unitary ones.

**The reading.** The generators are differences of the two one-sided operators, and the factor $\tfrac12$ is what makes the brackets come out with the structure constants of the algebra rather than twice them.

## The Brackets Close

**Theorem.** The triplet is closed under the commutator, and

$$
[J_1,J_2]=J_3,\qquad [J_2,J_3]=J_1,\qquad [J_3,J_1]=J_2 .
$$

*Proof.* The commutator of two commutators with elements $a$ and $b$ is a commutator with $[a,b]$, so $[\operatorname{ad}_a,\operatorname{ad}_b]=\operatorname{ad}_{[a,b]}$. With $a=\tfrac12\vec e_1$ and $b=\tfrac12\vec e_2$ the bracket of the elements is $\tfrac12[\vec e_1,\vec e_2]=\vec e_3$ and the commutator is $\operatorname{ad}_{\vec e_3}=J_3$. The other two relations are the cyclic images.

**Corollary.** $V_1$ is a Lie algebra isomorphic to the Lie algebra of the copy, and the isomorphism is the identity of the triplet with itself.

*Proof.* The closure and the structure constants are those of the copy, and the generators are three independent elements, so the span is isomorphic to the copy.

**Theorem.** No other carrier of positive label is closed under the commutator. The centre $V_0$ is closed only trivially: it is one-dimensional and abelian, and it commutes with everything.

*Proof.* The commutator of two elements of $V_2$ lies in $\Lambda^2V_2$, which is $V_1\oplus V_3$ and does not meet $V_2$; the commutator of two elements of $V_3$ lies in $\Lambda^2V_3$, which contains $V_1$ and $V_3$ and a carrier of label five that is absent from the row, so it is not contained in $V_3$. The centre consists of multiples of the identity, and the commutator with the identity vanishes.

**The reading.** Closure under the bracket is a property of exactly one summand, and this is the structural reason the triplet and the copy are the same object. The other three carriers are modules and not algebras.

## Two Occurrences

**Proposition.** The triplet occurs in two ways: as the summand $V_1$ of the principal reading of the whole operator space, and as the space spanned by the commutators $\tfrac12(L_a-R_a)$ as $a$ ranges over the algebra. The two spaces coincide.

*Proof.* The commutators with the three units are three independent elements of the summand of label one, and the summand has dimension three; the span of all commutators is therefore the whole summand, since every element $a$ is a combination of the units.

**Corollary.** The triplet is the image of the map $a\mapsto\tfrac12\operatorname{ad}_a$, whose kernel is the centre of the algebra, so the triplet is the algebra modulo its centre.

*Proof.* The map is linear and its kernel is the set of elements commuting with everything, which is the centre; the image has dimension $4-1=3$.

**The reading.** The two occurrences are the same statement: the label-one summand of the operator space is the algebra modulo its centre, embedded as commutators. This is why the triplet can be both a module and a Lie algebra.

## The Dual and the Tangent Space

**Proposition.** The triplet is isomorphic to its dual, $V_1^{\star}\cong V_1$.

*Proof.* The trace form restricts to a non-degenerate symmetric form on the triplet, since the four carriers are mutually orthogonal and the form is non-degenerate on each; a non-degenerate form is an isomorphism with the dual. The label is an integer, so the module is of real type and the form can be taken symmetric.

**Corollary.** The triplet is self-dual, and its self-duality is the reason a linear functional on it can be read as an element of it.

*Proof.* The isomorphism of the Proposition is canonical once the form is fixed, and the form is fixed by the trace.

**Proposition.** The triplet is the tangent space at the identity of the group of the copy, and the bracket of the triplet is the derivative at the identity of the commutator of the group.

*Proof.* The group is the image of the triplet under the exponential, so its tangent at the identity is the triplet; the derivative of the commutator of two group elements at the identity is the commutator of the two tangent elements.

**Corollary.** The triplet carries simultaneously a module structure, a Lie algebra structure and the tangent structure of a group, and the three are the same structure.

*Proof.* The module structure is the adjoint action, the Lie algebra structure is the bracket, and the tangent structure is the exponential; on the triplet the adjoint action is the bracket itself.

**The reading.** Label one is the only label at which the carrier is its own adjoint module. That is what the word adjoint in the title means here, and it is the reason the triplet is the natural place to read the group, the algebra and the bracket as one object.

## Further Reading

- [The Spin-One Anti-Hermitian Subspace](the-spin-one-anti-hermitian-subspace.html), for the compact real form and its three dimensions
- [The Carriers, the Representation, the Spin and the Closure](the-carriers-the-representation-the-spin-and-the-closure.html), for the four carriers of the operator space
- [The One-Sided Operators of the Biquaternion Algebra](the-one-sided-operators-of-the-biquaternion-algebra.html), for the left and the right multiplication whose difference gives the triplet
- [The Spin-One Carrier and the Trace Form](the-spin-one-carrier-and-the-trace-form.html), for the form that makes the triplet its own dual
- [From the Spin Group to the Spin of a Single Rotor](from-the-spin-group-to-the-spin-of-a-single-rotor.html), for the group whose tangent space is the triplet
