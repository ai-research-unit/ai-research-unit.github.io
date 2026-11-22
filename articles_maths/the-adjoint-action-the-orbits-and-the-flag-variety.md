# __The Adjoint Action, the Orbits and the Flag Variety__

## Introduction

**The subject.** The invertible operators act on the operator space by conjugation, $O\mapsto UOU^{-1}$, and the orbits of that action are the similarity classes. The article computes the invariants along an orbit, the dimension of an orbit from its stabiliser, the orbit–stabiliser count for the cyclic operators, the orbits of the idempotents, the closure order, and the infinitesimal picture. The count is $256=240+16$: the orbit is the frame and the centraliser is what the frame cannot move, which is the whole space at a scalar and only the polynomials at a cyclic operator.

**The order of the article.** The action and its invariants come first; the orbit dimensions and the orbit–stabiliser count second. The orbits of the idempotents and the flag variety of the algebra follow, then the closure order, and the infinitesimal picture closes the article.

**It assumes** *$\operatorname{End}(\mathbb{B})$ as an Algebra: the Regular Representation*, *The Operators of the Peirce Decomposition* and *The Spectrum of a Biquaternion*. **The row of the elements is** where the unit group of the algebra acts on the four-dimensional algebra and the orbits are the similarity classes of its elements; here the group is the unit group of the operator algebra, of dimension $255$ projectively, and it acts on the sixteen operators.

**The result in one line.** An orbit has dimension $256-\dim\mathfrak z(O)$, so a cyclic operator has an orbit of dimension $240$ with a centraliser of dimension sixteen, a scalar has the orbit of a point, and the idempotents of rank $k$ form one orbit of dimension $2k(16-k)$, of which the primitive idempotents of the algebra give the case of dimension two.

**Boundaries.** The finite shadow of the action is *The Extraspecial Group of the Two-Sided Operators*; the decomposition of the space into the blocks of an idempotent is *The Operators of the Peirce Decomposition*; the spectral data of the parameters is *The Spectrum of a Biquaternion*.

Nothing below is a statement of physics. The units are $e_t,\vec e_x,\vec e_y,\vec e_z$ with $\vec e_k^2=-e_t$ and the products cyclic; an element of the algebra is $a=a_te_t+a_x\vec e_x+a_y\vec e_y+a_z\vec e_z$ with complex coefficients; $N(a)=a_t^2+a_x^2+a_y^2+a_z^2$ is the norm; the operator space is $\operatorname{End}(\mathbb{B})$, of complex dimension sixteen; $L_a$, $R_b$ are the one-sided operators and $T_{a,b}=L_aR_b$ the two-sided one.

## The Action and Its Invariants

**Definition.** For an invertible operator $U$ and an operator $O$ the **adjoint action** is $\operatorname{Ad}_U(O)=UOU^{-1}$.

**Proposition.** The adjoint action is an action of the group of invertible operators by automorphisms of the operator algebra, and it preserves the trace, the determinant and the whole spectrum.

*Proof.* Conjugation respects products and sums, so it is an automorphism of the algebra of operators. The trace and the determinant are invariant under conjugation, and so is the characteristic polynomial, hence the spectrum.

**Corollary.** The scalar operators are fixed, and the orbit of a scalar is the point itself.

*Proof.* A scalar commutes with every operator.

**Corollary.** Two operators in the same orbit have the same characteristic polynomial, and the orbit is contained in the set of the operators with that spectrum.

*Proof.* The invariance of the characteristic polynomial, and the reading of its roots.

**The reading.** The action is the operator form of a change of frame, and its invariants are the spectral data. The orbit is the set of the operators that look the same from a different frame. The question of the article is how large those sets are, and the answer is a count of dimensions.

## The Orbit Dimensions

**Theorem.** The orbit of an operator $O$ has dimension
$$
\dim\operatorname{Ad}(O)=256-\dim\mathfrak z(O),
$$
where $\mathfrak z(O)$ is the centraliser of $O$ in the operator algebra.

*Proof.* The orbit–stabiliser theorem: the stabiliser of $O$ is its centraliser, the group of the invertible operators has dimension $255$ projectively, and the stabiliser in the projective group is the centraliser modulo the scalars, of dimension $\dim\mathfrak z(O)-1$. The difference is $255-\dim\mathfrak z(O)+1$.

**Corollary.** A cyclic operator has a centraliser of dimension sixteen and an orbit of dimension $240$.

*Proof.* An operator is **cyclic** when there is an $X$ whose images $X,OX,O^{2}X,\dots,O^{15}X$ span the space. For a cyclic operator the centraliser consists of the polynomials in the operator, which form an algebra of dimension sixteen, since the powers from the zeroth to the fifteenth are independent and every polynomial reduces to them.

**Corollary.** The cyclic operators form an open dense set, and it is the union of the orbits of dimension $240$.

*Proof.* Cyclicity is the non-vanishing of the determinant of the sixteen vectors $X,OX,\dots,O^{15}X$, a polynomial condition in the pair $(O,X)$, so the set of the $O$ for which some $X$ works is open; its complement is the set of the operators whose minimal polynomial has degree below sixteen, a proper closed subset over the complex numbers.

**Corollary.** The orbit of a scalar is a point, and the orbit of an idempotent of rank $k$ has dimension $2k(16-k)$.

*Proof.* The scalar has the whole operator algebra as its centraliser, of dimension $256$. An idempotent $E$ of rank $k$ commutes with exactly the operators carrying its image into itself and its kernel into itself, a space of dimension $k^{2}+(16-k)^{2}$, so the orbit has dimension $256-k^{2}-(16-k)^{2}=2k(16-k)$.

**The reading.** The size of an orbit measures the failure of the operator to be symmetric. The scalars commute with everything and sit in a point; a cyclic operator commutes with almost nothing and sweeps the largest orbit. The two extremes are separated by the dimension of the centraliser, and that dimension is the only datum the count needs.

## The Orbit-Stabiliser Count

**Proposition.** The centraliser of an operator is a subalgebra of the operator algebra containing the identity and the operator, and its dimension is at least one, exactly sixteen at a cyclic operator and $256$ at a scalar.

*Proof.* The centraliser is closed under sums and products, contains the identity and the operator, and contains the algebra of the polynomials in the operator, whose dimension is the degree of the minimal polynomial, sixteen for a cyclic operator and one for a scalar.

**Corollary.** No orbit has dimension greater than $240$, and the cyclic operators attain the bound.

*Proof.* The bound $256-16=240$ from the proposition, and the previous computation of the cyclic case.

**The reading.** The count $256=240+16$ is the operator reading of the decomposition of an operator into a spectrum and a frame. The sixteen dimensions of the centraliser are the polynomials, the $240$ of the orbit are the frames, and the spectrum is the transverse parameter that labels the orbit inside the open set of the cyclic operators.

## The Flag Variety of the Idempotents

**Definition.** An operator $E$ with $E^{2}=E$ is an **idempotent**; its image and its kernel are complementary subspaces of the algebra, and its rank is the dimension of the image.

**Theorem.** The idempotents of rank $k$ form a single orbit, of dimension $2k(16-k)$, parametrised by the pairs of complementary subspaces of dimensions $k$ and $16-k$.

*Proof.* An idempotent is determined by its image $M$ and its kernel $K$, which are complementary, and conversely a pair of complementary subspaces determines the projection onto the first along the second. The group of invertible operators acts transitively on the pairs with the two dimensions fixed, so there is one orbit, and its dimension is the dimension computed above.

**Corollary.** The idempotents of rank one are parametrised by a line and a hyperplane transverse to it, a family of dimension $30$.

*Proof.* The formula with $k=1$ gives $2\cdot15=30$; the lines form a projective fifteen-space and the hyperplanes transverse to a fixed line an open part of the dual projective fifteen-space.

**Corollary.** The primitive idempotents of the algebra itself form one orbit of dimension two, parametrised by the pairs of distinct lines of the two-dimensional module of the algebra.

*Proof.* The algebra is the algebra of the endomorphisms of a two-dimensional module, and a primitive idempotent is the projection onto a line along a complementary line; the pairs of distinct lines of a plane form a family of dimension $1+1=2$, and the unit group acts transitively on them. The four Peirce idempotents of a decomposition are four points of this family.

**The reading.** The flag variety appears twice. Inside the algebra it is the variety of the pairs of lines of the module, of dimension two, and it is the parameter space of the primitive idempotents. Inside the operator space it is the variety of a subspace and a complementary one, and the rank records the pair of dimensions. The passage from the one to the other is the Peirce decomposition, which turns each idempotent into a splitting of the sixteen.

## The Closure Order and the Infinitesimal Picture

**Proposition.** The closure of the orbit of an idempotent of rank $k$ contains the orbits of the idempotents of every rank smaller than $k$, and in particular the zero operator.

*Proof.* A family of idempotents of rank $k$ degenerating by letting the image fall inside the kernel gives an idempotent of smaller rank in the limit; iterating reaches zero.

**Corollary.** The closure order on the orbits of the idempotents is the order on the ranks, and the closed orbits are those of the scalars and of the zero operator.

*Proof.* The proposition, and the constancy of the rank on an orbit.

**Proposition.** The tangent space of the orbit at $O$ is the image of the map $\xi\mapsto[\xi,O]$ from the operator algebra into itself, and its dimension is $256-\dim\mathfrak z(O)$.

*Proof.* The derivative of the conjugation at the identity is the commutator, and the kernel of the commutator map is the centraliser.

**Corollary.** The rank of the commutator map is the dimension of the orbit, so an operator is a regular point of its orbit exactly when its centraliser is as small as the polynomial algebra allows.

*Proof.* The rank of a linear map is the dimension of the source minus the dimension of the kernel, and the kernel is the centraliser.

**The reading.** The infinitesimal picture reproduces the global one: the tangent space of an orbit is the image of the commutator, and its codimension is the centraliser. The closure order adds the degeneration of the idempotents. Together they stratify the sixteen by the spectral type, and the stratification is the operator reading of the decomposition of the algebra into its two minimal left ideals.

## Further Reading

- [The Operators of the Peirce Decomposition](the-operators-of-the-peirce-decomposition.html), for the idempotents and their blocks.
- [The Extraspecial Group of the Two-Sided Operators](the-extraspecial-group-of-the-two-sided-operators.html), for the finite shadow of the action.
- [The Spectrum of a Biquaternion](the-spectrum-of-a-biquaternion.html), for the spectral data of the parameters.
- [$\operatorname{End}(\mathbb{B})$ as an Algebra: the Regular Representation](end-b-as-an-algebra-the-regular-representation.html), for the operator algebra on which the action takes place.
