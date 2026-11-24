# __Introduction to the Spin-$\tfrac32$ Bispinor Spaces__

## Introduction

**The subject.** The space of the operators of the biquaternion algebra is an algebra of complex dimension sixteen, and it is the endomorphism algebra of a module of complex dimension four. This article introduces that module, its four weights, and the two families of spinor spaces it carries: the minimal left ideals and the minimal right ideals of $\operatorname{End}(\mathbb{B})$. It also explains why the label of the slot is $\tfrac32$ and not $\tfrac12$.

**The order of the article.** *The Slot of the Operators* identifies the module and proves that it is the third symmetric power of the minimal left ideal of the algebra. *The Four Coordinates of a Bispinor* reads the weights and the coordinate functionals. *The Two Families* constructs the minimal left and right ideals. *The Projective Line of Ideals* parametrises each family by the lines of the spinor plane and counts the orbit. *The Comparison with the Elements* relates the two rows and places the label.

**It assumes** *The Minimal Left Ideals of the Biquaternion Algebra*, *The Carriers, the Representation, the Spin and the Closure* and *$\operatorname{End}(\mathbb{B})$ as an Algebra: the Regular Representation*. **The row of the elements is** where the spinor space has dimension two.

**The result in one line.** The module of the operators is $V_{3/2}=\operatorname{Sym}^{3}S$, of complex dimension four and weights $\tfrac32,\tfrac12,-\tfrac12,-\tfrac32$, and its spinor spaces are two projective lines of copies of that module.

**Boundaries.** *Spinors and Dirac Spinors* builds the Dirac spinor from one space of each family; *The Fierz–Kofink Identities and the Classification of Spinors* treats the sixteen bilinears; the strata inside an ideal are *The Spin-$\tfrac32$ Bispinors and the Rank Strata* and *The Spin-$\tfrac32$ Bispinors and the Spectral Strata*.

Nothing below is a statement of physics. The units are $e_t,\vec e_x,\vec e_y,\vec e_z$, with $e_t$ the identity, $\vec e_x^2=\vec e_y^2=\vec e_z^2=-e_t$ and the products cyclic; $S$ is a minimal left ideal of $\mathbb{B}$, of complex dimension two; $\star$ is the star of the algebra; the operators are $L_a(X)=aX$, $R_b(X)=Xb$ and $T_{a,b}=L_aR_b$; and $\operatorname{tr}$ is the trace of an operator, read from its spectrum on the algebra.

## The Slot of the Operators

**The two rows.** At the row of the elements the algebra is the square of one slot, $\mathbb{B}\cong S\otimes S^{\star}$ with $S=V_{1/2}$ of complex dimension two. At the row of the operators the algebra is $\operatorname{End}(\mathbb{B})$, of complex dimension sixteen, and it is again the endomorphism algebra of a single module, because it is simple. That module has complex dimension four, and it is what the name spinor space of the row refers to.

**The cube.** The module is not a new object: the third symmetric power of the slot of the elements has dimension four and is irreducible for the copy,

$$
\dim_{\mathbb{C}}\operatorname{Sym}^{3}S=\binom{4}{3}=4,\qquad \operatorname{Sym}^{3}S=V_{3/2}.
$$

**Proposition.** The module of the operators is $V_{3/2}=\operatorname{Sym}^{3}S$. Its weight string is $\tfrac32,\tfrac12,-\tfrac12,-\tfrac32$, the raising operator carries the coefficient $\sqrt3$ on the first step, $2$ on the second and $\sqrt3$ on the third, and the Casimir is $\tfrac32\cdot\tfrac52=\tfrac{15}{4}$.

*Proof.* An irreducible carrier of the copy is determined by its largest weight, and the symmetric cube of the largest weight $\tfrac12$ has largest weight $\tfrac32$. The dimension then forces the string, since $2\cdot\tfrac32+1=4$. The three coefficients are $\sqrt{(j-m)(j+m+1)}$ at $j=\tfrac32$ for $m=\tfrac12,-\tfrac12,-\tfrac32$, which are $\sqrt3$, $2$ and $\sqrt3$. The Casimir is $j(j+1)$ at $j=\tfrac32$.

**The reading.** The label of the row is the label of the slot and not of a summand. The sixteen of the operators is the square of a four, as the four of the elements was the square of a two.

## The Four Coordinates of a Bispinor

**Definition.** A **bispinor** is an element of the module $V_{3/2}$. A **weight basis** is a chain $u_{3/2},u_{1/2},u_{-1/2},u_{-3/2}$ with $u_m$ of weight $m$ and with the raising operator carrying $u_m$ to a fixed non-zero multiple of $u_{m+1}$. In that basis a bispinor has four coordinates,

$$
Ξ_{\mathrm{wfn}}=Ξ_{\mathrm{wfn},3/2}u_{3/2}+Ξ_{\mathrm{wfn},1/2}u_{1/2}+Ξ_{\mathrm{wfn},-1/2}u_{-1/2}+Ξ_{\mathrm{wfn},-3/2}u_{-3/2}.
$$

**Proposition.** The four coordinates are the values of four functionals of weights $-\tfrac32,-\tfrac12,\tfrac12,\tfrac32$, and the functionals are a basis of the dual module. The coordinate of weight $-\tfrac32$ is the one that survives on the highest line, and it is the only one that does not vanish there.

*Proof.* A functional of weight $\mu$ takes the line of weight $m$ to the line of weight $m+\mu$; it is non-zero on that line only when $m+\mu=0$. The four functionals are therefore dual to the four lines, and reading a bispinor in the basis is the same as applying the four of them.

**The reading.** Four coordinates, and not two, is the whole difference between the two rows. The extra two are the price of the cube, and they form a weight string and not a degeneracy: the four weights are distinct.

## The Two Families

**Definition.** Let $\ell$ be a complex line of the module. The **left ideal at the line** is

$$
I_\ell=\{\,T\in\operatorname{End}(\mathbb{B}):T(V_{3/2})\subseteq\ell\,\},
$$

and, for a hyperplane $h$ of the module, the **right ideal at the hyperplane** is

$$
J_h=\{\,T\in\operatorname{End}(\mathbb{B}):T(h)=0\,\}.
$$

**Proposition.** $I_\ell$ is a minimal left ideal and $J_h$ a minimal right ideal, each of complex dimension four; the product of an element of $I_\ell$ with an element of $J_h$ lies in $I_\ell\cap J_h$, which is the line of the operators whose image is $\ell$ and whose kernel is $h$.

*Proof.* An operator with image in $\ell$ is determined by a functional on the module, so the space has dimension $1\cdot4=4$, and a composite $TU$ still has image in $\ell$. The statement for $J_h$ is the same one read on the other side; the intersection consists of the operators with image $\ell$ and kernel containing $h$, one complex line.

**Corollary.** The two families are different: a member of one meets a member of the other in a point of the projective space of the sixteen.

*Proof.* Dimension: a left ideal is four-dimensional and a right ideal is four-dimensional inside a sixteen; their intersection is a line, not the zero space, and a line is a point of the projective space.

**The reading.** A spinor is a point of a left ideal and a conjugate spinor a point of a right ideal; the pairing between the two families is the trace form.

## The Projective Line of Ideals

**Definition.** For a unit spinor $u\in S$ put $\ell_u=\mathbb{C}u^{3}$, the line of the pure cube, and let $E_u$ be the projector of the module onto $\ell_u$ along the orthogonal complement for the trace form. The idempotent of the row at $u$ is $E_u$, and the spinor space at $u$ is $I_{\ell_u}$.

**Proposition.** The map $u\mapsto\ell_u$ carries the projective line of the spinor plane into the projective space of the module, and the copy acts on the image transitively, with the Borel as stabiliser and the count

$$
3=\dim\operatorname{SL}_2=1+2=\dim\mathbb{P}(S)+\dim(\text{stabiliser}).
$$

*Proof.* A unit spinor is defined up to a scalar, so the parameter is a point of $\mathbb{P}(S)$, of complex dimension one. The copy carries $u$ to $gu$ and therefore $u^3$ to $(gu)^3$, so it acts transitively on the pure cubes. The stabiliser of the line of $u^3$ is the set of elements fixing the line of $u$, which is the group of an upper triangular shape, of dimension two.

**Corollary.** Each family is a projective line of copies of the module, and the idempotents of the row are parametrised by the primitive idempotents $\tfrac12(e_t+i\vec u_{\mathrm r})$ of the algebra, hence by the unit real axes, hence again by a projective line.

*Proof.* The primitive idempotents are the elements $\tfrac12(e_t+i\vec u_{\mathrm r})$ for a unit real axis, and the axes form a two-sphere, which is a projective line.

**The reading.** The family is one-dimensional although the module is four-dimensional: the parameter is the line of the spinor of the elements, not the line of the module. The cubing carries one projective line into the other.

## The Comparison with the Elements

**Proposition.** The spinor of the elements has two coordinates and the spinor of the operators four; the module of the operators is the cube of the module of the elements, and the label of the row is three times the label of the element row.

*Proof.* The first number is the dimension of $S$, the second the dimension of $\operatorname{Sym}^3S$. The highest weight of a cube is three times the highest weight of its factor, and $3\cdot\tfrac12=\tfrac32$.

**Corollary.** The rise of the label from $\tfrac12$ to $\tfrac32$ triples the weight and doubles the dimension of the string, and $2s+1=\dim$ holds at both rows.

*Proof.* Three weights of the cube lie strictly between the extreme ones, so the string has length four and largest weight $\tfrac32$.

**The reading.** Nothing below uses an axis outside the parametrisation. The label $\tfrac32$ is a weight of a module of dimension four, and the four coordinates of a bispinor are the four weights counted once each.

## Further Reading

- [Spinors and Dirac Spinors](spinors-and-dirac-spinors.html), for the sum of a left and a right ideal and the two chiralities
- [The Minimal Left Ideals of the Biquaternion Algebra](the-minimal-left-ideals-of-the-biquaternion-algebra.html), for the idempotents, the minimality and the two families at the row of the elements
- [The Spin-$\tfrac32$ Bispinors and the Minimal Left Ideals](the-spin-three-halves-bispinors-and-the-minimal-left-ideals.html), for the same family read through the ideals alone
- [The Carriers, the Representation, the Spin and the Closure](the-carriers-the-representation-the-spin-and-the-closure.html), for the label of a slot and the two kinds of carrier
- [$\operatorname{End}(\mathbb{B})$ as an Algebra: the Regular Representation](end-b-as-an-algebra-the-regular-representation.html), for the sixteen, the trace form and the simplicity of the operator algebra
