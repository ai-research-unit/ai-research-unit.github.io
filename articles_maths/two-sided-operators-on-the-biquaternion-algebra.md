# __Two-Sided Operators on the Biquaternion Algebra__

## Introduction

Let $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ be the biquaternion algebra with its natural conjugation ${}^{\natural}$ and the general plain bilinear form

$$
\langle\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}(\tilde Q_1\tilde Q_2),
$$

whose Gram matrix in the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ is $\mathrm{diag}(1,-1,-1,-1)$, and let $F^{\approx}$ be the associate, or transpose, of a $\mathbb{C}$-linear map for this form (*The Four Adjoints of the Biquaternion Algebra in Examples*).

For $\tilde Q_1,\tilde Q_2\in\mathbb{B}$ define the **two-sided operator**

$$
T_{\tilde Q_1,\tilde Q_2}:\mathbb{B}\longrightarrow\mathbb{B},\qquad
T_{\tilde Q_1,\tilde Q_2}(\tilde Q_3)=\tilde Q_1\,\tilde Q_3\,\tilde Q_2 ,
$$

the product of a left and a right multiplication, with the two parameters independent. The subscripts are read by position and not by number: **the first subscript is the left multiplier, the second the right multiplier, and the argument is the third slot.** The notation is the one of the ordinary two-sided multiplication of *The Sesquilinear Sandwich on the Biquaternion*, $T_{\tilde Q,\tilde Q_3}(\tilde Q_1)=\tilde Q\tilde Q_1\tilde Q_3$, and it is the product of the corpus's one-sided operators,

$$
T_{\tilde Q_1,\tilde Q_2}=L_{\tilde Q_1}R_{\tilde Q_2}.
$$

These operators are the subject of the article. They contain the one-sided ones as the two boundary cases $\tilde Q_2=e_t$ and $\tilde Q_1=e_t$, they contain every inner automorphism, and they are the elements of the enveloping algebra $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}$ read on the algebra itself.

The article is the parallel of *One-Sided Operators on the Biquaternion Algebra*, with one extra section, §*The Sandwich*, for the diagonal member that the sector articles study. The parallel is what isolates the cost of the second parameter. Three things change. The composition law **reverses the second slot**, $\tilde Q_2$ and $\tilde Q_4$ exchanging their places, because the right multiplications form an anti-representation. The adjoint **swaps the two parameters**, $(T_{\tilde Q_1,\tilde Q_2})^{\approx}=T_{\tilde Q_2,\tilde Q_1}$, because association is the transpose for the plain form, whereas the quaternionic adjoint keeps the side and the parameter. And the criteria become criteria on the **pair** and on its **product**: self-adjointness is $\tilde Q_2=\lambda\tilde Q_1$, preservation of the form is $\tilde Q_2\tilde Q_1=\pm e_t$, multiplicativity, for a nonzero operator, is $\tilde Q_1\tilde Q_2=e_t$. No norm enters any of the three, which is the second sharp difference from the quaternionic pair, where the corresponding criteria turn on $\langle\cdot\rangle_{\natural}$. It is for the same reason that the form selects no shell of parameters, and the isometry group of the family is computed in §*The Isometry Group and the Absence of a Pin Group*: every unit acts, with the second parameter forced to $\pm\tilde Q_1^{-1}$, and the form's own quadratic form is not multiplicative, so the level set that would serve as a pin group is not a group.

**The bilinear sandwich is the diagonal of the family.** The sector articles *The Sandwich of a N-Regular, Spectrally Regular Biquaternion* and its three companions study the member

$$
\Theta_{\tilde Q}=T_{\tilde Q,\tilde Q^{*}},
$$

whose two parameters are tied by the Hermitian conjugation. §*The Bilinear Sandwich* defines it, separates it from the literal diagonal $T_{\tilde Q,\tilde Q}$ and from the inner automorphism $T_{\tilde Q,\tilde Q^{-1}}$, and records the dependence on the parameter: the family is bilinear in its pair of parameters, while the bilinear sandwich is quadratic in its single parameter, $\Theta_{\lambda\tilde Q}=\lvert\lambda\rvert^{2}\Theta_{\tilde Q}$. The matrix readings are *$M_2(\mathbb{C})$ Model : The Sandwich* and *$M_4(\mathbb{C})_L$ Model : The Sandwich*.

The algebra, the conjugations and the remarkable subspaces are *The Biquaternion Algebra*, *The Group of Involutions* and *The Six Subspaces*; the form and its pairings are *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*; the enveloping algebra and the two-sided operators as its elements are *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*; the one-sided factors are *One-Sided Operators on the Biquaternion Algebra*.

## The Two-Sided Family

**Definition.** For $\tilde Q_1,\tilde Q_2\in\mathbb{B}$ the **two-sided operator of the pair $(\tilde Q_1,\tilde Q_2)$** is the $\mathbb{C}$-linear map

$$
T_{\tilde Q_1,\tilde Q_2}(\tilde Q_3)=\tilde Q_1\,\tilde Q_3\,\tilde Q_2 .
$$

The order of the subscripts is the order of the reading, left factor first, right factor second; no reversal is hidden in the definition. The reversal appears only in the composition law, where it belongs.

**Proposition (the family contains the one-sided operators).** With the unit in one slot,

$$
T_{\tilde Q_1,e_t}=L_{\tilde Q_1},\qquad T_{e_t,\tilde Q_2}=R_{\tilde Q_2}.
$$

The family is therefore the two-parameter extension of the one-sided pair, and the criteria below specialise to the criteria of the one-sided article at $\tilde Q_2=e_t$.

*Proof.* The unit acts by the identity in each slot.

**Proposition (bilinearity and the spanning set).** The assignment $(\tilde Q_1,\tilde Q_2)\mapsto T_{\tilde Q_1,\tilde Q_2}$ is bilinear and injective in each slot when the other parameter is fixed and a unit. The sixteen operators $e_\mu[\,]e_\nu$, $\mu,\nu\in\{t,x,y,z\}$, are linearly independent and therefore form a basis of $\mathrm{End}_{\mathbb{C}}(\mathbb{B})$:

$$
\dim_{\mathbb{C}}\mathrm{Span}\{\,T_{\tilde Q_1,\tilde Q_2}\,\}=16 .
$$

*Proof.* Bilinearity is the distributivity of the product. For the independence, the enveloping algebra $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}$ is isomorphic to $\mathrm{End}_{\mathbb{C}}(\mathbb{B})$ through $A\otimes B\mapsto L_AR_B=T_{A,B}$, and it has complex dimension $16$ (*The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*); the independence of the sixteen basis elements was verified by elimination on their matrices. Injectivity in the first slot at a unit $\tilde Q_2$ follows from $T_{\tilde Q_1,\tilde Q_2}(e_t)=\tilde Q_1\tilde Q_2$ and the invertibility of $\tilde Q_2$; the second slot is the same argument.

**Remark (the image is the decomposable tensors).** Under the isomorphism $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}\to\mathrm{End}_{\mathbb{C}}(\mathbb{B})$ the two-sided operators are the images of the **decomposable** tensors, and a general endomorphism is a sum of them. Projectively the image is the Segre variety $\mathbb{P}^3\times\mathbb{P}^3$, of dimension six, so the cone of two-sided operators has complex dimension seven, and a general element of $\mathrm{End}_{\mathbb{C}}(\mathbb{B})$ is a sum of at most four of them. That is the precise sense in which the two-sided family is the algebraic skeleton of the full operator algebra, and it is also why a sum of two-sided operators need not be two-sided: the decomposable tensors do not form a subspace. The count is also the answer to the dimension puzzle: the **parameters** are eight complex numbers, the **operators** they generate by linear combination are sixteen-dimensional, because the map is bilinear and not linear.

## The Composition Law

**Theorem (composition).** For all $\tilde Q_1,\tilde Q_2,\tilde Q_3,\tilde Q_4\in\mathbb{B}$,

$$
\boxed{\; T_{\tilde Q_1,\tilde Q_2}\circ T_{\tilde Q_3,\tilde Q_4}
=T_{\tilde Q_1\tilde Q_3,\ \tilde Q_4\tilde Q_2} \;},
$$

the parameters of the second slot reversing their order.

*Proof.* $T_{\tilde Q_1,\tilde Q_2}\bigl(T_{\tilde Q_3,\tilde Q_4}(\tilde Q)\bigr)=\tilde Q_1\bigl(\tilde Q_3\tilde Q\tilde Q_4\bigr)\tilde Q_2=\tilde Q_1\tilde Q_3\,\tilde Q\,\tilde Q_4\tilde Q_2$ by associativity.

**Corollary (the family is a monoid with reversed right factors).** The composition law makes the set of two-sided operators a submonoid of $\mathrm{End}_{\mathbb{C}}(\mathbb{B})$, isomorphic to the image of the monoid $\mathbb{B}\times\mathbb{B}^{\mathrm{opp}}$ under the bilinear map, with multiplication $(\tilde Q_1,\tilde Q_2)(\tilde Q_3,\tilde Q_4)=(\tilde Q_1\tilde Q_3,\tilde Q_4\tilde Q_2)$. The reversal in the second factor is the reason the family is not a direct product of two copies of the algebra.

**Corollary (invertibility and the units).** The operator $T_{\tilde Q_1,\tilde Q_2}$ is invertible if and only if $\tilde Q_1$ and $\tilde Q_2$ are units, with inverse

$$
\bigl(T_{\tilde Q_1,\tilde Q_2}\bigr)^{-1}=T_{\tilde Q_1^{-1},\tilde Q_2^{-1}} .
$$

The group of invertible two-sided operators is therefore the image of $\mathbb{B}^{\times}\times\mathbb{B}^{\times}$, and the kernel of the parametrisation is $\{(\lambda e_t,\lambda^{-1}e_t)\}$: the two-sided operator is the identity exactly for $\tilde Q_1\tilde Q_2=e_t$ with $\tilde Q_1$ central.

*Proof.* The inverse is verified by the composition law. For the converse, if the operator is invertible then it is injective, so $\tilde Q_1$ and $\tilde Q_2$ are units: a nonzero kernel of $\tilde Q_1$, say $\tilde Q_1\tilde Q=0$, gives $T_{\tilde Q_1,\tilde Q_2}(\tilde Q\tilde Q')=0$ for every $\tilde Q'$. For the kernel of the parametrisation, $T_{\tilde Q_1,\tilde Q_2}=\mathrm{id}$ reads $\tilde Q_1\tilde Q\tilde Q_2=\tilde Q$ for all $\tilde Q$; at $\tilde Q=e_t$ this gives $\tilde Q_1\tilde Q_2=e_t$, and substituting back gives $\tilde Q_1\tilde Q=\tilde Q\tilde Q_1$ for all $\tilde Q$, so $\tilde Q_1$ is central and $\tilde Q_2=\tilde Q_1^{-1}$ has the same central value.

**Corollary (the powers stay in the family).** For every $n\ge1$,

$$
\bigl(T_{\tilde Q_1,\tilde Q_2}\bigr)^{n}=T_{\tilde Q_1^{n},\tilde Q_2^{n}} .
$$

*Proof.* Induction on the composition law. The corollary is the reason the exponential of a two-sided operator generally leaves the family: $\exp(T_{\tilde Q_1,\tilde Q_2})$ is the operator $\tilde Q\mapsto\sum_{n\ge0}\frac{1}{n!}\tilde Q_1^{n}\tilde Q\tilde Q_2^{n}$, and a sum of decomposable tensors $\tilde Q_1^{n}\otimes\tilde Q_2^{n}$ is decomposable in degenerate cases only. In the one-sided case the same computation gives $\exp(L_{\tilde Q_1})=L_{\exp(\tilde Q_1)}$ and $\exp(R_{\tilde Q_2})=R_{\exp(\tilde Q_2)}$, because the parameter enters once and the series is the exponential of the parameter.

## The Bilinear Sandwich

**Definition.** The **bilinear sandwich** of $\tilde Q\in\mathbb{B}$ is the two-sided operator whose second parameter is the Hermitian conjugate of the first. **It is the default sandwich: an article that writes *the sandwich* with no qualifier means this operator.** The qualifier *bilinear* names the family it is cut from, the bilinear family $T_{a,b}$; it does not say that the operator is bilinear in $\tilde Q$, which it is not, as the next paragraph shows. The sector articles call it simply the **sandwich**.

$$
\Theta_{\tilde Q}=T_{\tilde Q,\tilde Q^{*}}=L_{\tilde Q}R_{\tilde Q^{*}},\qquad
\Theta_{\tilde Q}(\tilde X)=\tilde Q\,\tilde X\,\tilde Q^{*}.
$$

It is the member of the family on the graph $\tilde Q_2=\tilde Q_1^{*}$, and it is the object of the sector articles *The Sandwich of a N-Regular, Spectrally Regular Biquaternion*, *The Sandwich of a N-Regular, Spectrally Degenerate Biquaternion*, *The Sandwich of a N-Degenerate, Spectrally Regular Biquaternion* and *The Sandwich of a N-Degenerate, Spectrally Degenerate Biquaternion*, and of the two exponential companions.

**One bilinear family, one quadratic sandwich.** The family is **bilinear** in the pair $(\tilde Q_1,\tilde Q_2)$: the operator depends linearly on each parameter with the other fixed. The bilinear sandwich restricts the pair to the graph $\tilde Q_2=\tilde Q_1^{*}$. That graph is real-linear and not complex-linear, and the restriction of a bilinear map to it is **quadratic**, not sesquilinear:

$$
\Theta_{\lambda\tilde Q}=\lvert\lambda\rvert^{2}\Theta_{\tilde Q},\qquad
\Theta_{\tilde Q+\tilde P}=\Theta_{\tilde Q}+\Theta_{\tilde P}+T_{\tilde Q,\tilde P^{*}}+T_{\tilde P,\tilde Q^{*}} .
$$

**Not the sesquilinear sandwich.** The two qualifiers are complementary. The *sesquilinear sandwich* $S_{a,b}=T_{a,b}\circ\varkappa$, that is $S_{a,b}(\tilde X)=a\tilde X^{*}b$, of *The Sesquilinear Sandwich on the Biquaternion* puts the star on the **argument**. The bilinear sandwich $\Theta_{\tilde Q}=T_{\tilde Q,\tilde Q^{*}}$ puts it on the **second parameter** and leaves the argument alone. The two agree only on the fixed space of the star, $\tilde X=\tilde X^{*}$, and are different operators on the algebra. The adjective *sesquilinear* describes $S$; the bilinear sandwich is quadratic in $\tilde Q$. The family has two independent complex parameters; the bilinear sandwich has one complex parameter, entering twice, once conjugated. It is quadratic because it is the graph $(\tilde Q,\tilde Q^{*})$ inside a bilinear family.

**The diagonal that closes.** The literal diagonal $T_{\tilde Q,\tilde Q}$, $\tilde X\mapsto\tilde Q\tilde X\tilde Q$, is not a subfamily. For non-commuting $\tilde Q,\tilde P$,

$$
T_{\tilde Q,\tilde Q}\circ T_{\tilde P,\tilde P}
=T_{\tilde Q\tilde P,\ \tilde P\tilde Q}
\neq T_{\tilde Q\tilde P,\ \tilde Q\tilde P},
$$

so the square does not compose. The starred diagonal does close, because the star is an anti-automorphism, $(\tilde Q\tilde P)^{*}=\tilde P^{*}\tilde Q^{*}$:

$$
\Theta_{\tilde Q}\circ\Theta_{\tilde P}
=T_{\tilde Q\tilde P,\ \tilde P^{*}\tilde Q^{*}}
=T_{\tilde Q\tilde P,\ (\tilde Q\tilde P)^{*}}
=\Theta_{\tilde Q\tilde P}.
$$

**Proposition (the sandwich is a homomorphism of the unit group).** On the units,

$$
\Theta_{\tilde Q}\,\Theta_{\tilde P}=\Theta_{\tilde Q\tilde P},
$$

so $\Theta$ is a group homomorphism $\mathbb{B}^{\times}\to GL_{\mathbb{C}}(\mathbb{B})$. It is not faithful. For $\lambda\in\mathbb{C}$,

$$
\Theta_{\lambda\tilde Q}=\lvert\lambda\rvert^{2}\Theta_{\tilde Q},
\qquad
\Theta_{\tilde Q}=\mathrm{id}\iff \tilde Q=\lambda e_t\ \text{with}\ \lvert\lambda\rvert=1 .
$$

The kernel is the central unit circle $U(1)$, so the sandwich descends injectively to $\mathbb{B}^{\times}/U(1)$ and the central phase is invisible: $\Theta_{e^{i\alpha}}=\mathrm{id}$.

*Proof.* The multiplicativity is the computation above. For the scaling, $\lambda\tilde Q\,\tilde X\,(\lambda\tilde Q)^{*}=\lvert\lambda\rvert^{2}\tilde Q\tilde X\tilde Q^{*}$. For the kernel, $\Theta_{\tilde Q}=\mathrm{id}$ at $\tilde X=e_t$ gives $\tilde Q\tilde Q^{*}=e_t$, so $\tilde Q$ is invertible with inverse $\tilde Q^{*}$; the identity then reads $\tilde Q\tilde X=\tilde X\tilde Q$ for all $\tilde X$, so $\tilde Q$ is central, and $\tilde Q\tilde Q^{*}=\lvert\tilde Q\rvert^{2}e_t=e_t$ gives $\lvert\tilde Q\rvert=1$.

**Proposition (the two sectors are preserved).** If $\tilde X^{*}=\tilde X$ then $(\tilde Q\tilde X\tilde Q^{*})^{*}=\tilde Q\tilde X\tilde Q^{*}$, and if $\tilde X^{*}=-\tilde X$ then the image is anti-Hermitian. The sandwich preserves each of the two real sectors $\mathbb{M}_+$ and $\mathbb{M}_-$.

**The matrix reading.** In the model $M_2(\mathbb{C})$ the sandwich is the congruence

$$
\Theta_M(X)=MXM^{\dagger},\qquad M=\mathsf M_2(\tilde Q),
$$

with $\det(MXM^{\dagger})=\lvert\det M\rvert^{2}\det X$. In the algebra,

$$
N\bigl(\Theta_{\tilde Q}(\tilde X)\bigr)=\lvert N(\tilde Q)\rvert^{2}N(\tilde X),
$$

where $N=\langle\cdot\rangle_{\natural}$ is the quaternionic norm. The sandwich is therefore, in general, a congruence and not an automorphism. For a unit $\tilde Q$, $\Theta_{\tilde Q}(\tilde X\tilde Y)=\Theta_{\tilde Q}(\tilde X)\Theta_{\tilde Q}(\tilde Y)$ holds exactly when $\tilde Q^{*}\tilde Q$ is central, that is when $\tilde Q$ is a scalar multiple of a $*$-unitary element.

**Three diagonal operators, three different objects.** The family contains three natural diagonal subfamilies, and they must not be confused:

| object | formula | property |
|---|---|---|
| bilinear sandwich | $T_{\tilde Q,\tilde Q^{*}}$ | congruence; preserves $\mathbb{M}_+$ and $\mathbb{M}_-$ |
| inner automorphism | $T_{\tilde Q,\tilde Q^{-1}}$ | algebra automorphism |
| literal diagonal | $T_{\tilde Q,\tilde Q}$ | not closed under composition |

The sandwich uses the star; the automorphism uses the inverse; the literal diagonal uses the same element twice and closes only for commuting parameters. Only the second is a representation of the algebra by automorphisms; only the first is the conformal Lorentz congruence of the sector articles.

**The adjoint of the sandwich.** For the plain form and for the Hermitian form alike, the adjoint of the sandwich is the sandwich of the conjugate parameter:

$$
\bigl(\Theta_{\tilde Q}\bigr)^{\approx}=\Theta_{\tilde Q^{*}},
\qquad
\bigl(\Theta_{\tilde Q}\bigr)^{\dagger}=\Theta_{\tilde Q^{*}} .
$$

The first identity is the swap theorem below applied to the pair $(\tilde Q,\tilde Q^{*})$; the second is the computation $\langle \tilde Q\tilde X\tilde Q^{*},\tilde Y\rangle_{*}=\langle\tilde X,\tilde Q^{*}\tilde Y\tilde Q\rangle_{*}$ with the Hermitian form $\langle\tilde X_1,\tilde X_2\rangle_{*}=\mathrm{Sc}(\tilde X_1\tilde X_2^{*})$. Consequently the sandwich is self-adjoint for either form exactly when $\tilde Q^{*}=\lambda\tilde Q$ for some $\lambda\in\mathbb{C}$.

## The Adjoint and the Swap

**Theorem (the adjoint exchanges the parameters).** For all $\tilde Q_1,\tilde Q_2\in\mathbb{B}$,

$$
\boxed{\; \bigl(T_{\tilde Q_1,\tilde Q_2}\bigr)^{\approx}=T_{\tilde Q_2,\tilde Q_1} \;}.
$$

*Proof.* The transpose of a composite reverses the order, $(FG)^{\approx}=G^{\approx}\circ F^{\approx}$ (*The Four Adjoints of the Biquaternion Algebra in Examples*), and the transposes of the factors are the crossed one-sided operators, $(L_{\tilde Q_1})^{\approx}=R_{\tilde Q_1}$ and $(R_{\tilde Q_2})^{\approx}=L_{\tilde Q_2}$ (*One-Sided Operators on the Biquaternion Algebra*):

$$
\bigl(T_{\tilde Q_1,\tilde Q_2}\bigr)^{\approx}=\bigl(R_{\tilde Q_2}\bigr)^{\approx}\bigl(L_{\tilde Q_1}\bigr)^{\approx}=L_{\tilde Q_2}R_{\tilde Q_1}=T_{\tilde Q_2,\tilde Q_1}.
$$

**Remark (swap, not conjugation).** The adjoint of a two-sided operator is a two-sided operator with the two parameters interchanged. The quaternionic pair of the corpus has the opposite behaviour: there the adjoint for the quaternionic form keeps the parameter, $(L_{\tilde Q_1})^{N}=L_{\tilde Q_1^{\natural}}$ and $(\Theta_{\tilde Q_1})^{N}=\Theta_{\tilde Q_1^{\natural}}$, so a type criterion is a criterion on one parameter. Here every type criterion is symmetric or antisymmetric in the pair $(\tilde Q_1,\tilde Q_2)$, and the whole article turns on that single difference.

## The Self-Adjoint and the Skew-Adjoint Sectors

**Theorem (the self-adjoint criterion).** For $\tilde Q_1\neq0$ the operator $T_{\tilde Q_1,\tilde Q_2}$ is self-adjoint if and only if the two parameters are proportional,

$$
\boxed{\; \bigl(T_{\tilde Q_1,\tilde Q_2}\bigr)^{\approx}=T_{\tilde Q_1,\tilde Q_2}
\iff \tilde Q_2=\lambda\tilde Q_1\quad\text{for some }\lambda\in\mathbb{C} \;}.
$$

Consequently the self-adjoint two-sided operators are the scalar multiples $\lambda\,T_{\tilde Q_1,\tilde Q_1}$ of the diagonal products, together with the zero operator.

*Proof.* In the matrix model put $A=\mathsf M_2(\tilde Q_1)\neq0$ and $B=\mathsf M_2(\tilde Q_2)$, so that the swap theorem reads $BXA=AXB$ for every $X\in M_2(\mathbb{C})$. Testing on the matrix units $X=E_{ij}$ gives $B_{ki}A_{jl}=A_{ki}B_{jl}$ for all $i,j,k,l$. Since $A\neq0$, choose $(k_0,i_0)$ with $A_{k_0i_0}\neq0$ and put $\lambda=B_{k_0i_0}/A_{k_0i_0}$; then $B_{jl}=\lambda A_{jl}$ for all $j,l$, so $B=\lambda A$ and $\tilde Q_2=\lambda\tilde Q_1$. The argument uses no inverse, so it covers the zero divisors as well. Conversely $\tilde Q_2=\lambda\tilde Q_1$ gives $\tilde Q_1\tilde Q\lambda\tilde Q_1=\lambda\tilde Q_1\tilde Q\tilde Q_1=T_{\tilde Q_1,\tilde Q_2}(\tilde Q)$.

**Theorem (the skew sector is trivial).** No nonzero two-sided operator is skew-adjoint:

$$
\bigl(T_{\tilde Q_1,\tilde Q_2}\bigr)^{\approx}=-T_{\tilde Q_1,\tilde Q_2}
\iff T_{\tilde Q_1,\tilde Q_2}=0 .
$$

*Proof.* Skew-adjointness is $T_{\tilde Q_2,\tilde Q_1}=-T_{\tilde Q_1,\tilde Q_2}$, that is $\tilde Q_2\tilde X\tilde Q_1=-\tilde Q_1\tilde X\tilde Q_2$ for all $\tilde X$. In the matrix model put $A=\mathsf M_2(\tilde Q_1)$ and $B=\mathsf M_2(\tilde Q_2)$, so the identity reads $BXA=-AXB$ for every $X$. On the matrix units it gives $B_{ki}A_{jl}=-A_{ki}B_{jl}$ for all $i,j,k,l$. If $A=0$ the operator is zero; otherwise choose $(k_0,i_0)$ with $A_{k_0i_0}\neq0$ and put $\mu=-B_{k_0i_0}/A_{k_0i_0}$; then $B_{jl}=\mu A_{jl}$ for all $j,l$, so $B=\mu A$. Substituting back gives $2\mu AXA=0$ for all $X$, and since $A\neq0$ the product $AXA$ is not identically zero, so $\mu=0$ and $B=0$. Conversely the zero operator is skew-adjoint.

**Corollary (the two sectors at the boundary).** At $\tilde Q_2=e_t$ the two criteria of this section give the one-sided criteria: $\tilde Q_2=\lambda\tilde Q_1$ becomes $\tilde Q_1$ central, and the skew condition becomes $\tilde Q_1=0$. The one-sided type criteria are therefore the boundary case of the two-sided ones, and the pair of articles is one theorem read on a family and on its slice.

## Automorphisms of the Form and Multiplicative Operators

**Theorem (the automorphisms of the form inside the family).** The operator $T_{\tilde Q_1,\tilde Q_2}$ preserves the general plain bilinear form,

$$
\bigl\langle T_{\tilde Q_1,\tilde Q_2}\tilde X_1,\ T_{\tilde Q_1,\tilde Q_2}\tilde X_2\bigr\rangle=\langle\tilde X_1,\tilde X_2\rangle\qquad\text{for all }\tilde X_1,\tilde X_2,
$$

if and only if $\tilde Q_2\tilde Q_1=\pm e_t$, that is if and only if $\tilde Q_2=\pm\tilde Q_1^{-1}$. In that case the operator is $\pm\mathrm{Ad}_{\tilde Q_1}$, the inner automorphism of $\tilde Q_1$ up to sign.

*Proof.* If the operator preserves the form it is injective, because the form is non-degenerate, hence $\tilde Q_1$ and $\tilde Q_2$ are units. Put $\tilde Q_6=\tilde Q_2\tilde Q_1$, so that $\tilde Q_2=\tilde Q_6\tilde Q_1^{-1}$, and compute with the cyclicity of the scalar part:

$$
\mathrm{Sc}\bigl(\tilde Q_1\tilde X_1\tilde Q_2\tilde Q_1\tilde X_2\tilde Q_2\bigr)
=\mathrm{Sc}\bigl(\tilde Q_1\tilde X_1\tilde Q_6\tilde X_2\tilde Q_6\tilde Q_1^{-1}\bigr)
=\mathrm{Sc}\bigl(\tilde Q_6\tilde X_1\tilde Q_6\tilde X_2\bigr)
=\bigl\langle\tilde X_1,\tilde Q_6\tilde X_2\tilde Q_6\bigr\rangle .
$$

Preservation is therefore equivalent to $\tilde Q_6\tilde X\tilde Q_6=\tilde X$ for all $\tilde X$, which by the one-sided theorem forces $\tilde Q_6=\pm e_t$ (*One-Sided Operators on the Biquaternion Algebra*, §*Which Multiplications Preserve the Form*). Conversely $\tilde Q_2=\tilde Q_1^{-1}$ gives the inner automorphism, which preserves the form, and $\tilde Q_2=-\tilde Q_1^{-1}$ gives its negative, which preserves the form up to the sign $(-1)^{2}=1$.

**Theorem (the multiplicative operators).** A nonzero operator $T_{\tilde Q_1,\tilde Q_2}$ is multiplicative,

$$
\bigl(T_{\tilde Q_1,\tilde Q_2}\tilde X_1\bigr)\bigl(T_{\tilde Q_1,\tilde Q_2}\tilde X_2\bigr)=T_{\tilde Q_1,\tilde Q_2}\bigl(\tilde X_1\tilde X_2\bigr)\qquad\text{for all }\tilde X_1,\tilde X_2,
$$

if and only if $\tilde Q_1\tilde Q_2=e_t$, that is $\tilde Q_2=\tilde Q_1^{-1}$; and then it is the inner automorphism $\mathrm{Ad}_{\tilde Q_1}$, an automorphism of the algebra for every unit $\tilde Q_1$.

*Proof.* The left side is $\tilde Q_1\tilde X_1\tilde Q_2\tilde Q_1\tilde X_2\tilde Q_2$ and the right side is $\tilde Q_1\tilde X_1\tilde X_2\tilde Q_2$, so the identity reads

$$
\tilde Q_1\tilde X_1\bigl(\tilde Q_2\tilde Q_1-e_t\bigr)\tilde X_2\tilde Q_2=0\qquad\text{for all }\tilde X_1,\tilde X_2 .
$$

In the matrix model the algebra is $M_2(\mathbb{C})$, where $AXC=0$ for all $X$ forces $A=0$ or $C=0$. Since $\tilde Q_1$ and $\tilde Q_2$ are nonzero, the identity first gives $(\tilde Q_2\tilde Q_1-e_t)\tilde X_2\tilde Q_2=0$ for all $\tilde X_2$, and then $\tilde Q_2\tilde Q_1=e_t$. The product $\tilde Q_2\tilde Q_1=e_t$ makes both parameters units, and then $\tilde Q_1\tilde Q_2=e_t$ and $\tilde Q_2=\tilde Q_1^{-1}$; conversely $\tilde Q_1\tilde Q_2=e_t$ makes the two sides equal for all $\tilde X_1,\tilde X_2$, and the operator is $\tilde X\mapsto\tilde Q_1\tilde X\tilde Q_1^{-1}$.

**Remark (the zero operator).** The zero operator is multiplicative and its product of parameters is $0$, not $e_t$. It is the only exception: if either parameter is zero the operator is zero, so the criterion is read on the nonzero operators.

**Corollary (multiplicative and form preserving).** The two-sided operators that are multiplicative and preserve the form at once are exactly the inner automorphisms $\mathrm{Ad}_{\tilde Q_1}$ with $\tilde Q_1$ a unit, without the sign $-\mathrm{Ad}_{\tilde Q_1}$: the sign that the criterion of the first theorem allows is excluded by multiplicativity.

**Corollary (the partial law of the central product).** Suppose the product of the two parameters is central, that is $\tilde Q_2\tilde Q_1=\mu e_t$ with $\mu=\mathrm{Sc}(\tilde Q_2\tilde Q_1)$. Then for all $\tilde X_1,\tilde X_2$,

$$
\bigl(T_{\tilde Q_1,\tilde Q_2}\tilde X_1\bigr)\bigl(T_{\tilde Q_1,\tilde Q_2}\tilde X_2\bigr)
=(\tilde Q_2\tilde Q_1)\,T_{\tilde Q_1,\tilde Q_2}(\tilde X_1\tilde X_2)
=\mu\,T_{\tilde Q_1,\tilde Q_2}(\tilde X_1\tilde X_2),
$$

and the multiplier is the central scalar $\tilde Q_2\tilde Q_1$, not a norm. The condition is automatic for $\tilde Q_2=\tilde Q_1^{-1}$, which is the exact criterion of the theorem above, but it is weaker: it holds for every pair whose product falls in the centre $\mathbb{C}e_t$, and the operator is then multiplicative up to that central scalar.

*Proof.* $\tilde Q_2\tilde Q_1$ is central by hypothesis, so it may be moved across $\tilde X_1$ in $\tilde Q_1\tilde X_1(\tilde Q_2\tilde Q_1)\tilde X_2\tilde Q_2$; substituting $\tilde Q_2\tilde Q_1=\mu e_t$ gives the second form.

**Remark (no norm enters, and the law is the weaker for it).** The quaternionic pair of the corpus reads the same two questions through the norm and carries the correspondingly stronger law: there $\Theta_{\tilde Q_1}(\tilde X_1)\Theta_{\tilde Q_1}(\tilde X_2)=\langle\tilde Q_1\rangle_{\natural}\,\Theta_{\tilde Q_1}(\tilde X_1\tilde X_2)$ holds for **every** parameter, with the norm as the scalar, and genuine multiplicativity up to a scalar is the condition $\langle\tilde Q_1\rangle_{\natural}=1$. Here the criteria are $\tilde Q_2\tilde Q_1=\pm e_t$ and $\tilde Q_1\tilde Q_2=e_t$: conditions on the product of the two parameters, in which no norm and no conjugation appears, and the partial law above holds only when that product is central. The two shapes are not the same theorem with different letters; the plain form carries no twist for a norm to absorb, so it loses the parameter-free law and keeps the criterion.

## The Isometry Group and the Absence of a Pin Group

**Theorem (the isometries of the family).** The map $T_{\tilde Q_1,\tilde Q_2}$ is an isometry of the plain form if and only if $\tilde Q_2\tilde Q_1=\pm e_t$. Equivalently, every unit $\tilde Q_1$ acts, with $\tilde Q_2=\pm\tilde Q_1^{-1}$, and the isometry group of the family is the image of the pairs $(\tilde Q_1,\pm\tilde Q_1^{-1})$.

*Proof.* The operator is invertible exactly when both parameters are units, and an invertible isometry has inverse its adjoint, so $T_{\tilde Q_1,\tilde Q_2}\circ T_{\tilde Q_2,\tilde Q_1}=\mathrm{id}$. By the composition law the composite is $T_{\tilde Q_1\tilde Q_2,\tilde Q_1\tilde Q_2}$, and $T_{\tilde A,\tilde A}=\mathrm{id}$ holds exactly when $\tilde A$ is central with $\tilde A^{2}=e_t$, that is $\tilde A=\pm e_t$. Hence $\tilde Q_1\tilde Q_2=\pm e_t$, equivalently $\tilde Q_2\tilde Q_1=\pm e_t$ for units, and the pairs with $\tilde Q_2=\pm\tilde Q_1^{-1}$ are exactly the solutions.

**Corollary (the two cosets and the dimension).** The isometries of the family are the operators

$$
T_{\tilde Q_1,\tilde Q_1^{-1}}=\mathrm{Ad}_{\tilde Q_1},\qquad T_{\tilde Q_1,-\tilde Q_1^{-1}}=-\mathrm{Ad}_{\tilde Q_1},
$$

and the two assignments are well defined and distinct. On a unit the inner automorphism depends on $\tilde Q_1$ only through its class in $\mathbb{B}^{\times}/\mathbb{C}^{\times}$, so the group is $\{\pm\mathrm{Ad}_{\tilde Q_1}\}\cong(\mathbb{B}^{\times}/\mathbb{C}^{\times})\times\{\pm1\}$, of complex dimension three; it is not all of $O_4(\mathbb{C})$, which has dimension six. The factor $\{\pm1\}$ is discrete and $\mathbb{B}^{\times}/\mathbb{C}^{\times}$ is connected, so the two cosets are the two components of the group.

**The quadratic form is the obstruction.** Put $\mathfrak{Q}(\tilde Q)=\mathrm{Sc}(\tilde Q^{2})$, the quadratic form polarised to the plain bilinear form. It is **not** multiplicative: the two elements $(5e_t+4\vec e_x)/3$ and $(5e_t+4\vec e_y)/3$ both have $\mathfrak{Q}=1$, while their product has $\mathfrak{Q}=-431/81$. The level set $\{\mathfrak{Q}=\pm1\}$ is therefore not closed under multiplication, and no scalar condition on one parameter can cut a subgroup out of the family.

**Corollary (no pin group inside the family, and the kernel).** The isometry group of the plain form inside this family is $\{\pm\mathrm{Ad}_{\tilde Q_1}\}$, of complex dimension three, and it is not a pin group. A pin group needs a multiplicative form whose level set is a subgroup, and $\mathfrak{Q}$ is not multiplicative; the pin group of the quadratic space is the one built in the Clifford algebra, of dimension six, and it is not contained in the family. The isometry condition here is a condition on the **pair** of parameters, $\tilde Q_2\tilde Q_1=\pm e_t$, not on either parameter alone. The kernel of $(\tilde Q_1,\tilde Q_2)\mapsto T_{\tilde Q_1,\tilde Q_2}$ is $\{(\lambda e_t,\lambda^{-1}e_t)\}\cong\mathbb{C}^{\times}$, so the isometry group is the quotient of the pairs $(\tilde Q_1,\pm\tilde Q_1^{-1})$ by this kernel.

**The reflections lie outside the family.** For $\tilde Q_4$ with $\mathfrak{Q}(\tilde Q_4)\neq0$ the reflection of the plain form in the direction $\tilde Q_4$ is

$$
\rho_{\tilde Q_4}(\tilde Q)=\tilde Q-\frac{2\langle\tilde Q,\tilde Q_4\rangle}{\mathfrak{Q}(\tilde Q_4)}\tilde Q_4 .
$$

*Proof.* The reflection formula is the definition of the reflection of a quadratic space, so $\rho_{\tilde Q_4}$ is an isometry and its determinant is $-1$. For the second statement, three cases exhaust the directions. If $\tilde Q_4=\lambda e_t$ is central, $\rho_{\lambda e_t}=\operatorname{diag}(-1,1,1,1)$: it negates the centre, so it is not $+\mathrm{Ad}$, and if it were $-\mathrm{Ad}_{\tilde Q_1}$ then $\mathrm{Ad}_{\tilde Q_1}$ would act as $-\mathrm{id}$ on $V$, of determinant $-1$, whereas every inner automorphism acts on $V$ with determinant $+1$. If $\tilde Q_4\in V$ is pure, $\rho_{\tilde Q_4}$ fixes the centre and acts as $-1$ on the line $\mathbb{C}\tilde Q_4$ and as $+1$ on its orthogonal complement in $V$, so it is neither $+\mathrm{Ad}$, whose restriction to $V$ has determinant $+1$, nor $-\mathrm{Ad}$, which negates the centre. If $\tilde Q_4$ is mixed, $\rho_{\tilde Q_4}(e_t)=e_t-2Q_{4t}\mathfrak{Q}(\tilde Q_4)^{-1}\tilde Q_4$ has a nonzero vector part, so the reflection moves the centre, while $\pm\mathrm{Ad}$ preserves the line $\mathbb{C}e_t$. Equivalently, under $\mathrm{End}_{\mathbb{C}}(\mathbb{B})\cong\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}$ a two-sided operator is the elementary tensor $\tilde Q_1\otimes\tilde Q_2$, and the coefficient matrix of a reflection is not one.

A product of two reflections in directions of $V$ is back in the family, $\rho_{\vec e_x}\rho_{\vec e_y}=\mathrm{Ad}_{\vec e_z}$ for the orthogonal pure directions, and every such product is an inner automorphism; a product of an odd number of reflections is not two-sided, and a product of two reflections of the whole space in general directions need not be. The improper isometries are therefore not operators of the algebra: their carrier is the Clifford algebra of the form, in its odd slot, where the reflection in a non-isotropic vector is $\rho_u(v)=-uvu^{-1}$ (*Biquaternion Versors and the Orthogonal Group*, *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*).

**Remark (the quaternionic twin, in one line).** There the sandwich $\Theta_{\tilde Q_1}$ is an isometry exactly when $\langle\tilde Q_1\rangle_{\natural}=\pm1$, the level set is a group because the norm is multiplicative, and the reflections of the vector subspace lie inside the family. Here nothing is selected, the shell is not a group, and the reflections lie outside. The difference has one source: the plain form is the scalar part of the algebra's own product, while the quaternionic form carries the norm as a twist.

## Worked Examples

**The identity and its multiples.** $T_{e_t,e_t}=\mathrm{id}$, self-adjoint and form preserving; the central multiples $\lambda\,\mathrm{id}=T_{\lambda e_t,e_t}$ are self-adjoint for every $\lambda$, preserve the form only for $\lambda=\pm1$, and are multiplicative only for $\lambda=1$: the three criteria are genuinely different, and the example separates them.

**A mixed operator.** The operator $\tilde Q\mapsto \vec e_x\tilde Q\vec e_y=T_{\vec e_x,\vec e_y}$ has $\tilde Q_2\tilde Q_1=\vec e_y\vec e_x=-\vec e_z$, so by the criteria it is neither self-adjoint (the parameters are not proportional), nor form preserving ($-\vec e_z\neq\pm e_t$), nor multiplicative. Its adjoint is $T_{\vec e_y,\vec e_x}$, the parameter pair exchanged, and the two operators differ, since $\vec e_x\vec e_z\vec e_y$ and $\vec e_y\vec e_z\vec e_x$ have opposite signs.

**An inner automorphism.** For the pure unit $\tilde Q_1=\vec e_x$ one has $\tilde Q_1^{-1}=-\vec e_x$, so

$$
\mathrm{Ad}_{\vec e_x}=T_{\vec e_x,\vec e_x^{-1}}=T_{\vec e_x,-\vec e_x},
$$

and the three criteria hold at once: the parameters are proportional with $\lambda=-1$, so the operator is self-adjoint; $\tilde Q_2\tilde Q_1=(-\vec e_x)\vec e_x=e_t$, so it preserves the form; and $\tilde Q_2=\tilde Q_1^{-1}$, so it is multiplicative. It is the least degenerate two-sided operator after the identity, and the example exercises the three criteria on one object.

**A self-adjoint operator with a null parameter.** For $\tilde Q=e_t+i\vec e_z$, a zero divisor with $\tilde Q^{2}=2\tilde Q\neq e_t$, the diagonal operator $T_{\tilde Q,\tilde Q}$ is self-adjoint by the criterion $\tilde Q_2=\lambda\tilde Q_1$ with $\lambda=1$, although the parameter is not a unit. The example records that self-adjointness is a condition on the pair and not on invertibility, in contrast with the form-preserving criterion, which forces both parameters to be units.

**A diagonal operator multiplicative up to sign.** For the pure unit $\tilde Q_1=\tilde Q_2=\vec e_x$ the product of the parameters is $\tilde Q_2\tilde Q_1=\vec e_x^{2}=-e_t$, central, so the partial law applies with the scalar $-1$:

$$
\bigl(T_{\vec e_x,\vec e_x}\tilde X_1\bigr)\bigl(T_{\vec e_x,\vec e_x}\tilde X_2\bigr)=-T_{\vec e_x,\vec e_x}(\tilde X_1\tilde X_2),
$$

and the operator $\tilde Q\mapsto \vec e_x\tilde Q\vec e_x$ is anti-multiplicative. It is the negative of the inner automorphism $\mathrm{Ad}_{\vec e_x}$, since $\vec e_x^{-1}=-\vec e_x$; the example is the least degenerate instance of the partial law, and it separates the central-product family from the genuinely multiplicative operators of the theorem. A general parameter does not qualify: for $\tilde Q_1=1+\vec e_x+(1+2i)\vec e_y$ the product with itself is not central, and no scalar makes the product law hold.

**The sandwich of a central phase.** For $\tilde Q=e^{i\alpha}e_t$ the sandwich is $\Theta_{\tilde Q}=\mathrm{id}$: the phase is invisible. For $\tilde Q=\vec e_x$ the sandwich is $\Theta_{\vec e_x}(\tilde X)=-\vec e_x\tilde X\vec e_x$, an involution, because $\vec e_x^{2}=-e_t$ and the sandwich is multiplicative. The two examples are the two extremes of the sandwich family: the central scalar collapses it to the identity, the pure unit gives a genuine involution.

## Summary

The two-sided operators are the products $T_{\tilde Q_1,\tilde Q_2}(\tilde Q_3)=\tilde Q_1\tilde Q_3\tilde Q_2$ of a left and a right multiplication with independent parameters; they contain the one-sided ones at the boundary cases and they are the decomposable tensors of the enveloping algebra $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}$, whose products span the whole operator algebra of complex dimension sixteen. The parameters are eight complex numbers and the operator algebra sixteen complex dimensions, because the map is bilinear. Composition reverses the second slot, $(\tilde Q_1,\tilde Q_2)(\tilde Q_3,\tilde Q_4)=(\tilde Q_1\tilde Q_3,\tilde Q_4\tilde Q_2)$, and the adjoint for the general plain bilinear form swaps the two parameters. The type criteria are criteria on the pair, and the automorphism and multiplicativity criteria on the product: self-adjoint exactly when $\tilde Q_2=\lambda\tilde Q_1$ (for $\tilde Q_1\neq0$), never skew-adjoint except for the zero operator, form preserving exactly when $\tilde Q_2\tilde Q_1=\pm e_t$, multiplicative for a nonzero operator exactly when $\tilde Q_1\tilde Q_2=e_t$; when the product $\tilde Q_2\tilde Q_1$ is merely central the operator is still multiplicative up to that central scalar, which is the weaker and differently shaped analogue of the quaternionic law $\Theta_{\tilde Q_1}(\tilde X_1)\Theta_{\tilde Q_1}(\tilde X_2)=\langle\tilde Q_1\rangle_{\natural}\Theta_{\tilde Q_1}(\tilde X_1\tilde X_2)$. The multiplicative and form-preserving operators are the inner automorphisms of the units, and no norm enters any criterion — the sharp contrast with the quaternionic pair of the corpus. At $\tilde Q_2=e_t$ all the criteria reduce to the one-sided ones.

The bilinear sandwich is the diagonal $\Theta_{\tilde Q}=T_{\tilde Q,\tilde Q^{*}}$, the member on the graph of the Hermitian conjugation. The family is bilinear and the bilinear sandwich is its restriction to the graph of the conjugation, hence quadratic in $\tilde Q$: $\Theta_{\lambda\tilde Q}=\lvert\lambda\rvert^{2}\Theta_{\tilde Q}$. The bilinear sandwich is a group homomorphism on the units with kernel $U(1)$, it preserves the two real sectors, and in the matrix model it is the congruence $X\mapsto MXM^{\dagger}$.

The isometries of the family are the two cosets $\pm\mathrm{Ad}_{\tilde Q_1}$, of complex dimension three, reached by every unit with the second parameter forced to $\pm\tilde Q_1^{-1}$ and no condition on a norm, and the two cosets are the two components; the shell $\mathfrak{Q}=\pm1$ is not closed, so the family contains no pin group; the kernel is $\mathbb{C}^{\times}$; and the reflections, of determinant $-1$, lie outside the family.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ | The general plain bilinear form; Gram matrix $\mathrm{diag}(1,-1,-1,-1)$ |
| $F^{\approx}$ | The associate, or transpose, of $F$ for this form |
| $T_{\tilde Q_1,\tilde Q_2}(\tilde Q_3)=\tilde Q_1\tilde Q_3\tilde Q_2$ | The two-sided operator of the pair $(\tilde Q_1,\tilde Q_2)$; first subscript left, second right, argument third |
| $T_{\tilde Q_1,e_t}=L_{\tilde Q_1}$, $T_{e_t,\tilde Q_2}=R_{\tilde Q_2}$ | The one-sided operators as boundary cases |
| $e_\mu[\,]e_\nu$, $\mu,\nu\in\{t,x,y,z\}$ | Basis of the family; independent, spanning $\mathrm{End}_{\mathbb{C}}(\mathbb{B})$ |
| $T_{\tilde Q_1,\tilde Q_2}\circ T_{\tilde Q_3,\tilde Q_4}=T_{\tilde Q_1\tilde Q_3,\tilde Q_4\tilde Q_2}$ | Composition; the second slot reverses |
| $(T_{\tilde Q_1,\tilde Q_2})^{n}=T_{\tilde Q_1^{n},\tilde Q_2^{n}}$ | Powers stay in the family |
| $(T_{\tilde Q_1,\tilde Q_2})^{\approx}=T_{\tilde Q_2,\tilde Q_1}$ | The adjoint swaps the parameters |
| Self-adjoint $\iff\tilde Q_2=\lambda\tilde Q_1$ | Type criterion of the family, for $\tilde Q_1\neq0$ |
| Skew-adjoint $\iff$ the operator is $0$ | The skew sector is trivial |
| $T_{\tilde Q_1,\tilde Q_2}$ preserves the form $\iff \tilde Q_2\tilde Q_1=\pm e_t$ | The automorphisms of the form in the family |
| $T_{\tilde Q_1,\tilde Q_2}$ multiplicative $\iff \tilde Q_1\tilde Q_2=e_t$ | For a nonzero operator; then $T_{\tilde Q_1,\tilde Q_1^{-1}}=\mathrm{Ad}_{\tilde Q_1}$ |
| $\tilde Q_2\tilde Q_1$ central $\implies$ multiplicative up to $\tilde Q_2\tilde Q_1$ | The partial law; the scalar is the central product, not a norm |
| $(\tilde Q_1,\tilde Q_2)\mapsto T_{\tilde Q_1,\tilde Q_2}$ | Bilinear; injective in each slot at a unit; kernel $\{(\lambda e_t,\lambda^{-1}e_t)\}$ |
| $\Theta_{\tilde Q}=T_{\tilde Q,\tilde Q^{*}}$ | The bilinear sandwich; the diagonal on the graph of the Hermitian conjugation; quadratic in $\tilde Q$, $\Theta_{\lambda\tilde Q}=\lvert\lambda\rvert^{2}\Theta_{\tilde Q}$ |
| $\Theta_{\tilde Q}\Theta_{\tilde P}=\Theta_{\tilde Q\tilde P}$, $\Theta_{\lambda\tilde Q}=\lvert\lambda\rvert^{2}\Theta_{\tilde Q}$ | The bilinear sandwich is a group homomorphism on the units; kernel $U(1)$ |
| $(\Theta_{\tilde Q})^{\approx}=\Theta_{\tilde Q^{*}}$, $(\Theta_{\tilde Q})^{\dagger}=\Theta_{\tilde Q^{*}}$ | The adjoint of the sandwich, for the plain and the Hermitian forms |
| $\{\pm\mathrm{Ad}_{\tilde Q_1}\}\cong(\mathbb{B}^{\times}/\mathbb{C}^{\times})\times\{\pm1\}$ | The isometries of the family, of complex dimension three, in two components |
| $\mathfrak{Q}(\tilde Q)=\mathrm{Sc}(\tilde Q^{2})=Q_t^{2}-Q_x^{2}-Q_y^{2}-Q_z^{2}$ | The quadratic form of the plain form; not multiplicative |
| $\rho_{\tilde Q_4}(\tilde Q)=\tilde Q-2\langle\tilde Q,\tilde Q_4\rangle\mathfrak{Q}(\tilde Q_4)^{-1}\tilde Q_4$ | The reflection; an isometry of determinant $-1$, not two-sided |

## Further Reading

- [The Four Adjoints of the Biquaternion Algebra in Examples](the-four-adjoints-of-the-biquaternion-algebra-in-examples.html), for the four adjoints of one two-sided operator and the self-adjointness criteria, of which the association column is the first; the associate $F^{\approx}$, the basis rule $(e_\mu[\,]e_\nu)^{\approx}=e_\nu[\,]e_\mu$, and the reversal $(FG)^{\approx}=G^{\approx}F^{\approx}$.
- [One-Sided Operators on the Biquaternion Algebra](one-sided-operators-on-the-biquaternion-algebra.html), the companion article, for the factors $L_{\tilde Q_1}$ and $R_{\tilde Q_2}$, the swap $L^{\approx}=R$, and the one-sided form-preserving theorem used in the proof of the form-preserving criterion.
- [The Sesquilinear Sandwich on the Biquaternion](the-sesquilinear-sandwich-on-the-biquaternion.html), for the ordinary two-sided multiplication $T_{\tilde Q,\tilde Q_3}(\tilde Q_1)=\tilde Q\tilde Q_1\tilde Q_3$ whose notation this article uses, and for the sesquilinear sandwich $S_{a,b}(\tilde X)=a\tilde X^{*}b$, a different operator: its star is on the argument, not on the right parameter.
- [The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure](the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.html), for $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}$ as the operator algebra and the two-sided operators as the decomposable tensors.
- [$M_4(\mathbb{C})_L$ Representation : The Two-Sided Operators on the Biquaternion Algebra](m4c-representation-the-two-sided-operators-on-the-biquaternion-algebra.html), for the sixteen matrices $T_{\mu\nu}=L_\mu R_\nu$ in the $M_4(\mathbb{C})_L$ model.
- [The Sandwich of a N-Regular, Spectrally Regular Biquaternion](the-sandwich-of-a-n-regular-spectrally-regular-biquaternion.html), for the sandwich $\Theta_{\tilde Q}=T_{\tilde Q,\tilde Q^{*}}$ on the regular sector: multiplicativity, the closed form, the scale, the cancelled phase, the image $CO^{+}(1,3)$ and the two spinor slots.
- [$M_2(\mathbb{C})$ Model : The Sandwich](the-sandwich-in-the-m2c-model.html) and [$M_4(\mathbb{C})_L$ Model : The Sandwich](the-sandwich-in-the-m4c-l-model.html), for the congruence reading, the two halves and the Lorentz action.
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the place of $\langle\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ among the pairings of the algebra.
- [N-Regularity and N-Degeneracy in the Biquaternion Algebra](n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the null parameters and the complementary zero divisor pairs that the skew criterion excludes.
- [Square Roots of an Element](square-roots-of-an-element.html), for the square-root problem in the algebra, whose solutions are the involutive parameters of the form-preserving criterion.
