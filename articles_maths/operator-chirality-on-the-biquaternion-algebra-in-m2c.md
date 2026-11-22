# __Operator Chirality on the Biquaternion Algebra in $M_2(\mathbb{C})$__

## Introduction

**The question.** Every operator of the algebra has a slot: it may multiply on the left, on the right, on both ends, or on neither. The label is a membership in one of two four-dimensional images, and this article asks what the membership is in the display, which is the array of the operator in a chosen basis of $M_4(\mathbb{C})$.

**Why it is the same statement.** This is the in-depth matrix reading of [Operator Chirality on the Biquaternion Algebra](operator-chirality-on-the-biquaternion-algebra.html). The display $\mathsf M_2$ is an isomorphism of complex algebras, so it carries the two regular images, their intersection and their sum onto two four-dimensional subspaces of $M_4(\mathbb{C})$, their line and their seven-dimensional sum. The statements are the same statements and only the writing is new; the writing is an array of sixteen coefficients, and the slot label becomes a property of that array.

**What the article proves.** In this order. The left image is $\{\mathrm I_2\otimes A\}$ and the right image is $\{B^{\mathsf T}\otimes\mathrm I_2\}$ in the Peirce frame; each is four-dimensional, their intersection is the scalars and their sum is seven-dimensional. The swap of the two sides is the transposition of the coefficient array, and on the matrix it is the flip of the two tensor factors after a transpose. The swap is an anti-automorphism and its $\pm1$ eigenspaces are the symmetric and the antisymmetric coefficient arrays, of dimensions ten and six. The trace form is $\tfrac12\operatorname{tr}(XY)$ and the swap is its adjoint. The conjugation by $\natural$ exchanges the sides and moves the parameters, and its matrix form is a conjugation of each tensor factor. Chirality is not a grading, and the array shows why: the label is not additive and not linear.

**What the article does not do.** It does not decompose the operator space into its symmetric and antisymmetric parts in detail, which is [The Symmetric and Antisymmetric Parts of the Operator Space at $n=2$](the-symmetric-and-antisymmetric-parts-of-the-operator-space-at-n-2.html); it does not treat the Jordan and Lie structures of the two eigenspaces; and it does not enumerate the objects that are offered as chirality beyond the table that the source gives.

**Conventions.** The display is $\mathsf M_2(\tilde Q)=Q_t\mathrm I_2-i(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3)$, with units $\mathrm I_2,-i\sigma_1,-i\sigma_2,-i\sigma_3$. The trace is $2Q_t$ and the determinant is $N(\tilde Q)=Q_t^2+Q_x^2+Q_y^2+Q_z^2$. The carrier is read in the Peirce frame, with coordinate column $(y_{11},y_{21},y_{12},y_{22})^{\mathsf T}$, so that

$$
L_A=\mathrm I_2\otimes A,\qquad R_B=B^{\mathsf T}\otimes\mathrm I_2,\qquad L_AR_B=B^{\mathsf T}\otimes A .
$$

Any $4\times4$ array printed here is the axis-free array and not the Pauli array: the axis-free family is the unique representative, among the $96$ signed-permutation bases, whose sixteen operator arrays are signed permutations, so its entries are the multiplication table read aloud and every identity checked in it is an integer check ([$M_4(\mathbb{C})$ Axis-Free Representation : Operators](m4c-axis-free-representation-operators.html)). The Pauli and gamma arrays are a translation and are refused as primary, because one entry of one of their matrices is diagonal by privilege, which puts a spatial direction into the notation. The privilege is canonical and fixes no invariant.

**Boundaries.** The two regular representations are [$\operatorname{End}(M_2(\mathbb{C}))$ as an Algebra: the Regular Representation](end-m2c-as-an-algebra-the-regular-representation.html). The one-sided families are [Operators Acting on One Side in $M_2(\mathbb{C})$](operators-acting-on-one-side-in-m2c.html). The two-sided cone is [Operators Acting on Two Sides in $M_2(\mathbb{C})$](operators-acting-on-two-sides-in-m2c.html). The adjoint pair is [Adjoint Pair of $L$ and $R$ Operators in $M_2(\mathbb{C})$](adjoint-pair-of-l-and-r-operators-in-m2c.html). The $n=2$ spine is [The One-Sided Operators at $n=2$](the-one-sided-operators-at-n-2.html) and [The Length and the Two Ranks at $n=2$](the-length-and-the-two-ranks-at-n-2.html), and the display is [$M_2(\mathbb{C})$ Pauli Representation : Operators](m2c-pauli-representation-operators.html).

**Letters.** The coefficient array of an operator $M$ is $c(M)$, with entries $c_{\mu\nu}$ in the basis $L_{e_\mu}R_{e_\nu}$. The flip of the two tensor factors is $F$, with $F(X\otimes Y)F^{-1}=Y\otimes X$. The swap of the two slots is $\sigma$. The trace form is $\beta$.

## The Two Sides as Two Tensor Factors

**The left image.** The left multiplication $L_A(Y)=AY$ is, on the coordinate column, the matrix

$$
L_A=\mathrm I_2\otimes A=\begin{pmatrix}
a_{11}&a_{12}&0&0\\
a_{21}&a_{22}&0&0\\
0&0&a_{11}&a_{12}\\
0&0&a_{21}&a_{22}
\end{pmatrix},
$$

an array with two identical $2\times2$ blocks on the diagonal and zeros elsewhere. The image is four-dimensional, spanned by $\mathrm I_2\otimes(-i\sigma_k)$ and $\mathrm I_2\otimes\mathrm I_2$.

**The right image.** The right multiplication $R_B(Y)=YB$ is

$$
R_B=B^{\mathsf T}\otimes\mathrm I_2=\begin{pmatrix}
b_{11}&0&b_{21}&0\\
0&b_{11}&0&b_{21}\\
b_{12}&0&b_{22}&0\\
0&b_{12}&0&b_{22}
\end{pmatrix},
$$

the same construction with the blocks interleaved. The image is four-dimensional, spanned by $(-i\sigma_k)^{\mathsf T}\otimes\mathrm I_2$ and $\mathrm I_2\otimes\mathrm I_2$.

**The intersection.** The two arrays meet in the scalars. A matrix that is at once block diagonal with two equal blocks and interleaved with two equal blocks is a multiple of $\mathrm I_4$, so

$$
L(\mathbb{B})\cap R(\mathbb{B})=\mathbb{C}\,\mathrm I_4,\qquad
\dim\bigl(L+R\bigr)=4+4-1=7 .
$$

**The sum.** The seven-dimensional sum is the set of arrays $B^{\mathsf T}\otimes A$ with $A,B$ arbitrary $2\times2$ matrices, modulo the one relation $(\lambda A,\lambda^{-1}B)$. It is not a subalgebra, because the product of two such arrays is again of the form $B^{\mathsf T}\otimes A$ only when the coefficient arrays multiply to a rank-one array, which they do not in general.

**The coefficient array.** The sixteen arrays $L_{e_\mu}R_{e_\nu}$ are a basis of $M_4(\mathbb{C})$, of Hilbert–Schmidt norm two and pairwise orthogonal. The coefficient array of an operator is

$$
c(M)_{\mu\nu}=\tfrac14\operatorname{Tr}\bigl((L_{e_\mu}R_{e_\nu})^{\mathsf T}M\bigr),
\qquad
M=\sum_{\mu,\nu}c_{\mu\nu}L_{e_\mu}R_{e_\nu}.
$$

The chart $c$ is a linear isomorphism and not an algebra map: it turns products into a convolution on the four indices, not into the product of the arrays.

**The chart on the two images.** The left image is the set of arrays with only the first column nonzero, $c(M)_{\mu\nu}=0$ for $\nu\neq t$, and the right image is the set with only the first row nonzero, $c(M)_{\mu\nu}=0$ for $\mu\neq t$. The membership is therefore a support condition on the coefficient array, and the label takes four values:

| Label | Condition on $c(M)$ |
|---|---|
| left slot | support in the first column |
| right slot | support in the first row |
| both slots | support in the single entry $(t,t)$ |
| no single side | support outside the union of the row and the column |

**The fourth case.** The set of operators with no single side is the complement of a union of two subspaces, so it is not a subspace. It contains the generic operator, and its dimension is not defined by a count of coordinates but is the complement of a seven-dimensional union inside sixteen.

## The Swap of the Two Sides

**The definition.** The swap is defined on the coefficient array by transposition:

$$
\sigma(M)=\sum_{\mu,\nu}c_{\mu\nu}(M)\,L_{e_\nu}R_{e_\mu},
\qquad\text{so that}\qquad
c\bigl(\sigma(M)\bigr)=c(M)^{\mathsf T}.
$$

The definition uses no basis, because it permutes the two indices of a coordinate array, and a coordinate array is a basis-free object once the two-sided basis is fixed. It was checked on fifty random products that $\sigma(L_AR_B)=L_BR_A$.

**The matrix form.** On the $4\times4$ array the swap is the transpose followed by the flip of the two tensor factors:

$$
\sigma(M)=F\,M^{\mathsf T}F,
\qquad
F(X\otimes Y)F^{-1}=Y\otimes X .
$$

*Proof.* For a product, $M=B^{\mathsf T}\otimes A$, so $M^{\mathsf T}=B\otimes A^{\mathsf T}$ and $F M^{\mathsf T}F=A^{\mathsf T}\otimes B$, which is the array of $L_BR_A$. Both sides are linear in $M$ and the products span, so the identity holds everywhere. The residual on a hundred random products is below $10^{-15}$.

**Three properties.** The swap is an involution, it is an anti-automorphism, and it exchanges the two images:

$$
\sigma^2=\mathrm{id},\qquad
\sigma(XY)=\sigma(Y)\sigma(X),\qquad
\sigma\bigl(L(\mathbb{B})\bigr)=R(\mathbb{B}).
$$

The anti-automorphism is read on the arrays as $(c(X)c(Y))^{\mathsf T}=c(Y)^{\mathsf T}c(X)^{\mathsf T}$, which is the ordinary transpose rule; the check on twenty random pairs gives a residual below $2\cdot10^{-14}$.

**The swap is not inner.** An inner automorphism preserves products, and $\sigma$ reverses them, so no matrix $\mathsf S$ satisfies $\sigma(M)=\mathsf S M\mathsf S^{-1}$ for all $M$. The exchange of the sides is an operation on operators and is not a change of frame, a change of display or a choice of basis.

## The Trace Form

**The form.** On the display the trace form is

$$
\beta(X,Y)=\operatorname{Sc}(XY)=\tfrac12\operatorname{tr}(XY),
$$

complex-bilinear, symmetric and nondegenerate, with Gram matrix $E=\operatorname{diag}(1,-1,-1,-1)$ in the basis of units. The value at the identity is $\beta(\mathrm I_2,\mathrm I_2)=1$, so $\beta$ is the reduced trace form of $M_2(\mathbb{C})$.

**The adjoint identity.** For every pair of elements,

$$
\beta(L_AX,Y)=\tfrac12\operatorname{tr}(AXY)=\tfrac12\operatorname{tr}(XYA)=\beta(X,R_AY).
$$

The adjoint of a left multiplication with respect to $\beta$ is the right multiplication by the same matrix. In the swap notation,

$$
\beta\bigl(X\tilde Y,\tilde Z\bigr)=\beta\bigl(\tilde Y,\sigma(X)\tilde Z\bigr),
$$

so $\sigma$ is the adjoint operation of the trace form. This is the matrix proof of the source's theorem, and it uses only the cyclicity of the trace.

**The pairing of the two sides.** The identity shows that $L_A$ and $R_A$ are paired by $\beta$ and not merely exchanged by a formal rule. The bilinear form that pairs them is the plain bilinear form of the first article, and its Gram matrix $E$ has three negative entries: the form is not positive definite, and the adjoint with respect to it is not the Hilbert–Schmidt adjoint.

## The Two Eigenspaces

**The split.** The swap is an involution, so the operator space splits:

$$
M_4(\mathbb{C})=\operatorname{Fix}(\sigma)\oplus\operatorname{Neg}(\sigma),
\qquad
\dim\operatorname{Fix}(\sigma)=10,\quad \dim\operatorname{Neg}(\sigma)=6 .
$$

In the coefficient array the two summands are the symmetric and the antisymmetric arrays. The dimensions are the counts $\tfrac{4\cdot5}{2}=10$ and $\tfrac{4\cdot3}{2}=6$.

**The fixed part.** An operator is fixed exactly when its coefficient array is symmetric, $c(M)=c(M)^{\mathsf T}$. In the matrix it is the condition $M^{\mathsf T}=FMF$, which is a symmetry under the flip and not the ordinary symmetry of the array. The fixed part is the image of the symmetric square of the algebra, and its generic member has rank $4$.

**The negated part.** An operator is negated exactly when its coefficient array is antisymmetric. The part is spanned by the six differences $L_{e_\mu}R_{e_\nu}-L_{e_\nu}R_{e_\mu}$ for $\mu<\nu$, which are the commutators $[L_{e_\mu},R_{e_\nu}]$. In the matrix the generator is $B^{\mathsf T}\otimes A-A^{\mathsf T}\otimes B$, the antisymmetric part of a tensor.

**The two operations.** Neither part is closed under composition. The fixed part closes under the anti-commutator and is a Jordan algebra of dimension ten; the negated part closes under the commutator and is a Lie algebra of dimension six. Both statements follow from $\sigma(XY)=\sigma(Y)\sigma(X)$ in one line, and both are read on the arrays as the symmetry of $c(X)c(Y)\pm c(Y)c(X)$.

**A caution about dimensions.** The six arrays $L_{e_\mu}R_{e_\nu}$ with $\mu<\nu$ span a six-dimensional space, and its image under $\sigma$ is the span of the six complementary arrays with $\mu>\nu$. The two spaces meet only at zero and their sum is twelve-dimensional. A space of dimension six is therefore not the negated part, and the negated part is not the span of any six of the sixteen basis arrays. Equal dimensions never identify two subspaces.

## Conjugation Exchanges the Sides

**The map.** The quaternion conjugation is the matrix map $\Phi(A)=\sigma_2A^{\mathsf T}\sigma_2$, and it is an anti-automorphism of the display. Conjugating an operator by it, $X\mapsto\Phi X\Phi$, exchanges the sides and moves the parameters:

$$
\Phi\,L_A\,\Phi=R_{\Phi(A)},\qquad
\Phi\,R_B\,\Phi=L_{\Phi(B)} .
$$

*Proof.* Apply $\Phi$ to $L_A(\Phi(Y))=A\sigma_2Y^{\mathsf T}\sigma_2$: since $\Phi$ reverses products, the result is $Y\sigma_2A^{\mathsf T}\sigma_2=Y\Phi(A)=R_{\Phi(A)}(Y)$. The second identity is the same computation on the other side.

**The two exchangers compared.** The swap keeps the parameters and exchanges the slots; the conjugation exchanges the slots after applying $\Phi$ to the parameters. They agree on a left multiplier exactly when $\Phi(A)=A$, that is when $A$ is a real linear combination of $\mathrm I_2$ and the three $-i\sigma_k$ with real coefficients, and they differ everywhere else. The difference is the entrywise conjugation of the coefficients, and it is the origin of every phase in the corpus that comes from a change of side.

**The division of labour.** The swap defines the label and needs no display. The conjugation explains when two operators of opposite slots have arrays that agree up to a sign, and it belongs to the display. Neither is inner, and neither replaces the other.

## What Operator Chirality Is Not

**The table.** The source lists eleven objects that are offered as the home of chirality. In the display each has a matrix form, and none of them is the label.

| Object | Matrix form | Why it is not the label |
|---|---|---|
| a root | $A^2=\mathrm I_2$ | a condition on an element, not on an operator |
| an idempotent | $A^2=A$ | the same objection |
| a Peirce decomposition | four lines cut by two idempotents | the label's four cases are not lines |
| a Peirce basis | a basis of $M_2(\mathbb{C})$ | a display is not a membership |
| a spectrum | the list $+1,+1,-1,-1$ of one basis operator | a list of numbers is a consequence |
| a spinor | an element of a minimal left ideal | a vector, not an operator |
| the module $S$ | one minimal left ideal | needs a chosen point of a projective line |
| an ideal | a subspace with $M_2I\subseteq I$ | a subspace of the carrier |
| a Clifford algebra | a real algebra with a fixed inertia | fixes a dimension the images do not |
| a matrix unit | one $E_{ij}$ of a display | a basis operator is a sum of four |
| the basis operator | one $-iR_u$ | an example is not a definition |

**The spectrum of one basis operator.** For a unit vector $\vec u$ the operator $-iR_{\vec u}$ has matrix $-i(A^{\mathsf T}\otimes\mathrm I_2)$ with $A=\mathsf M_2(\vec u)$ and $A^2=-\mathrm I_2$. The eigenvalues of $A$ are $\pm i$, each twice, so the eigenvalues of $-iR_{\vec u}$ are $+1,+1,-1,-1$, verified numerically. The balance of the two signs is a theorem with two hypotheses, $u^2=-e_t$ and $\operatorname{Sc}u=0$, and a theorem with hypotheses about a chosen element cannot be the definition of a label that needs no element.

**The shape of the objection.** The label has four cases, two of which have no spectrum at all. A finite list of numbers in $\mathbb{C}$ cannot carry four cases, so no spectrum is the label.

## Why the Slot Label Is Not a Grading

**The requirement.** A grading of an algebra by a group would decompose the space into subspaces indexed by the group, with products landing in the component indexed by the product of the indices. The four labels fail the requirement twice.

**The failure of additivity.** The labels are not additive: $L_A+L_C$ has the left slot while $L_A+R_B$ has none. A grading is additive by construction, so no grading has these four classes as its components.

**The failure of closure under products.** The product of two operators with no single side can have a single side: $L_AR_B$ multiplied by $L_{A^{-1}}R_{B^{-1}}$ gives $\mathrm I_4$, which has both slots. A graded product would stay in a prescribed component.

**What the label is.** The label is a membership in a union of two subspaces and their intersection. It is a name, not a quantity: it is not linear, not additive and not signed, and no linear functional assigns it. The display shows the reason plainly: the four classes are a column, a row, one point of the array and the complement of the union, and a complement of a union of subspaces is not a subspace.

## Where $n=2$ Differs

**The number of slots.** At $n=2$ the carrier is four-complex-dimensional, each regular image is four-dimensional, the intersection is one and the sum is seven. The numbers $4,4,1,7$ are fixed by $n^2=4$ and would be $n^2,n^2,1,2n^2-1$ at order $n$. Here they are $4,4,1,7$ and the ladder stops at the next rung, $16$.

**The two tensor factors.** The carrier is $M_2(\mathbb{C})$ and the operator algebra is $M_2(\mathbb{C})\otimes M_2(\mathbb{C})$. The two factors are of the same size, which is why the swap can be written as the flip of two equal factors. At order $n$ the two factors are still equal, but here the flip has a two-element symmetry and the coefficient array is $4\times4$.

**The eigenspaces.** The dimensions ten and six are the counts of symmetric and antisymmetric $4\times4$ arrays. At order $n$ they are $\tfrac{n^2(n^2+1)}{2}$ and $\tfrac{n^2(n^2-1)}{2}$; here $10$ and $6$, and their sum is the sixteen of the operator space.

**Nothing else differs.** The two-sided cone, the length and the adjoint structures are the same statements, because they are statements about the tensor square and the tensor square is computed from $n^2=4$ alone.

## Summary

The two regular images are $\{\mathrm I_2\otimes A\}$ and $\{B^{\mathsf T}\otimes\mathrm I_2\}$, of dimension four each, meeting in the scalars and summing to seven dimensions. The label is a support condition on the coefficient array $c(M)$: a column for the left slot, a row for the right slot, the single entry $(t,t)$ for both, and the complement for no single side.

The swap of the two sides is transposition of the coefficient array and, on the matrix, the transpose followed by the flip of the tensor factors, $\sigma(M)=FM^{\mathsf T}F$. It is an involution and an anti-automorphism, it is not inner, and it is the adjoint of the trace form $\beta(X,Y)=\tfrac12\operatorname{tr}(XY)$, whose Gram matrix is $E$. Its eigenspaces are the symmetric and antisymmetric arrays, of dimensions ten and six, a Jordan algebra under the anti-commutator and a Lie algebra under the commutator.

The conjugation by $\natural$ is the matrix map $\Phi(A)=\sigma_2A^{\mathsf T}\sigma_2$, and it exchanges the sides after moving the parameters. The label is not a grading: it is not additive and not closed under products, and the array shows that its four classes are a column, a row, a point and a complement.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_A=\mathrm I_2\otimes A$ | left multiplication by $A$ |
| $R_B=B^{\mathsf T}\otimes\mathrm I_2$ | right multiplication by $B$ |
| $c(M)$ | coefficient array in the basis $L_{e_\mu}R_{e_\nu}$ |
| $\sigma$ | the swap of the two sides |
| $F$ | the flip of the two tensor factors |
| $\beta(X,Y)=\tfrac12\operatorname{tr}(XY)$ | the trace form |
| $\Phi(A)=\sigma_2A^{\mathsf T}\sigma_2$ | the quaternion conjugation in the display |
| $\operatorname{Fix}(\sigma),\operatorname{Neg}(\sigma)$ | symmetric and antisymmetric arrays, dimensions $10$ and $6$ |
| $E=\operatorname{diag}(1,-1,-1,-1)$ | Gram matrix of $\beta$ |

## Further Reading

- [Operator Chirality on the Biquaternion Algebra](operator-chirality-on-the-biquaternion-algebra.html), for the source definition of the slot label and its eleven rivals.
- [$\operatorname{End}(M_2(\mathbb{C}))$ as an Algebra: the Regular Representation](end-m2c-as-an-algebra-the-regular-representation.html), for the two regular images in the display.
- [Operators Acting on One Side in $M_2(\mathbb{C})$](operators-acting-on-one-side-in-m2c.html), for the two images, their intersection and their sum.
- [The Transposition of the Two Sides in $M_2(\mathbb{C})$](the-transposition-of-the-two-sides-in-m2c.html), for the swap and the two identities it satisfies.
- [The Symmetric and Antisymmetric Parts of the Operator Space at $n=2$](the-symmetric-and-antisymmetric-parts-of-the-operator-space-at-n-2.html), for the two eigenspaces as a Jordan and a Lie algebra.
- [The Two-Sided Operators and the Segre Cone at $n=2$](the-two-sided-operators-and-the-segre-cone-at-n-2.html), for the cone of products and the coefficient array.
