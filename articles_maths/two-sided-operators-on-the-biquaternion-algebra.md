# __Two-Sided Operators on the Biquaternion Algebra__

## Introduction

Let $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ be the biquaternion algebra with its natural conjugation ${}^{\natural}$ and the general plain bilinear form

$$
\langle\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}(\tilde Q_1\tilde Q_2),
$$

whose Gram matrix in the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ is $\mathrm{diag}(1,-1,-1,-1)$, and let $F^{\approx}$ be the associate, or transpose, of a $\mathbb{C}$-linear map for this form (*The Four Adjoints of the Two Algebras and the Two Sesqualgebras in Examples*).

For $\tilde Q_5,\tilde Q_3\in\mathbb{B}$ define the **two-sided operator**

$$
L_{\tilde Q_5}R_{\tilde Q_3}:\mathbb{B}\longrightarrow\mathbb{B},\qquad
\bigl(L_{\tilde Q_5}R_{\tilde Q_3}\bigr)(\tilde Q)=\tilde Q_5\,\tilde Q\,\tilde Q_3 ,
$$

the product of a left and a right multiplication, with the two parameters independent. These operators are the subject of the article. They contain the one-sided ones as the two boundary cases $\tilde Q_3=e_t$ and $\tilde Q_5=e_t$, they contain every inner automorphism, and they are the elements of the enveloping algebra $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}$ read on the algebra itself.

The article is the parallel of *One-Sided Operators on the Biquaternion Algebra*, section for section, and the parallel is what isolates the cost of the second parameter. Three things change. The composition law **reverses the second slot**, $\tilde Q_3$ and $\tilde D$ exchanging their places, because the right multiplications form an anti-representation. The adjoint **swaps the two parameters**, $(L_{\tilde Q_5}R_{\tilde Q_3})^{\approx}=L_{\tilde Q_3}R_{\tilde Q_5}$, because association is the transpose for the plain form, whereas the Hermitian dagger and the quaternionic adjoint keep the parameter they act on. And the criteria become criteria on the **product** of the parameters: self-adjointness is $\tilde Q_3=\lambda\tilde Q_5$, preservation of the form is $\tilde Q_3\tilde Q_5=\pm e_t$, multiplicativity is $\tilde Q_5\tilde Q_3=e_t$. No norm enters any of the three, which is the second sharp difference from the quaternionic pair, where the corresponding criteria turn on $\langle\cdot\rangle_{\natural}$.

The algebra, the conjugations and the remarkable subspaces are *The Biquaternioid as a Vector Space over $\mathbb{C}$*, *The Group of Involutions* and *Introduction to the Remarkable Subspaces*; the form and its pairings are *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space*; the enveloping algebra and the two-sided operators as its elements are *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*; the one-sided factors are *One-Sided Operators on the Biquaternion Algebra*.

## The Two-Sided Family

**Definition.** For $\tilde Q_5,\tilde Q_3\in\mathbb{B}$ the **two-sided operator of the pair $(\tilde Q_5,\tilde Q_3)$** is the $\mathbb{C}$-linear map

$$
\bigl(L_{\tilde Q_5}R_{\tilde Q_3}\bigr)(\tilde Q)=\tilde Q_5\,\tilde Q\,\tilde Q_3 .
$$

**Proposition (the family contains the one-sided operators).** With the unit in one slot,

$$
L_{\tilde Q_5}R_{e_t}=L_{\tilde Q_5},\qquad L_{e_t}R_{\tilde Q_3}=R_{\tilde Q_3}.
$$

The family is therefore the two-parameter extension of the one-sided pair, and the criteria below specialise to the criteria of the one-sided article at $\tilde Q_3=e_t$.

*Proof.* The unit acts by the identity in each slot.

**Proposition (bilinearity and the spanning set).** The assignment $(\tilde Q_5,\tilde Q_3)\mapsto L_{\tilde Q_5}R_{\tilde Q_3}$ is bilinear and injective in each slot when the other parameter is fixed and a unit. The sixteen operators $e_\mu[\,]e_\nu$, $\mu,\nu\in\{t,x,y,z\}$, are linearly independent and therefore form a basis of $\mathrm{End}_{\mathbb{C}}(\mathbb{B})$:

$$
\dim_{\mathbb{C}}\mathrm{Span}\{\,L_{\tilde Q_5}R_{\tilde Q_3}\,\}=16 .
$$

*Proof.* Bilinearity is the distributivity of the product. For the independence, the enveloping algebra $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}$ is isomorphic to $\mathrm{End}_{\mathbb{C}}(\mathbb{B})$ through $A\otimes B\mapsto L_AR_B$, and it has complex dimension $16$ (*The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*); the independence of the sixteen basis elements was verified by elimination on their matrices. Injectivity in the first slot at a unit $\tilde Q_3$ follows from $L_{\tilde Q_5}R_{\tilde Q_3}(e_t)=\tilde Q_5\tilde Q_3$ and the invertibility of $\tilde Q_3$.

**Remark (the image is the decomposable tensors).** Under the isomorphism $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}\to\mathrm{End}_{\mathbb{C}}(\mathbb{B})$ the two-sided operators are the images of the **decomposable** tensors, and a general endomorphism is a sum of them. That is the precise sense in which the two-sided family is the algebraic skeleton of the full operator algebra, and it is also why a sum of two-sided operators need not be two-sided: the decomposable tensors do not form a subspace.

## The Composition Law

**Theorem (composition).** For all $\tilde Q_5,\tilde Q_3,\tilde Q_4,\tilde D\in\mathbb{B}$,

$$
\bigl(L_{\tilde Q_5}R_{\tilde Q_3}\bigr)\circ\bigl(L_{\tilde Q_4}R_{\tilde D}\bigr)=L_{\tilde Q_5\tilde Q_4}\,R_{\tilde D\tilde Q_3},
$$

the parameters of the second slot reversing their order.

*Proof.* $\tilde Q_5\bigl(\tilde Q_4\tilde Q\tilde D\bigr)\tilde Q_3=\tilde Q_5\tilde Q_4\,\tilde Q\,\tilde D\tilde Q_3$ by associativity.

**Corollary (the family is a monoid with reversed right factors).** The composition law makes the set of two-sided operators a submonoid of $\mathrm{End}_{\mathbb{C}}(\mathbb{B})$, isomorphic to the image of the monoid $\mathbb{B}\times\mathbb{B}^{\mathrm{opp}}$ under the bilinear map, with multiplication $(\tilde Q_5,\tilde Q_3)(\tilde Q_4,\tilde D)=(\tilde Q_5\tilde Q_4,\tilde D\tilde Q_3)$. The reversal in the second factor is the reason the family is not a direct product of two copies of the algebra.

**Corollary (invertibility and the units).** The operator $L_{\tilde Q_5}R_{\tilde Q_3}$ is invertible if and only if $\tilde Q_5$ and $\tilde Q_3$ are units, with inverse

$$
\bigl(L_{\tilde Q_5}R_{\tilde Q_3}\bigr)^{-1}=L_{\tilde Q_5^{-1}}R_{\tilde Q_3^{-1}} .
$$

The group of invertible two-sided operators is therefore the image of $\mathbb{B}^{\times}\times\mathbb{B}^{\times}$, and the kernel of the parametrisation is $\{(\lambda e_t,\lambda^{-1}e_t)\}$: the two-sided operator is the identity exactly for $\tilde Q_5\tilde Q_3=e_t$ with $\tilde Q_5$ central.

*Proof.* The inverse is verified by the composition law. For the converse, if the operator is invertible then it is injective, so $\tilde Q_5$ and $\tilde Q_3$ are units: a nonzero kernel of $\tilde Q_5$, say $\tilde Q_5\tilde Q_1=0$, gives $L_{\tilde Q_5}R_{\tilde Q_3}(\tilde Q_1\tilde Q_2)=0$ for every $\tilde Q_2$. For the kernel of the parametrisation, $L_{\tilde Q_5}R_{\tilde Q_3}=\mathrm{id}$ reads $\tilde Q_5\tilde Q\tilde Q_3=\tilde Q$ for all $\tilde Q$; at $\tilde Q=e_t$ this gives $\tilde Q_5\tilde Q_3=e_t$, and substituting back gives $\tilde Q_5\tilde Q=\tilde Q\tilde Q_5$ for all $\tilde Q$, so $\tilde Q_5$ is central and $\tilde Q_3=\tilde Q_5^{-1}$ has the same central value.

**Corollary (the powers stay in the family).** For every $n\ge1$,

$$
\bigl(L_{\tilde Q_5}R_{\tilde Q_3}\bigr)^{n}=L_{\tilde Q_5^{n}}R_{\tilde Q_3^{n}} .
$$

*Proof.* Induction on the composition law. The corollary is the reason the exponential of a two-sided operator generally leaves the family: $\exp(L_{\tilde Q_5}R_{\tilde Q_3})$ is the operator $\tilde Q\mapsto\sum_{n\ge0}\frac{1}{n!}\tilde Q_5^{n}\tilde Q\tilde Q_3^{n}$, and a sum of decomposable tensors $\tilde Q_5^{n}\otimes\tilde Q_3^{n}$ is decomposable in degenerate cases only. In the one-sided case the same computation gives $\exp(L_{\tilde Q_5})=L_{\exp(\tilde Q_5)}$ and $\exp(R_{\tilde Q_3})=R_{\exp(\tilde Q_3)}$, because the parameter enters once and the series is the exponential of the parameter.

## The Adjoint and the Swap

**Theorem (the adjoint exchanges the parameters).** For all $\tilde Q_5,\tilde Q_3\in\mathbb{B}$,

$$
\bigl(L_{\tilde Q_5}R_{\tilde Q_3}\bigr)^{\approx}=L_{\tilde Q_3}R_{\tilde Q_5}.
$$

*Proof.* The transpose of a composite reverses the order, $(FG)^{\approx}=G^{\approx}\circ F^{\approx}$ (*The Four Adjoints of the Two Algebras and the Two Sesqualgebras in Examples*), and the transposes of the factors are the crossed one-sided operators, $(L_{\tilde Q_5})^{\approx}=R_{\tilde Q_5}$ and $(R_{\tilde Q_3})^{\approx}=L_{\tilde Q_3}$ (*One-Sided Operators on the Biquaternion Algebra*):

$$
\bigl(L_{\tilde Q_5}R_{\tilde Q_3}\bigr)^{\approx}=\bigl(R_{\tilde Q_3}\bigr)^{\approx}\bigl(L_{\tilde Q_5}\bigr)^{\approx}=L_{\tilde Q_3}R_{\tilde Q_5}.
$$


**Remark (swap, not conjugation).** The adjoint of a two-sided operator is a two-sided operator with the two parameters interchanged. The quaternionic pair of the corpus has the opposite behaviour: there the adjoint for the quaternionic form keeps the parameter, $(L_{\tilde Q_5})^{N}=L_{\tilde Q_5^{\natural}}$ and $(\Theta_{\tilde Q_5})^{N}=\Theta_{\tilde Q_5^{\natural}}$, so a type criterion is a criterion on one parameter. Here every type criterion is symmetric or antisymmetric in the pair $(\tilde Q_5,\tilde Q_3)$, and the whole article turns on that single difference. This is §*The Adjoint and the Swap* referred to by the one-sided article.

## The Self-Adjoint and the Skew-Adjoint Sectors

**Theorem (the self-adjoint criterion).** For $\tilde Q_5\neq0$ the operator $L_{\tilde Q_5}R_{\tilde Q_3}$ is self-adjoint if and only if the two parameters are proportional,

$$
\bigl(L_{\tilde Q_5}R_{\tilde Q_3}\bigr)^{\approx}=L_{\tilde Q_5}R_{\tilde Q_3}
\iff \tilde Q_3=\lambda\tilde Q_5\quad\text{for some }\lambda\in\mathbb{C}.
$$

Consequently the self-adjoint two-sided operators are the scalar multiples $\lambda\,L_{\tilde Q_5}R_{\tilde Q_5}$ of the diagonal products, together with the zero operator.

*Proof.* By the swap theorem, self-adjointness is $L_{\tilde Q_3}R_{\tilde Q_5}=L_{\tilde Q_5}R_{\tilde Q_3}$, that is $\tilde Q_3\tilde Q\tilde Q_5=\tilde Q_5\tilde Q\tilde Q_3$ for all $\tilde Q$. At $\tilde Q=e_t$ the two parameters commute. Substitute $\tilde Q=\tilde Q_5^{-1}\tilde Q_4\tilde Q_5^{-1}$ for an arbitrary $\tilde Q_4$, which is legitimate when $\tilde Q_5$ is a unit: the identity becomes $\tilde Q_3\tilde Q_5^{-1}\tilde Q_4=\tilde Q_4\tilde Q_5^{-1}\tilde Q_3$ for all $\tilde Q_4$, so $\tilde Q_3\tilde Q_5^{-1}$ is central, that is $\tilde Q_3=\lambda\tilde Q_5$. Conversely $\tilde Q_3=\lambda\tilde Q_5$ gives $\tilde Q_3\tilde Q\tilde Q_5=\lambda\tilde Q_5\tilde Q\tilde Q_5=\tilde Q_5\tilde Q\lambda\tilde Q_5=\tilde Q_5\tilde Q\tilde Q_3$. The case of a non-unit $\tilde Q_5$ is the same computation with the parameter of the other slot, or follows by evaluating the identity at $\tilde Q=e_t$ and using centrality.

**Theorem (the skew sector is trivial).** No nonzero two-sided operator is skew-adjoint:

$$
\bigl(L_{\tilde Q_5}R_{\tilde Q_3}\bigr)^{\approx}=-L_{\tilde Q_5}R_{\tilde Q_3}
\iff L_{\tilde Q_5}R_{\tilde Q_3}=0 .
$$

*Proof.* Skew-adjointness is $L_{\tilde Q_3}R_{\tilde Q_5}=-L_{\tilde Q_5}R_{\tilde Q_3}$, that is $\tilde Q_3\tilde Q\tilde Q_5=-\tilde Q_5\tilde Q\tilde Q_3$ for all $\tilde Q$. Taking the scalar part and using the cyclicity of $\mathrm{Sc}$,

$$
\mathrm{Sc}\bigl(\tilde Q_3\tilde Q\tilde Q_5\bigr)=\mathrm{Sc}\bigl(\tilde Q\tilde Q_5\tilde Q_3\bigr)
=-\mathrm{Sc}\bigl(\tilde Q_5\tilde Q\tilde Q_3\bigr)=-\mathrm{Sc}\bigl(\tilde Q\tilde Q_5\tilde Q_3\bigr),
$$

so $\mathrm{Sc}(\tilde Q\tilde Q_5\tilde Q_3)=0$ for all $\tilde Q$, and the non-degeneracy of the form gives $\tilde Q_5\tilde Q_3=0$; the same argument with the parameters read in the other order gives $\tilde Q_3\tilde Q_5=0$. At $\tilde Q=e_t$ the defining identity then reads $\tilde Q_3\tilde Q_5=-\tilde Q_5\tilde Q_3$, so both products vanish. A zero divisor pair with $\tilde Q_5\tilde Q_3=\tilde Q_3\tilde Q_5=0$ and both parameters nonzero nevertheless fails the identity on a general element, and the cases were settled by elimination: for every fixed nonzero $\tilde Q_3$, both null and non-null, the linear system in $\tilde Q_5$ has only the solution $\tilde Q_5=0$.

**Corollary (the two sectors at the boundary).** At $\tilde Q_3=e_t$ the two criteria of this section give the one-sided criteria: $\tilde Q_3=\lambda\tilde Q_5$ becomes $\tilde Q_5$ central, and the skew condition becomes $\tilde Q_5=0$. The one-sided type criteria are therefore the boundary case of the two-sided ones, and the pair of articles is one theorem read on a family and on its slice.

## Automorphisms of the Form and Multiplicative Operators

**Theorem (the automorphisms of the form inside the family).** The operator $L_{\tilde Q_5}R_{\tilde Q_3}$ preserves the general plain bilinear form,

$$
\bigl\langle L_{\tilde Q_5}R_{\tilde Q_3}\tilde Q_1,\ L_{\tilde Q_5}R_{\tilde Q_3}\tilde Q_2\bigr\rangle=\langle\tilde Q_1,\tilde Q_2\rangle\qquad\text{for all }\tilde Q_1,\tilde Q_2,
$$

if and only if $\tilde Q_3\tilde Q_5=\pm e_t$, that is if and only if $\tilde Q_3=\pm\tilde Q_5^{-1}$. In that case the operator is $\pm\mathrm{Ad}_{\tilde Q_5}$, the inner automorphism of $\tilde Q_5$ up to sign.

*Proof.* If the operator preserves the form it is injective, because the form is non-degenerate, hence $\tilde Q_5$ and $\tilde Q_3$ are units. Put $\tilde Q_6=\tilde Q_3\tilde Q_5$, so that $\tilde Q_3=\tilde Q_6\tilde Q_5^{-1}$, and compute with the cyclicity of the scalar part:

$$
\mathrm{Sc}\bigl(\tilde Q_5\tilde Q_1\tilde Q_3\tilde Q_5\tilde Q_2\tilde Q_3\bigr)
=\mathrm{Sc}\bigl(\tilde Q_5\tilde Q_1\tilde Q_6\tilde Q_2\tilde Q_6\tilde Q_5^{-1}\bigr)
=\mathrm{Sc}\bigl(\tilde Q_6\tilde Q_1\tilde Q_6\tilde Q_2\bigr)
=\bigl\langle\tilde Q_1,\tilde Q_6\tilde Q_2\tilde Q_6\bigr\rangle .
$$

Preservation is therefore equivalent to $\tilde Q_6\tilde Q\tilde Q_6=\tilde Q$ for all $\tilde Q$, which by the one-sided theorem forces $\tilde Q_6=\pm e_t$ (*One-Sided Operators on the Biquaternion Algebra*, §*Which Multiplications Preserve the Form*). Conversely $\tilde Q_3=\tilde Q_5^{-1}$ gives the inner automorphism, which preserves the form, and $\tilde Q_3=-\tilde Q_5^{-1}$ gives its negative, which preserves the form up to the sign $(-1)^{2}=1$.

**Theorem (the multiplicative operators).** The operator $L_{\tilde Q_5}R_{\tilde Q_3}$ is multiplicative,

$$
\bigl(L_{\tilde Q_5}R_{\tilde Q_3}\bigr)(\tilde Q_1)\bigl(L_{\tilde Q_5}R_{\tilde Q_3}\bigr)(\tilde Q_2)=\bigl(L_{\tilde Q_5}R_{\tilde Q_3}\bigr)(\tilde Q_1\tilde Q_2)\qquad\text{for all }\tilde Q_1,\tilde Q_2,
$$

if and only if $\tilde Q_5\tilde Q_3=e_t$, that is $\tilde Q_3=\tilde Q_5^{-1}$; and then it is the inner automorphism $\mathrm{Ad}_{\tilde Q_5}$, an automorphism of the algebra for every unit $\tilde Q_5$.

*Proof.* The left side is $\tilde Q_5\tilde Q_1\tilde Q_3\tilde Q_5\tilde Q_2\tilde Q_3$ and the right side is $\tilde Q_5\tilde Q_1\tilde Q_2\tilde Q_3$, so with $\tilde Q_7=\tilde Q_5\tilde Q_3$ the identity reads $\tilde Q_5\tilde Q_1\tilde Q_7\tilde Q_2\tilde Q_3=\tilde Q_5\tilde Q_1\tilde Q_2\tilde Q_3$ for all $\tilde Q_1,\tilde Q_2$. At $\tilde Q_1=e_t$ and for units $\tilde Q_5,\tilde Q_3$ this is $\tilde Q_7\tilde Q_2=\tilde Q_2$ for all $\tilde Q_2$, hence $\tilde Q_7=e_t$, that is $\tilde Q_3=\tilde Q_5^{-1}$; conversely $\tilde Q_5\tilde Q_3=e_t$ makes the two sides equal for all $\tilde Q_1,\tilde Q_2$, and the operator is $\tilde Q\mapsto\tilde Q_5\tilde Q\tilde Q_5^{-1}$.

**Corollary (multiplicative and form preserving).** The two-sided operators that are multiplicative and preserve the form at once are exactly the inner automorphisms $\mathrm{Ad}_{\tilde Q_5}$ with $\tilde Q_5$ a unit, without the sign $-\mathrm{Ad}_{\tilde Q_5}$: the sign that the criterion of the first theorem allows is excluded by multiplicativity.

**Corollary (the partial law of the central product).** Suppose the product of the two parameters is central, that is $\tilde Q_3\tilde Q_5=\mu e_t$ with $\mu=\mathrm{Sc}(\tilde Q_3\tilde Q_5)$. Then for all $\tilde Q_1,\tilde Q_2$,

$$
\bigl(L_{\tilde Q_5}R_{\tilde Q_3}\tilde Q_1\bigr)\bigl(L_{\tilde Q_5}R_{\tilde Q_3}\tilde Q_2\bigr)
=(\tilde Q_3\tilde Q_5)\,\bigl(L_{\tilde Q_5}R_{\tilde Q_3}\bigr)(\tilde Q_1\tilde Q_2)
=\mu\,\bigl(L_{\tilde Q_5}R_{\tilde Q_3}\bigr)(\tilde Q_1\tilde Q_2),
$$

and the multiplier is the central scalar $\tilde Q_3\tilde Q_5$, not a norm. The condition is automatic for $\tilde Q_3=\tilde Q_5^{-1}$, which is the exact criterion of the theorem above, but it is weaker: it holds for every pair whose product falls in the centre $\mathbb{C}e_t$, and the operator is then multiplicative up to that central scalar.

*Proof.* $\tilde Q_3\tilde Q_5$ is central by hypothesis, so it may be moved across $\tilde Q_1$ in $\tilde Q_5\tilde Q_1(\tilde Q_3\tilde Q_5)\tilde Q_2\tilde Q_3$; substituting $\tilde Q_3\tilde Q_5=\mu e_t$ gives the second form.

**Remark (no norm enters, and the law is the weaker for it).** The quaternionic pair of the corpus reads the same two questions through the norm and carries the correspondingly stronger law: there $\Theta_{\tilde Q_5}(\tilde Q_1)\Theta_{\tilde Q_5}(\tilde Q_2)=\langle\tilde Q_5\rangle_{\natural}\,\Theta_{\tilde Q_5}(\tilde Q_1\tilde Q_2)$ holds for **every** parameter, with the norm as the scalar, and genuine multiplicativity up to a scalar is the condition $\langle\tilde Q_5\rangle_{\natural}=1$. Here the criteria are $\tilde Q_3\tilde Q_5=\pm e_t$ and $\tilde Q_5\tilde Q_3=e_t$: conditions on the product of the two parameters, in which no norm and no conjugation appears, and the partial law above holds only when that product is central. The two shapes are not the same theorem with different letters; the plain form carries no twist for a norm to absorb, so it loses the parameter-free law and keeps the criterion.

## Worked Examples

**The identity and its multiples.** $L_{e_t}R_{e_t}=\mathrm{id}$, self-adjoint and form preserving; the central multiples $\lambda\,\mathrm{id}=L_{\lambda e_t}R_{e_t}$ are self-adjoint for every $\lambda$, preserve the form only for $\lambda=\pm1$, and are multiplicative only for $\lambda=1$: the three criteria are genuinely different, and the example separates them.

**A mixed operator.** The operator $\tilde Q\mapsto \vec e_x\tilde Q\vec e_y=L_{\vec e_x}R_{\vec e_y}$ has $\tilde Q_3\tilde Q_5=\vec e_y\vec e_x=-\vec e_z$, so by the criteria it is neither self-adjoint (the parameters are not proportional), nor form preserving ($-\vec e_z\neq\pm e_t$), nor multiplicative. Its adjoint is $L_{\vec e_y}R_{\vec e_x}$, the parameter pair exchanged, and the two operators differ, since $\vec e_x\vec e_z\vec e_y$ and $\vec e_y\vec e_z\vec e_x$ have opposite signs.

**An inner automorphism.** For the pure unit $\tilde Q_5=\vec e_x$ one has $\tilde Q_5^{-1}=-\vec e_x$, so

$$
\mathrm{Ad}_{\vec e_x}=L_{\vec e_x}R_{\vec e_x^{-1}}=L_{\vec e_x}R_{-\vec e_x},
$$

and the three criteria hold at once: the parameters are proportional with $\lambda=-1$, so the operator is self-adjoint; $\tilde Q_3\tilde Q_5=(-\vec e_x)\vec e_x=e_t$, so it preserves the form; and $\tilde Q_3=\tilde Q_5^{-1}$, so it is multiplicative. It is the least degenerate two-sided operator after the identity, and the example exercises the three criteria on one object.

**A self-adjoint operator with a null parameter.** For $\tilde Q_5=e_t+i\vec e_z$, a zero divisor with $\tilde Q_5^{2}=2\tilde Q_5\neq e_t$, the diagonal operator $L_{\tilde Q_5}R_{\tilde Q_5}$ is self-adjoint by the criterion $\tilde Q_3=\lambda\tilde Q_5$ with $\lambda=1$, although the parameter is not a unit. The example records that self-adjointness is a condition on the pair and not on invertibility, in contrast with the form-preserving criterion, which forces both parameters to be units.

**A diagonal operator multiplicative up to sign.** For the pure unit $\tilde Q_5=\tilde Q_3=\vec e_x$ the product of the parameters is $\tilde Q_3\tilde Q_5=\vec e_x^{2}=-e_t$, central, so the partial law applies with the scalar $-1$:

$$
\bigl(L_{\vec e_x}R_{\vec e_x}\tilde Q_1\bigr)\bigl(L_{\vec e_x}R_{\vec e_x}\tilde Q_2\bigr)=-\bigl(L_{\vec e_x}R_{\vec e_x}\bigr)(\tilde Q_1\tilde Q_2),
$$

and the operator $\tilde Q\mapsto \vec e_x\tilde Q\vec e_x$ is anti-multiplicative. It is the negative of the inner automorphism $\mathrm{Ad}_{\vec e_x}$, since $\vec e_x^{-1}=-\vec e_x$; the example is the least degenerate instance of the partial law, and it separates the central-product family from the genuinely multiplicative operators of the theorem. A general parameter does not qualify: for $\tilde Q_5=1+\vec e_x+(1+2i)\vec e_y$ the square is not central, and no scalar makes the product law hold.

**The powers and the exponential.** For $\tilde Q_5=\vec e_x$, $\tilde Q_3=\vec e_y$ the second power is $L_{\vec e_x^{2}}R_{\vec e_y^{2}}=L_{-e_t}R_{-e_t}=\mathrm{id}$, so the powers alternate between $L_{\vec e_x}R_{\vec e_y}$ and the identity; the exponential $\exp(L_{\vec e_x}R_{\vec e_y})$ is the operator $\tilde Q\mapsto\cosh(1)\tilde Q+\sinh(1)\vec e_x\tilde Q\vec e_y$, which is a sum of two two-sided operators and is not itself two-sided, the sum of decomposable tensors having ceased to be decomposable.

**A numerical check of the composition and the swap.** For random parameters the identities $(L_{\tilde Q_5}R_{\tilde Q_3})(L_{\tilde Q_4}R_{\tilde D})=L_{\tilde Q_5\tilde Q_4}R_{\tilde D\tilde Q_3}$ and $(L_{\tilde Q_5}R_{\tilde Q_3})^{\approx}=L_{\tilde Q_3}R_{\tilde Q_5}$ hold to machine precision, and the four criteria of the article were checked on random, central, pure, null and unit parameters.

## Summary

The two-sided operators are the products $L_{\tilde Q_5}R_{\tilde Q_3}(\tilde Q)=\tilde Q_5\tilde Q\tilde Q_3$ of a left and a right multiplication with independent parameters; they contain the one-sided ones at the boundary cases and they are the decomposable tensors of the enveloping algebra $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}$, whose products span the whole operator algebra of complex dimension sixteen. Composition reverses the second slot, $(\tilde Q_5,\tilde Q_3)(\tilde Q_4,\tilde D)=(\tilde Q_5\tilde Q_4,\tilde D\tilde Q_3)$, and the adjoint for the general plain bilinear form swaps the two parameters. The type, automorphism and multiplicativity criteria are criteria on the product of the pair: self-adjoint exactly when $\tilde Q_3=\lambda\tilde Q_5$, never skew-adjoint except for the zero operator, form preserving exactly when $\tilde Q_3\tilde Q_5=\pm e_t$, multiplicative exactly when $\tilde Q_5\tilde Q_3=e_t$; when the product $\tilde Q_3\tilde Q_5$ is merely central the operator is still multiplicative up to that central scalar, which is the weaker and differently shaped analogue of the quaternionic law $\Theta_{\tilde Q_5}(\tilde Q_1)\Theta_{\tilde Q_5}(\tilde Q_2)=\langle\tilde Q_5\rangle_{\natural}\Theta_{\tilde Q_5}(\tilde Q_1\tilde Q_2)$. The multiplicative and form-preserving operators are the inner automorphisms of the units, and no norm enters any criterion — the sharp contrast with the quaternionic pair of the corpus. At $\tilde Q_3=e_t$ all the criteria reduce to the one-sided ones.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ | The general plain bilinear form; Gram matrix $\mathrm{diag}(1,-1,-1,-1)$ |
| $F^{\approx}$ | The associate, or transpose, of $F$ for this form |
| $L_{\tilde Q_5}R_{\tilde Q_3}(\tilde Q)=\tilde Q_5\tilde Q\tilde Q_3$ | The two-sided operator of the pair $(\tilde Q_5,\tilde Q_3)$ |
| $L_{\tilde Q_5}R_{\tilde Q_3}=L_{\tilde Q_5}$ at $\tilde Q_3=e_t$ | The one-sided operators as boundary cases |
| $e_\mu[\,]e_\nu$, $\mu,\nu\in\{t,x,y,z\}$ | Basis of the family; independent, spanning $\mathrm{End}_{\mathbb{C}}(\mathbb{B})$ |
| $(\tilde Q_5,\tilde Q_3)(\tilde Q_4,\tilde D)=(\tilde Q_5\tilde Q_4,\tilde D\tilde Q_3)$ | Composition; the second slot reverses |
| $(L_{\tilde Q_5}R_{\tilde Q_3})^{n}=L_{\tilde Q_5^{n}}R_{\tilde Q_3^{n}}$ | Powers stay in the family |
| $(L_{\tilde Q_5}R_{\tilde Q_3})^{\approx}=L_{\tilde Q_3}R_{\tilde Q_5}$ | The adjoint swaps the parameters |
| Self-adjoint $\iff\tilde Q_3=\lambda\tilde Q_5$ | Type criterion of the family |
| Skew-adjoint $\iff$ the operator is $0$ | The skew sector is trivial |
| $L_{\tilde Q_5}R_{\tilde Q_3}$ preserves the form $\iff \tilde Q_3\tilde Q_5=\pm e_t$ | The automorphisms of the form in the family |
| $L_{\tilde Q_5}R_{\tilde Q_3}$ multiplicative $\iff \tilde Q_5\tilde Q_3=e_t$ | Then $L_{\tilde Q_5}R_{\tilde Q_5^{-1}}=\mathrm{Ad}_{\tilde Q_5}$ |
| $\tilde Q_3\tilde Q_5$ central $\implies$ multiplicative up to $\tilde Q_3\tilde Q_5$ | The partial law; the scalar is the central product, not a norm |
| $(\tilde Q_5,\tilde Q_3)\mapsto L_{\tilde Q_5}R_{\tilde Q_3}$ | Bilinear; injective in each slot at a unit; kernel $\{(\lambda e_t,\lambda^{-1}e_t)\}$ |

## Further Reading

- *The Four Adjoints of the Two Algebras and the Two Sesqualgebras in Examples* (`articles_maths/the-four-adjoints-of-the-two-algebras-and-the-two-sesqualgebras-in-examples.md`), for the four adjoints of one two-sided operator and the self-adjointness criteria, of which the association column is the first
- *The Pin and Spin Groups of the Biquaternion Algebra* (`articles_maths/the-pin-and-spin-groups-of-the-biquaternion-algebra.md`), the plain twin of the quaternionic pin and spin article, for the isometry side of the criterion $\tilde Q_3\tilde Q_5=\pm e_t$: the two cosets $\pm\mathrm{Ad}_{\tilde Q_5}$, the vacuous isometry condition, and the reason no shell of the plain form is a group.
- *One-Sided Operators on the Biquaternion Algebra* (`articles_maths/one-sided-operators-on-the-biquaternion-algebra.md`), the companion article, for the factors $L_{\tilde Q_5}$ and $R_{\tilde Q_3}$, the swap $L^{\approx}=R$, and the one-sided form-preserving theorem used in the proof of the isometry criterion.
- *The Four Adjoints of the Two Algebras and the Two Sesqualgebras in Examples* (`articles_maths/the-four-adjoints-of-the-two-algebras-and-the-two-sesqualgebras-in-examples.md`), for the associate $F^{\approx}$, the basis rule $(e_\mu[\,]e_\nu)^{\approx}=e_\nu[\,]e_\mu$, and the reversal $(FG)^{\approx}=G^{\approx}F^{\approx}$.
- *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure* (`articles_maths/the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.md`), for $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}$ as the operator algebra and the two-sided operators as the decomposable tensors.
- *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/the-4-forms-over-the-biquaternioid-c-space.md`), for the place of $\langle\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ among the pairings of the algebra.
- *Zero Divisors of the Biquaternion Algebra* (`articles_maths/zero-divisors-of-the-biquaternion-algebra.md`), for the null parameters and the complementary zero divisor pairs that the skew criterion excludes.
- *Square Roots of a General Element in the Biquaternion Algebra* (`articles_maths/square-roots-of-a-general-element-in-the-biquaternion-algebra.md`), for the square-root problem in the algebra, whose solutions are the involutive parameters of the form-preserving criterion.
