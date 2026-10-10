# __Two-Sided Operators on the General Plain Algebra of Biquaternions__

## Introduction

Let $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ be the biquaternion algebra with its natural conjugation ${}^{\natural}$ and the general plain bilinear form

$$
\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q),
$$

whose Gram matrix in the basis $e_{0},e_{1},e_{2},e_{3}$ is $\mathrm{diag}(1,-1,-1,-1)$, and let $F^{\approx}$ be the associate, or transpose, of a $\mathbb{C}$-linear map for this form (*Association and the Transpose on the Biquaternion Algebra*).

For $\tilde A,\tilde B\in\mathbb{B}$ define the **two-sided operator**

$$
L_{\tilde A}R_{\tilde B}:\mathbb{B}\longrightarrow\mathbb{B},\qquad
\bigl(L_{\tilde A}R_{\tilde B}\bigr)(\tilde Y)=\tilde A\,\tilde Y\,\tilde B ,
$$

the product of a left and a right multiplication, with the two parameters independent. These operators are the subject of the article. They contain the one-sided ones as the two boundary cases $\tilde B=e_{0}$ and $\tilde A=e_{0}$, they contain every inner automorphism, and they are the elements of the enveloping algebra $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{op}}$ read on the algebra itself.

The article is the parallel of *One-Sided Operators on the General Plain Algebra of Biquaternions*, section for section, and the parallel is what isolates the cost of the second parameter. Three things change. The composition law **reverses the second slot**, $\tilde B$ and $\tilde D$ exchanging their places, because the right multiplications form an anti-representation. The adjoint **swaps the two parameters**, $(L_{\tilde A}R_{\tilde B})^{\approx}=L_{\tilde B}R_{\tilde A}$, because association is the transpose for the plain form, whereas the Hermitian dagger and the quaternionic adjoint keep the parameter they act on. And the criteria become criteria on the **product** of the parameters: self-adjointness is $\tilde B=\lambda\tilde A$, preservation of the form is $\tilde B\tilde A=\pm e_{0}$, multiplicativity is $\tilde A\tilde B=e_{0}$. No norm enters any of the three, which is the second sharp difference from the quaternionic pair, where the corresponding criteria turn on $N$.

The algebra, the conjugations and the remarkable subspaces are *Biquaternions as a Vector Space over $\mathbb{C}$*, *The Group of Involutions* and *Introduction to the Remarkable Subspaces*; the form and its pairings are *The Four Pairings of the Biquaternion Algebra*; the enveloping algebra and the two-sided operators as its elements are *The Enveloping Algebra of the Biquaternion Algebra and the Bi-module Structure*; the one-sided factors are *One-Sided Operators on the General Plain Algebra of Biquaternions*.

## The Two-Sided Family

**Definition.** For $\tilde A,\tilde B\in\mathbb{B}$ the **two-sided operator of the pair $(\tilde A,\tilde B)$** is the $\mathbb{C}$-linear map

$$
\bigl(L_{\tilde A}R_{\tilde B}\bigr)(\tilde Y)=\tilde A\,\tilde Y\,\tilde B .
$$

**Proposition (the family contains the one-sided operators).** With the unit in one slot,

$$
L_{\tilde A}R_{e_{0}}=L_{\tilde A},\qquad L_{e_{0}}R_{\tilde B}=R_{\tilde B}.
$$

The family is therefore the two-parameter extension of the one-sided pair, and the criteria below specialise to the criteria of the one-sided article at $\tilde B=e_{0}$.

*Proof.* The unit acts by the identity in each slot.

**Proposition (bilinearity and the spanning set).** The assignment $(\tilde A,\tilde B)\mapsto L_{\tilde A}R_{\tilde B}$ is bilinear and injective in each slot when the other parameter is fixed and a unit. The sixteen operators $e_n[\,]e_m$ are linearly independent and therefore form a basis of $\mathrm{End}_{\mathbb{C}}(\mathbb{B})$:

$$
\dim_{\mathbb{C}}\mathrm{Span}\{\,L_{\tilde A}R_{\tilde B}\,\}=16 .
$$

*Proof.* Bilinearity is the distributivity of the product. For the independence, the enveloping algebra $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{op}}$ is isomorphic to $\mathrm{End}_{\mathbb{C}}(\mathbb{B})$ through $A\otimes B\mapsto L_AR_B$, and it has complex dimension $16$ (*The Enveloping Algebra of the Biquaternion Algebra and the Bi-module Structure*); the independence of the sixteen basis elements was verified by elimination on their matrices. Injectivity in the first slot at a unit $\tilde B$ follows from $L_{\tilde A}R_{\tilde B}(e_{0})=\tilde A\tilde B$ and the invertibility of $\tilde B$.

**Remark (the image is the decomposable tensors).** Under the isomorphism $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{op}}\to\mathrm{End}_{\mathbb{C}}(\mathbb{B})$ the two-sided operators are the images of the **decomposable** tensors, and a general endomorphism is a sum of them. That is the precise sense in which the two-sided family is the algebraic skeleton of the full operator algebra, and it is also why a sum of two-sided operators need not be two-sided: the decomposable tensors do not form a subspace.

## The Composition Law

**Theorem (composition).** For all $\tilde A,\tilde B,\tilde C,\tilde D\in\mathbb{B}$,

$$
\bigl(L_{\tilde A}R_{\tilde B}\bigr)\circ\bigl(L_{\tilde C}R_{\tilde D}\bigr)=L_{\tilde A\tilde C}\,R_{\tilde D\tilde B},
$$

the parameters of the second slot reversing their order.

*Proof.* $\tilde A\bigl(\tilde C\tilde Y\tilde D\bigr)\tilde B=\tilde A\tilde C\,\tilde Y\,\tilde D\tilde B$ by associativity. Verified on random quadruples.

**Corollary (the family is a monoid with reversed right factors).** The composition law makes the set of two-sided operators a submonoid of $\mathrm{End}_{\mathbb{C}}(\mathbb{B})$, isomorphic to the image of the monoid $\mathbb{B}\times\mathbb{B}^{\mathrm{op}}$ under the bilinear map, with multiplication $(\tilde A,\tilde B)(\tilde C,\tilde D)=(\tilde A\tilde C,\tilde D\tilde B)$. The reversal in the second factor is the reason the family is not a direct product of two copies of the algebra.

**Corollary (invertibility and the units).** The operator $L_{\tilde A}R_{\tilde B}$ is invertible if and only if $\tilde A$ and $\tilde B$ are units, with inverse

$$
\bigl(L_{\tilde A}R_{\tilde B}\bigr)^{-1}=L_{\tilde A^{-1}}R_{\tilde B^{-1}} .
$$

The group of invertible two-sided operators is therefore the image of $\mathbb{B}^{\times}\times\mathbb{B}^{\times}$, and the kernel of the parametrisation is $\{(\lambda e_{0},\lambda^{-1}e_{0})\}$: the two-sided operator is the identity exactly for $\tilde A\tilde B=e_{0}$ with $\tilde A$ central.

*Proof.* The inverse is verified by the composition law. For the converse, if the operator is invertible then it is injective, so $\tilde A$ and $\tilde B$ are units: a nonzero kernel of $\tilde A$, say $\tilde A\tilde X=0$, gives $L_{\tilde A}R_{\tilde B}(\tilde X\tilde Y)=0$ for every $\tilde Y$. For the kernel of the parametrisation, $L_{\tilde A}R_{\tilde B}=\mathrm{id}$ reads $\tilde A\tilde Y\tilde B=\tilde Y$ for all $\tilde Y$; at $\tilde Y=e_{0}$ this gives $\tilde A\tilde B=e_{0}$, and substituting back gives $\tilde A\tilde Y=\tilde Y\tilde A$ for all $\tilde Y$, so $\tilde A$ is central and $\tilde B=\tilde A^{-1}$ has the same central value. Verified on random units.

**Corollary (the powers stay in the family).** For every $n\ge1$,

$$
\bigl(L_{\tilde A}R_{\tilde B}\bigr)^{n}=L_{\tilde A^{n}}R_{\tilde B^{n}} .
$$

*Proof.* Induction on the composition law. The corollary is the reason the exponential of a two-sided operator generally leaves the family: $\exp(L_{\tilde A}R_{\tilde B})$ is the operator $\tilde Y\mapsto\sum_{n\ge0}\frac{1}{n!}\tilde A^{n}\tilde Y\tilde B^{n}$, and a sum of decomposable tensors $\tilde A^{n}\otimes\tilde B^{n}$ is decomposable in degenerate cases only. In the one-sided case the same computation gives $\exp(L_{\tilde A})=L_{e^{\tilde A}}$ and $\exp(R_{\tilde B})=R_{e^{\tilde B}}$, because the parameter enters once and the series is the exponential of the parameter.

## The Adjoint and the Swap

**Theorem (the adjoint exchanges the parameters).** For all $\tilde A,\tilde B\in\mathbb{B}$,

$$
\bigl(L_{\tilde A}R_{\tilde B}\bigr)^{\approx}=L_{\tilde B}R_{\tilde A}.
$$

*Proof.* The transpose of a composite reverses the order, $(FG)^{\approx}=G^{\approx}\circ F^{\approx}$ (*Association and the Transpose on the Biquaternion Algebra*), and the transposes of the factors are the crossed one-sided operators, $(L_{\tilde A})^{\approx}=R_{\tilde A}$ and $(R_{\tilde B})^{\approx}=L_{\tilde B}$ (*One-Sided Operators on the General Plain Algebra of Biquaternions*):

$$
\bigl(L_{\tilde A}R_{\tilde B}\bigr)^{\approx}=\bigl(R_{\tilde B}\bigr)^{\approx}\bigl(L_{\tilde A}\bigr)^{\approx}=L_{\tilde B}R_{\tilde A}.
$$

Verified on random pairs.

**Remark (swap, not conjugation).** The adjoint of a two-sided operator is a two-sided operator with the two parameters interchanged. The quaternionic pair of the corpus has the opposite behaviour: there the adjoint for the quaternionic form keeps the parameter, $(L_{\tilde A})^{N}=L_{\tilde A^{\natural}}$ and $(\Theta_{\tilde A})^{N}=\Theta_{\tilde A^{\natural}}$, so a type criterion is a criterion on one parameter. Here every type criterion is symmetric or antisymmetric in the pair $(\tilde A,\tilde B)$, and the whole article turns on that single difference. This is §*The Adjoint and the Swap* referred to by the one-sided article.

## The Self-Adjoint and the Skew-Adjoint Sectors

**Theorem (the self-adjoint criterion).** For $\tilde A\neq0$ the operator $L_{\tilde A}R_{\tilde B}$ is self-adjoint if and only if the two parameters are proportional,

$$
\bigl(L_{\tilde A}R_{\tilde B}\bigr)^{\approx}=L_{\tilde A}R_{\tilde B}
\iff \tilde B=\lambda\tilde A\quad\text{for some }\lambda\in\mathbb{C}.
$$

Consequently the self-adjoint two-sided operators are the scalar multiples $\lambda\,L_{\tilde A}R_{\tilde A}$ of the diagonal products, together with the zero operator.

*Proof.* By the swap theorem, self-adjointness is $L_{\tilde B}R_{\tilde A}=L_{\tilde A}R_{\tilde B}$, that is $\tilde B\tilde Y\tilde A=\tilde A\tilde Y\tilde B$ for all $\tilde Y$. At $\tilde Y=e_{0}$ the two parameters commute. Substitute $\tilde Y=\tilde A^{-1}\tilde C\tilde A^{-1}$ for an arbitrary $\tilde C$, which is legitimate when $\tilde A$ is a unit: the identity becomes $\tilde B\tilde A^{-1}\tilde C=\tilde C\tilde A^{-1}\tilde B$ for all $\tilde C$, so $\tilde B\tilde A^{-1}$ is central, that is $\tilde B=\lambda\tilde A$. Conversely $\tilde B=\lambda\tilde A$ gives $\tilde B\tilde Y\tilde A=\lambda\tilde A\tilde Y\tilde A=\tilde A\tilde Y\lambda\tilde A=\tilde A\tilde Y\tilde B$. The case of a non-unit $\tilde A$ is the same computation with the parameter of the other slot, or follows by evaluating the identity at $\tilde Y=e_{0}$ and using centrality. Verified on random pairs, on central pairs and on null parameters.

**Theorem (the skew sector is trivial).** No nonzero two-sided operator is skew-adjoint:

$$
\bigl(L_{\tilde A}R_{\tilde B}\bigr)^{\approx}=-L_{\tilde A}R_{\tilde B}
\iff L_{\tilde A}R_{\tilde B}=0 .
$$

*Proof.* Skew-adjointness is $L_{\tilde B}R_{\tilde A}=-L_{\tilde A}R_{\tilde B}$, that is $\tilde B\tilde Y\tilde A=-\tilde A\tilde Y\tilde B$ for all $\tilde Y$. Taking the scalar part and using the cyclicity of $\mathrm{Sc}$,

$$
\mathrm{Sc}\bigl(\tilde B\tilde Y\tilde A\bigr)=\mathrm{Sc}\bigl(\tilde Y\tilde A\tilde B\bigr)
=-\mathrm{Sc}\bigl(\tilde A\tilde Y\tilde B\bigr)=-\mathrm{Sc}\bigl(\tilde Y\tilde A\tilde B\bigr),
$$

so $\mathrm{Sc}(\tilde Y\tilde A\tilde B)=0$ for all $\tilde Y$, and the non-degeneracy of the form gives $\tilde A\tilde B=0$; the same argument with the parameters read in the other order gives $\tilde B\tilde A=0$. At $\tilde Y=e_{0}$ the defining identity then reads $\tilde B\tilde A=-\tilde A\tilde B$, so both products vanish. A zero divisor pair with $\tilde A\tilde B=\tilde B\tilde A=0$ and both parameters nonzero nevertheless fails the identity on a general element, and the cases were settled by elimination: for every fixed nonzero $\tilde B$, both null and non-null, the linear system in $\tilde A$ has only the solution $\tilde A=0$.

**Corollary (the two sectors at the boundary).** At $\tilde B=e_{0}$ the two criteria of this section give the one-sided criteria: $\tilde B=\lambda\tilde A$ becomes $\tilde A$ central, and the skew condition becomes $\tilde A=0$. The one-sided type criteria are therefore the boundary case of the two-sided ones, and the pair of articles is one theorem read on a family and on its slice.

## Automorphisms of the Form and Multiplicative Operators

**Theorem (the automorphisms of the form inside the family).** The operator $L_{\tilde A}R_{\tilde B}$ preserves the general plain bilinear form,

$$
\bigl\langle L_{\tilde A}R_{\tilde B}\tilde X,\ L_{\tilde A}R_{\tilde B}\tilde Y\bigr\rangle=\langle\tilde X,\tilde Y\rangle\qquad\text{for all }\tilde X,\tilde Y,
$$

if and only if $\tilde B\tilde A=\pm e_{0}$, that is if and only if $\tilde B=\pm\tilde A^{-1}$. In that case the operator is $\pm\mathrm{Ad}_{\tilde A}$, the inner automorphism of $\tilde A$ up to sign.

*Proof.* If the operator preserves the form it is injective, because the form is non-degenerate, hence $\tilde A$ and $\tilde B$ are units. Put $\tilde M=\tilde B\tilde A$, so that $\tilde B=\tilde M\tilde A^{-1}$, and compute with the cyclicity of the scalar part:

$$
\mathrm{Sc}\bigl(\tilde A\tilde X\tilde B\tilde A\tilde Y\tilde B\bigr)
=\mathrm{Sc}\bigl(\tilde A\tilde X\tilde M\tilde Y\tilde M\tilde A^{-1}\bigr)
=\mathrm{Sc}\bigl(\tilde M\tilde X\tilde M\tilde Y\bigr)
=\bigl\langle\tilde X,\tilde M\tilde Y\tilde M\bigr\rangle .
$$

Preservation is therefore equivalent to $\tilde M\tilde Y\tilde M=\tilde Y$ for all $\tilde Y$, which by the one-sided theorem forces $\tilde M=\pm e_{0}$ (*One-Sided Operators on the General Plain Algebra of Biquaternions*, §*Which Multiplications Preserve the Form*). Conversely $\tilde B=\tilde A^{-1}$ gives the inner automorphism, which preserves the form, and $\tilde B=-\tilde A^{-1}$ gives its negative, which preserves the form up to the sign $(-1)^{2}=1$. Verified on random units and on random signed inverses.

**Theorem (the multiplicative operators).** The operator $L_{\tilde A}R_{\tilde B}$ is multiplicative,

$$
\bigl(L_{\tilde A}R_{\tilde B}\bigr)(\tilde X)\bigl(L_{\tilde A}R_{\tilde B}\bigr)(\tilde Y)=\bigl(L_{\tilde A}R_{\tilde B}\bigr)(\tilde X\tilde Y)\qquad\text{for all }\tilde X,\tilde Y,
$$

if and only if $\tilde A\tilde B=e_{0}$, that is $\tilde B=\tilde A^{-1}$; and then it is the inner automorphism $\mathrm{Ad}_{\tilde A}$, an automorphism of the algebra for every unit $\tilde A$.

*Proof.* The left side is $\tilde A\tilde X\tilde B\tilde A\tilde Y\tilde B$ and the right side is $\tilde A\tilde X\tilde Y\tilde B$, so with $\tilde M=\tilde A\tilde B$ the identity reads $\tilde A\tilde X\tilde M\tilde Y\tilde B=\tilde A\tilde X\tilde Y\tilde B$ for all $\tilde X,\tilde Y$. At $\tilde X=e_{0}$ and for units $\tilde A,\tilde B$ this is $\tilde M\tilde Y=\tilde Y$ for all $\tilde Y$, hence $\tilde M=e_{0}$, that is $\tilde B=\tilde A^{-1}$; conversely $\tilde A\tilde B=e_{0}$ makes the two sides equal for all $\tilde X,\tilde Y$, and the operator is $\tilde Y\mapsto\tilde A\tilde Y\tilde A^{-1}$. Verified on random units and on random non-inverse pairs.

**Corollary (multiplicative and form preserving).** The two-sided operators that are multiplicative and preserve the form at once are exactly the inner automorphisms $\mathrm{Ad}_{\tilde A}$ with $\tilde A$ a unit, without the sign $-\mathrm{Ad}_{\tilde A}$: the sign that the criterion of the first theorem allows is excluded by multiplicativity.

**Corollary (the partial law of the central product).** Suppose the product of the two parameters is central, that is $\tilde B\tilde A=\mu e_{0}$ with $\mu=\mathrm{Sc}(\tilde B\tilde A)$. Then for all $\tilde X,\tilde Y$,

$$
\bigl(L_{\tilde A}R_{\tilde B}\tilde X\bigr)\bigl(L_{\tilde A}R_{\tilde B}\tilde Y\bigr)
=(\tilde B\tilde A)\,\bigl(L_{\tilde A}R_{\tilde B}\bigr)(\tilde X\tilde Y)
=\mu\,\bigl(L_{\tilde A}R_{\tilde B}\bigr)(\tilde X\tilde Y),
$$

and the multiplier is the central scalar $\tilde B\tilde A$, not a norm. The condition is automatic for $\tilde B=\tilde A^{-1}$, which is the exact criterion of the theorem above, but it is weaker: it holds for every pair whose product falls in the centre $\mathbb{C}e_{0}$, and the operator is then multiplicative up to that central scalar.

*Proof.* $\tilde B\tilde A$ is central by hypothesis, so it may be moved across $\tilde X$ in $\tilde A\tilde X(\tilde B\tilde A)\tilde Y\tilde B$; substituting $\tilde B\tilde A=\mu e_{0}$ gives the second form. Verified with the product forced central, on $400$ random pairs and random central scalars, and with the scalar $\mu$ read off the parameter.

**Remark (no norm enters, and the law is the weaker for it).** The quaternionic pair of the corpus reads the same two questions through the norm and carries the correspondingly stronger law: there $\Theta_{\tilde A}(\tilde X)\Theta_{\tilde A}(\tilde Y)=N(\tilde A)\,\Theta_{\tilde A}(\tilde X\tilde Y)$ holds for **every** parameter, with the norm as the scalar, and genuine multiplicativity up to a scalar is the condition $N(\tilde A)=1$. Here the criteria are $\tilde B\tilde A=\pm e_{0}$ and $\tilde A\tilde B=e_{0}$: conditions on the product of the two parameters, in which no norm and no conjugation appears, and the partial law above holds only when that product is central. The two shapes are not the same theorem with different letters; the plain form carries no twist for a norm to absorb, so it loses the parameter-free law and keeps the criterion. Verified: with $\tilde B\tilde A$ non-central, no scalar whatever makes the product law hold.

## Worked Examples

**The identity and its multiples.** $L_{e_{0}}R_{e_{0}}=\mathrm{id}$, self-adjoint and form preserving; the central multiples $\lambda\,\mathrm{id}=L_{\lambda e_{0}}R_{e_{0}}$ are self-adjoint for every $\lambda$, preserve the form only for $\lambda=\pm1$, and are multiplicative only for $\lambda=1$: the three criteria are genuinely different, and the example separates them.

**A mixed operator.** The operator $\tilde Y\mapsto e_{1}\tilde Ye_{2}=L_{e_{1}}R_{e_{2}}$ has $\tilde B\tilde A=e_{2}e_{1}=-e_{3}$, so by the criteria it is neither self-adjoint (the parameters are not proportional), nor form preserving ($-e_{3}\neq\pm e_{0}$), nor multiplicative. Its adjoint is $L_{e_{2}}R_{e_{1}}$, the parameter pair exchanged, and the two operators differ, since $e_{1}e_{3}e_{2}$ and $e_{2}e_{3}e_{1}$ have opposite signs.

**An inner automorphism.** For the pure unit $\tilde A=e_{1}$ one has $\tilde A^{-1}=-e_{1}$, so

$$
\mathrm{Ad}_{e_{1}}=L_{e_{1}}R_{e_{1}^{-1}}=L_{e_{1}}R_{-e_{1}},
$$

and the three criteria hold at once: the parameters are proportional with $\lambda=-1$, so the operator is self-adjoint; $\tilde B\tilde A=(-e_{1})e_{1}=e_{0}$, so it preserves the form; and $\tilde B=\tilde A^{-1}$, so it is multiplicative. It is the least degenerate two-sided operator after the identity, and the example exercises the three criteria on one object.

**A self-adjoint operator with a null parameter.** For $\tilde A=e_{0}+ie_{3}$, a zero divisor with $\tilde A^{2}=2\tilde A\neq e_{0}$, the diagonal operator $L_{\tilde A}R_{\tilde A}$ is self-adjoint by the criterion $\tilde B=\lambda\tilde A$ with $\lambda=1$, although the parameter is not a unit. The example records that self-adjointness is a condition on the pair and not on invertibility, in contrast with the form-preserving criterion, which forces both parameters to be units.

**A diagonal operator multiplicative up to sign.** For the pure unit $\tilde A=\tilde B=e_{1}$ the product of the parameters is $\tilde B\tilde A=e_{1}^{2}=-e_{0}$, central, so the partial law applies with the scalar $-1$:

$$
\bigl(L_{e_{1}}R_{e_{1}}\tilde X\bigr)\bigl(L_{e_{1}}R_{e_{1}}\tilde Y\bigr)=-\bigl(L_{e_{1}}R_{e_{1}}\bigr)(\tilde X\tilde Y),
$$

and the operator $\tilde Y\mapsto e_{1}\tilde Ye_{1}$ is anti-multiplicative. It is the negative of the inner automorphism $\mathrm{Ad}_{e_{1}}$, since $e_{1}^{-1}=-e_{1}$; the example is the least degenerate instance of the partial law, and it separates the central-product family from the genuinely multiplicative operators of the theorem. A general parameter does not qualify: for $\tilde A=e_{1}+(1+2i)e_{2}$ the square is not central, and no scalar makes the product law hold.

**The powers and the exponential.** For $\tilde A=e_{1}$, $\tilde B=e_{2}$ the second power is $L_{e_{1}^{2}}R_{e_{2}^{2}}=L_{-e_{0}}R_{-e_{0}}=\mathrm{id}$, so the powers alternate between $L_{e_{1}}R_{e_{2}}$ and the identity; the exponential $\exp(L_{e_{1}}R_{e_{2}})$ is the operator $\tilde Y\mapsto\cosh(1)\tilde Y+\sinh(1)e_{1}\tilde Ye_{2}$, which is a sum of two two-sided operators and is not itself two-sided, the sum of decomposable tensors having ceased to be decomposable.

**A numerical check of the composition and the swap.** For random parameters the identities $(L_{\tilde A}R_{\tilde B})(L_{\tilde C}R_{\tilde D})=L_{\tilde A\tilde C}R_{\tilde D\tilde B}$ and $(L_{\tilde A}R_{\tilde B})^{\approx}=L_{\tilde B}R_{\tilde A}$ hold to machine precision, and the four criteria of the article were checked on random, central, pure, null and unit parameters.

## Summary

The two-sided operators are the products $L_{\tilde A}R_{\tilde B}(\tilde Y)=\tilde A\tilde Y\tilde B$ of a left and a right multiplication with independent parameters; they contain the one-sided ones at the boundary cases and they are the decomposable tensors of the enveloping algebra $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{op}}$, whose products span the whole operator algebra of complex dimension sixteen. Composition reverses the second slot, $(\tilde A,\tilde B)(\tilde C,\tilde D)=(\tilde A\tilde C,\tilde D\tilde B)$, and the adjoint for the general plain bilinear form swaps the two parameters. The type, automorphism and multiplicativity criteria are criteria on the product of the pair: self-adjoint exactly when $\tilde B=\lambda\tilde A$, never skew-adjoint except for the zero operator, form preserving exactly when $\tilde B\tilde A=\pm e_{0}$, multiplicative exactly when $\tilde A\tilde B=e_{0}$; when the product $\tilde B\tilde A$ is merely central the operator is still multiplicative up to that central scalar, which is the weaker and differently shaped analogue of the quaternionic law $\Theta_{\tilde A}(\tilde X)\Theta_{\tilde A}(\tilde Y)=N(\tilde A)\Theta_{\tilde A}(\tilde X\tilde Y)$. The multiplicative and form-preserving operators are the inner automorphisms of the units, and no norm enters any criterion — the sharp contrast with the quaternionic pair of the corpus. At $\tilde B=e_{0}$ all the criteria reduce to the one-sided ones.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q)$ | The general plain bilinear form; Gram matrix $\mathrm{diag}(1,-1,-1,-1)$ |
| $F^{\approx}$ | The associate, or transpose, of $F$ for this form |
| $L_{\tilde A}R_{\tilde B}(\tilde Y)=\tilde A\tilde Y\tilde B$ | The two-sided operator of the pair $(\tilde A,\tilde B)$ |
| $L_{\tilde A}R_{\tilde B}=L_{\tilde A}$ at $\tilde B=e_{0}$ | The one-sided operators as boundary cases |
| $e_n[\,]e_m$, $n,m=0,\dots,3$ | Basis of the family; independent, spanning $\mathrm{End}_{\mathbb{C}}(\mathbb{B})$ |
| $(\tilde A,\tilde B)(\tilde C,\tilde D)=(\tilde A\tilde C,\tilde D\tilde B)$ | Composition; the second slot reverses |
| $(L_{\tilde A}R_{\tilde B})^{n}=L_{\tilde A^{n}}R_{\tilde B^{n}}$ | Powers stay in the family |
| $(L_{\tilde A}R_{\tilde B})^{\approx}=L_{\tilde B}R_{\tilde A}$ | The adjoint swaps the parameters |
| Self-adjoint $\iff\tilde B=\lambda\tilde A$ | Type criterion of the family |
| Skew-adjoint $\iff$ the operator is $0$ | The skew sector is trivial |
| $L_{\tilde A}R_{\tilde B}$ preserves the form $\iff \tilde B\tilde A=\pm e_{0}$ | The automorphisms of the form in the family |
| $L_{\tilde A}R_{\tilde B}$ multiplicative $\iff \tilde A\tilde B=e_{0}$ | Then $L_{\tilde A}R_{\tilde A^{-1}}=\mathrm{Ad}_{\tilde A}$ |
| $\tilde B\tilde A$ central $\implies$ multiplicative up to $\tilde B\tilde A$ | The partial law; the scalar is the central product, not a norm |
| $(\tilde A,\tilde B)\mapsto L_{\tilde A}R_{\tilde B}$ | Bilinear; injective in each slot at a unit; kernel $\{(\lambda e_{0},\lambda^{-1}e_{0})\}$ |

## Further Reading

- *The Four Adjoints of the Two Algebras and the Two Sesqualgebras in Examples* (`articles_maths/the-four-adjoints-of-the-two-algebras-and-the-two-sesqualgebras-in-examples.md`), for the four adjoints of one two-sided operator and the self-adjointness criteria, of which the association column is the first
- *The Pin and Spin Groups of the General Plain Algebra of Biquaternions* (`articles_maths/the-pin-and-spin-groups-of-the-general-plain-algebra-of-biquaternions.md`), the plain twin of the quaternionic pin and spin article, for the isometry side of the criterion $\tilde B\tilde A=\pm e_0$: the two cosets $\pm\mathrm{Ad}_{\tilde A}$, the vacuous isometry condition, and the reason no shell of the plain form is a group.
- *One-Sided Operators on the General Plain Algebra of Biquaternions* (`articles_maths/one-sided-operators-on-the-general-plain-algebra-of-biquaternions.md`), the companion article, for the factors $L_{\tilde A}$ and $R_{\tilde B}$, the swap $L^{\approx}=R$, and the one-sided form-preserving theorem used in the proof of the isometry criterion.
- *Association and the Transpose on the Biquaternion Algebra* (`articles_maths/association-and-the-transpose-on-the-biquaternion-algebra.md`), for the associate $F^{\approx}$, the basis rule $(e_n[\,]e_m)^{\approx}=e_m[\,]e_n$, and the reversal $(FG)^{\approx}=G^{\approx}F^{\approx}$.
- *The Enveloping Algebra of the Biquaternion Algebra and the Bi-module Structure* (`articles_maths/the-enveloping-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.md`), for $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{op}}$ as the operator algebra and the two-sided operators as the decomposable tensors.
- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the place of $\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q)$ among the pairings of the algebra.
- *Biquaternion Zero Divisors* (`articles_maths/biquaternion-zero-divisors.md`), for the null parameters and the complementary zero divisor pairs that the skew criterion excludes.
- *Biquaternion Square Roots of a General Element* (`articles_maths/biquaternion-square-roots-of-a-general-element.md`), for the square-root problem in the algebra, whose solutions are the involutive parameters of the form-preserving criterion.
