# __The Spin-One Carrier and the Trace Form__

## Introduction

**The subject.** The trace form is the natural form of the operator space. Restricted to the triplet it is non-degenerate, symmetric and positive on the compact real form, and it turns the adjoint action into a rotation. This article computes the restriction, the reality and the signature, proves that the copy embeds in the rotations of the triplet, and relates the restriction to the Killing form.

**The order of the article.** *The Restriction* computes the values on the generators; *Reality and Self-Duality* fixes the type of the module; *The Signature* describes the real forms; *The Adjoint Action Is an Isometry* proves the embedding into the rotations; *The Killing Form* and *The Index and the Norm* read the two invariant forms.

**It assumes** *The Spin-One Carrier: the Adjoint Triplet*, *The Trace Form and Its Signature on the Two Halves* and *The Symmetric and Antisymmetric Parts of the Operator Space*. **The row of the elements is** where the trace form is the quadratic form of the algebra and its restriction to the traceless part is the same calculation one level down.

**The result in one line.** On the triplet the trace form is $5$ times the standard form, the copy acts on it by rotations, and the Killing form is $-\tfrac25$ of the trace form.

**Boundaries.** The brackets are *The Spin-One Carrier: the Adjoint Triplet*; the spectrum and the rank strata are *The Spin-One Carrier and the Spectral Strata* and *The Spin-One Carrier and the Rank Strata*; the signature of the form on the whole operator space is *The Symmetric and Antisymmetric Parts of the Operator Space*.

Nothing below is a statement of physics. The units are $e_t,\vec e_x,\vec e_y,\vec e_z$ with $\vec e_k^2=-e_t$; the generators of the triplet are $J_k=\tfrac12(L_{\vec e_k}-R_{\vec e_k})$; the star is $\natural$; the trace form is $\langle S,T\rangle=\operatorname{tr}(S^{\natural}T)$ for operators and the norm of the algebra is $N(a)$; and $\operatorname{tr}$ is the trace of an operator on the four-dimensional algebra.

## The Restriction

**Definition.** The **restriction** of the trace form to the triplet is the complex bilinear form $g(S,T)=\langle S,T\rangle$ taken on $V_1\times V_1$.

**Proposition.** On the generators the restriction is diagonal with equal entries,

$$
g(J_a,J_b)=5\,\delta_{ab},
$$

so the three generators have the common norm $5$ and are mutually orthogonal.

*Proof.* The trace form is invariant under the copy, so the restriction is an invariant form on an irreducible module and, by the lemma of Schur, a scalar multiple of the standard one. The value on a generator is the trace of $J_k^{\natural}J_k=-J_k^2$, which is $-5$ on each of the three axes, the same number for all three by the symmetry of the axes.

**Corollary.** The restriction is non-degenerate, and the triplet is its own dual through it.

*Proof.* A diagonal form with three equal non-zero entries is non-degenerate, and a non-degenerate form identifies a space with its dual.

**The reading.** The three axes have equal norms, so the form cannot see a choice of axis; this equality is also the reason the copy acts by rotations and not by shears.

## Reality and Self-Duality

**Proposition.** The triplet is of real type: it carries an invariant complex bilinear symmetric form, and it is isomorphic to its own complex conjugate.

*Proof.* The label is an integer, so the module is self-conjugate; a self-conjugate module of integer label carries an invariant symmetric form, unlike a module of half-integer label, which carries an alternating one.

**Corollary.** The restriction can be taken symmetric and complex bilinear, and no conjugation is needed to define it.

*Proof.* Symmetry is the reality of the module, and the trace form is already complex bilinear.

**The reading.** At the neighbouring label the type is the other one: the module of label $\tfrac32$ is of quaternionic type and carries an alternating form, and the triplet carries a symmetric one.

## The Signature

**Definition.** The **compact real form** of the triplet is the real space spanned by the three generators over the real numbers, $V_{1,\mathbb{R}}=\mathbb{R}J_x\oplus\mathbb{R}J_y\oplus\mathbb{R}J_z$, and its elements are the anti-Hermitian ones.

**Proposition.** On the compact real form the restriction is positive definite, so its signature is $(3,0)$; on the complexified triplet it is split, and it admits isotropic vectors.

*Proof.* For a real combination $S=\sum c_kJ_k$ the value $g(S,S)=5\sum c_k^2$ is a sum of squares, which is positive unless all the coefficients vanish. On the complexification the element $J_x+iJ_y$ has $g$-square $5(1+i^2)=0$, so the form is isotropic and the complexified space is a hyperbolic plane orthogonal to the line of $J_z$.

**Corollary.** The complexified triplet decomposes as a hyperbolic plane and an orthogonal line, and the orthogonal group of the form is the complex rotation group of three dimensions.

*Proof.* A non-degenerate symmetric form in three complex dimensions with an isotropic vector splits off a hyperbolic plane and leaves a line, and the isometry group of such a form is the rotation group.

**The reading.** The signature depends on the real form chosen: the compact form is definite, the complexification is split, and the passage between them is the passage from the group to its complexification.

## The Adjoint Action Is an Isometry

**Theorem.** The adjoint action of the copy on the triplet preserves the restriction, so the copy embeds in the orthogonal algebra of the form; on the compact real form the image is the algebra of rotations, and the embedding is an isomorphism.

*Proof.* Invariance of the trace form under conjugation by the copy gives $g([X,S],T)+g(S,[X,T])=0$ for every $X$ in the copy, which is the statement that the adjoint action is an isometry. The kernel of the action is the set of elements acting trivially, which is the centre of the copy, and the centre is zero; so the map from the copy to the orthogonal algebra is injective. Both spaces have dimension three, so the injective map is an isomorphism.

**Corollary.** The triplet is the adjoint module of the copy, and its isometry group is the copy itself.

*Proof.* The adjoint module is the copy acting on itself by the bracket, and the isometry group of a three-dimensional form of definite signature is the copy of rotations.

**The reading.** This is where the metric and the bracket agree: the form is invariant, the action is by isometries, and the bracket is the derivative of the action.

## The Killing Form

**Proposition.** The Killing form of the triplet is $-\tfrac{2}{5}$ times the restriction of the trace form, and the two forms have the same orthogonal complements.

*Proof.* The Killing form is invariant and non-degenerate on a semisimple algebra, and the restriction is invariant and non-degenerate; two invariant forms on the same irreducible module are proportional, so only the constant has to be computed. Evaluating on a generator gives the constant $-\tfrac25$, the same for the three axes.

**Corollary.** The ratio depends only on the label, so the restriction is the form in which the generators have the common norm $5$.

*Proof.* The constant is computed once on one generator and extended by symmetry.

**The reading.** Two invariant forms and one ratio: the trace form is natural to the operator space, the Killing form to the algebra, and on the triplet they differ by $-\tfrac25$.

## The Index and the Norm

**Proposition.** The common norm of a generator is the index of the module,

$$
g(J,J)=\tfrac13\,j(j+1)(2j+1)=5\quad\text{at } j=\tfrac32 ,
$$

and the Casimir of the module is $j(j+1)=\tfrac{15}{4}$.

*Proof.* The index of an irreducible module is the trace of the square of a generator in the normalised form, which is $\tfrac13j(j+1)(2j+1)$; at $j=\tfrac32$ the value is $\tfrac13\cdot\tfrac{15}{4}\cdot4=5$. The Casimir is the value of the quadratic element on the module, $\tfrac32\cdot\tfrac52$.

**Corollary.** With the trace form as metric the Casimir of the module is $-\tfrac34$, the value of the module divided by the norm of a generator.

*Proof.* The Casimir read with the metric is the quadratic element divided by the norm, that is $\tfrac{15}{4}$ divided by $5$.

**The reading.** A single number, the label, produces the dimension, the norm of a generator and the Casimir, so the form on the triplet is described completely without a basis.

## Orthogonality of the Carriers

**Proposition.** The four carriers are mutually orthogonal for the trace form, and the form on the operator space is the orthogonal sum of its four restrictions.

*Proof.* The pairing of two different carriers is an invariant bilinear map between non-isomorphic irreducible modules, hence zero by the lemma of Schur; the space is their direct sum, so the form is the sum of the restrictions.

**Corollary.** The restriction to the triplet is non-degenerate, and so is the restriction to each of the other three carriers.

*Proof.* The whole form is non-degenerate and the summands are mutually orthogonal, so no summand can be degenerate.

**The reading.** Orthogonality makes the four carriers independent objects: each carries its own form, its own bracket where it has one, and its own spectrum.

## Further Reading

- [The Spin-One Carrier: the Adjoint Triplet](the-spin-one-carrier-the-adjoint-triplet.html), for the generators and the brackets on which the form is evaluated
- [The Trace Form and Its Signature on the Two Halves](the-trace-form-and-its-inertia-on-the-two-halves.html), for the same form at the row of the elements
- [The Symmetric and Antisymmetric Parts of the Operator Space](the-symmetric-and-antisymmetric-parts-of-the-biquaternion-operator-space.html), for the form on the whole space and its two squares
- [The Spin-One Carrier and the Spectral Strata](the-spin-one-carrier-and-the-spectral-strata.html), for the spectrum read with the form in hand
- [The Adjoints and the Polar Decomposition of an Operator](the-adjoints-and-the-polar-decomposition-of-an-operator.html), for the star and the form as an inner product
