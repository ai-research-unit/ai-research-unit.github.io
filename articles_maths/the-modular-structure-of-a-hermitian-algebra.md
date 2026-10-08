# __The Modular Structure of a Hermitian Algebra__

## Introduction

A Hermitian algebra carries an involution and a form, and the algebraic theory of that layer is in Part I. This article is its topological companion: it owns the completion-level operator theory, where the involution, the adjoint and the two-sided operators are read as operators on a Hilbert space.

Three things happen at the completion that cannot happen on the algebra alone. The involution is a bounded adjoint operation on the algebra but only a closable antilinear operator on the completion, and the operator recording the difference is the modular operator. The sandwich is bounded for the form and for the completion at once, and the comparison of its two adjoints is again the modular operator. And the intertwiners of the left representation form the commutant, on which the modular conjugation turns the adjoint into the involution of the algebra.

The material below was moved here from the Part I articles, whose algebraic statements remain there: *Hermitian Adjoints on a Hermitian Algebra*, *The Adjoint of the Left and the Right Multiplication*, *The Adjoint of the Sandwich on a Hermitian Algebra*, *The Two-Sided Operators on a Hermitian Algebra*, *The Adjoint of the Left Multiplication on a Hermitian Algebra* and *Adjoints of the Intertwiners of a Hermitian Algebra*. The adjoint of an operator under a Hermitian form is *The Adjoint under a Hermitian Form*, the polar decomposition of an operator of the form is *The Polar Decomposition of an Operator of the Form*, and the adjoint on a module is *The Hermitian Adjoint on a Hermitian Module*; none of those is re-derived here. The conventions are those of *Hermitian Algebras*: the algebra is $A$ with involution $\dagger$ and form $\langle\cdot,\cdot\rangle$, the completion is $H$ with cyclic vector $\xi=\iota(1)$, and $\jmath$ is the modular conjugation.

## The Involution on the Completion

**Proposition (the involution is an isometry exactly for a tracial form).** The involution is isometric for the form, $\langle x^{\dagger},y^{\dagger}\rangle = \langle y,x\rangle$, but it is bounded on the completion exactly when the form is tracial, $\langle xy,z\rangle = \langle y,xz\rangle$-symmetric; otherwise it is closable and unbounded.

**Proof.** $\langle x^{\dagger},y^{\dagger}\rangle = \langle y^{\dagger\dagger},x^{\dagger\dagger}\rangle$ by the adjoint axiom with the two sides exchanged, giving the isometry; the boundedness fails when the standard form has $\Delta\neq\mathrm{id}$, since the involution on $H$ is then the unbounded antilinear operator $S$.

### A Non-Tracial Example

For the Hermitian algebra of the group von Neumann algebra of a non-abelian infinite group with a non-tracial vector state, the involution is closable but unbounded on the completion, and its polar decomposition has a nontrivial modular operator: the involution is still the adjoint on the algebra and is no longer a bounded operator on the completion.

## The Modular Conjugation and the Exchange

**Theorem (the exchange).** Let $\jmath$ be the modular conjugation of the completion. Then

$$
\jmath\,\bar L_x\,\jmath = \bar R_{x^{\dagger}} , \qquad \jmath\,\bar R_x\,\jmath = \bar L_{x^{\dagger}} ,
$$

and consequently $\jmath\bar L_x^{*}\jmath = \bar R_x$: the modular conjugation turns the adjoint of a left multiplication into the right multiplication by the same element.

**Proof.** The modular conjugation satisfies $\jmath\mathcal{M}\jmath = \mathcal{M}^{c}$ and reverses products, by *The Modular Operator and Tomita-Takesaki Theory*; on the left multiplications this gives $\jmath\bar L_x\jmath = \bar R_{x^{\dagger}}$ as in *The Left and the Right Regular Representation*; applying the involution gives the second identity, and combining with the adjoint formula gives the third.

**Corollary (adjunction is the exchange of side).** For every $x$ the operator $\jmath\bar L_x^{*}\jmath$ is $\bar R_x$; so the Hermitian adjoint followed by the modular conjugation is the passage from the left representation to the right representation, and the two operations together generate the symmetry between an algebra and its commutant.

**Proof.** Substitute $\bar L_x^{*} = \bar L_{x^{\dagger}}$ into the theorem.

**Remark (three operations, one symmetry).** The involution reverses products; the Hermitian adjoint reverses the arrow; the modular conjugation exchanges the algebra with its commutant. On the left multiplications the three compose into the single symmetry between the left and the right regular representations, and this is why the modular conjugation is the natural home of the adjoint operation in a standard form.

## The Modular Operator

**Proposition (the sandwich commutes with the modular conjugation).** For every $x$ the sandwich is invariant under the modular conjugation of the standard form,

$$
\jmath\,\bar\Theta_x\,\jmath = \bar\Theta_x .
$$

So the two-sided operator is unchanged by the modular conjugation, which exchanges its two factors: $\jmath\bar L_x\jmath = \bar R_{x^{\dagger}}$ and $\jmath\bar R_{x^{\dagger}}\jmath = \bar L_x$.

**Proof.** Compose the two exchange identities established above.

**Corollary (the sandwich is an inner automorphism exactly for invertible parameters).** A sandwich $\Theta_x$ with $x$ invertible is the inner automorphism $\mathrm{Ad}_x$ of the algebra, and it preserves the form exactly when $x$ is unitary, in which case $x^{-1} = x^{\dagger}$; the correspondence $x\mapsto\Theta_x$ is a homomorphism of the unitary group onto the group of inner automorphisms of the form-preserving kind.

**Proof.** Multiplicativity is associativity of the product; preservation of the form is the unitarity condition; the inverse of a unitary element is its involution.

**Proposition (the modular flow).** The modular automorphism group $\sigma_t(a) = \Delta^{it}a\Delta^{-it}$ is implemented by the powers of the modular operator, and the modular conjugation inverts it, $\jmath\Delta^{it}\jmath = \Delta^{-it}$. The flow is generally **outer**: a sandwich realises an automorphism of the algebra only through an element of the algebra, and $\Delta^{it}$ is not such an element unless the algebra contains it.

**Proof.** The inversion is the modular conjugation theorem of *The Modular Operator and Tomita-Takesaki Theory*; the outerness is that $\Delta^{it}$ is defined through the modular operator and not through an element of the algebra.

**Remark (where the two theories of operators meet).** The sandwiches are the two-sided operators implemented by elements, that is, the inner automorphisms; the modular flow is implemented by the modular operator and is generally outer. The two theories meet at the invariance of the sandwich under the modular conjugation, which is the operator form of the exchange between the algebra and its commutant, and they separate at the outerness of the flow.

## The Modular Conjugation

**Theorem (the invariance).** Let $\jmath$ be the modular conjugation of the standard form. Then for every $x$

$$
\jmath\,\bar L_x\,\jmath = \bar R_{x^{\dagger}} , \qquad \jmath\,\bar R_{x^{\dagger}}\,\jmath = \bar L_x , \qquad \jmath\,\bar\Theta_x\,\jmath = \bar\Theta_x .
$$

So the modular conjugation exchanges the two factors of a two-sided operator and leaves the operator itself unchanged.

**Proof.** The first two identities are the exchange theorem established above; multiplying them gives $\jmath\bar L_x\bar R_{x^{\dagger}}\jmath = \bar R_{x^{\dagger}}\bar L_x = \bar\Theta_x$.

**Corollary (the fixed algebra of the conjugation).** The operators fixed by $T\mapsto\jmath T\jmath$ form the commutant of the pair, and the two-sided operators lie in it: so $\Theta_x$ belongs to the commutant of the algebra generated by the modular conjugation and the conjugation-invariant elements.

**Proof.** The fixed set of an involution is a subalgebra; the sandwiches lie in it by the theorem.

**Remark (why the invariance is structural).** The invariance is the operator statement that a two-sided object depends on an element and its involution only through the pair, and it is the reason the modular conjugation is the natural symmetry of the theory of two-sided operators: the sandwiches are exactly the operators whose left and right parts are exchanged by the conjugation without changing the operator.

## The Standard Form and the Self-Duality

**Definition.** The **standard form** of the algebra is the quadruple $(\mathcal{M}, H, \jmath, P)$ where $\mathcal{M}$ is the von Neumann algebra generated by the left multiplications, $\jmath$ the modular conjugation, and

$$
P = \overline{\{\Theta_x\xi : x\in\mathcal{M}\}} = \overline{\mathcal{M}_{+}\xi}
$$

the closure of the image of the positive cone under the cyclic vector.

**Theorem (self-duality).** The cone $P$ is **self-dual**:

$$
P = P^{\natural} := \{u\in H : [u,v]\geq0 \text{ for every } v\in P\} ,
$$

the modular conjugation fixes $P$ pointwise in the sense $\jmath P = P$, and $\Theta_xP\subseteq P$ for every $x\in\mathcal{M}$.

**Proof.** The self-duality is the cone theorem of the modular theory: $P^{\natural}\subseteq P$ because a vector in the dual cone is a limit of positive elements applied to $\xi$, and $P\subseteq P^{\natural}$ by the positivity of the sandwiches; the invariance $\jmath P = P$ follows from the matrix-valued version of $\jmath\Theta_x\jmath = \Theta_x$, which is $\jmath x\jmath = x^{*}$ acting on the cone; and the invariance of the cone under the sandwiches is the stabilisation of the positive cone under inner conjugation.

**Proposition (two-sided operators preserve the cone).** Every two-sided operator maps $P$ into $P$, and every operator preserving $P$ and commuting with the modular conjugation is a limit of two-sided operators.

**Proof.** The first statement is the last identity of the theorem; the second is the identification of the cone-preserving operators with the positive sandwiches.

**Remark (three equivalent structures).** In the standard form the algebra, the commutant and the self-dual cone are three aspects of one structure: the left multiplications generate the algebra, the modular conjugation exchanges it with the commutant, and the cone encodes the positivity that the modular theory needs to replace the missing Cauchy–Schwarz inequality. The two-sided operators are the maps that respect all three, which is why they are the natural morphisms of the standard form.

## The Tomita Operator

**Definition.** The **Tomita operator** of the Hermitian algebra is the antilinear map

$$
S : A\xi\longrightarrow A\xi , \qquad S(x\xi) = x^{\dagger}\xi ,
$$

with domain the dense subspace $A\xi$; its closure, when needed, is written $\bar S$.

**Proposition (elementary properties).** $S$ is antilinear, $S^{2} = \mathrm{id}$ on its domain, $S$ is isometric exactly when the form is tracial, and $S$ satisfies

$$
L_x^{*} = S\,R_x\,S \qquad \text{and} \qquad S\,L_x\,S = R_{x^{\dagger}} .
$$

**Proof.** Antilinearity is that of the involution; $S^{2}(x\xi) = S(x^{\dagger}\xi) = x\xi$; the identities are computed on $A\xi$: $SR_xS(y\xi) = SR_x(y^{\dagger}\xi) = S(y^{\dagger}x\xi) = (y^{\dagger}x)^{\dagger}\xi = x^{\dagger}y\xi = L_{x^{\dagger}}(y\xi)$, which is $L_x^{*}$ by the theorem, and $SL_xS(y\xi) = S(xy^{\dagger}\xi) = (xy^{\dagger})^{\dagger}\xi = yx^{\dagger}\xi = R_{x^{\dagger}}(y\xi)$.

**Corollary (the adjoint is a conjugation of the other side).** The adjoint of the left multiplication by $x$ is the right multiplication by $x$ conjugated by the Tomita operator, and the Tomita operator exchanges the two sides.

**Proof.** The first identity of the proposition.

**Remark (why the adjoint carries the modular operator).** The identity $L_x^{*} = SR_xS$ shows that the adjoint of a one-sided operator is obtained by conjugating the *other* one-sided operator with $S$, an operator that is not bounded unless the form is tracial. So the adjoint of the left multiplication, read through the cyclic vector, is exactly the involution, and read on the completion it is the modular operator in disguise; the two readings are reconciled by the polar decomposition of the next section.

## The Polar Decomposition

**Theorem (Tomita–Takesaki).** The closure of $S$ has a polar decomposition

$$
\bar S = J\,\Delta^{1/2} ,
$$

where $J$ is an antiunitary involution, $J^{2} = \mathrm{id}$, and $\Delta = \bar S^{*}\bar S$ is a positive self-adjoint operator, generally unbounded; equivalently $\bar S = J\Delta^{1/2}$, $\bar S^{*} = J\Delta^{-1/2}$ and $\Delta = \bar S^{*}\bar S$.

**Proof.** The operator $\bar S$ is closed and densely defined, so it has a polar decomposition $\bar S = U|\bar S|$, by the polar decomposition of *The Polar Decomposition of an Operator of the Form* read for the closed operator $S$, with $|\bar S| = (\bar S^{*}\bar S)^{1/2} = \Delta^{1/2}$ and $U$ a partial isometry with kernel $\ker\bar S$ and range $\overline{\mathrm{ran}\,\bar S}$; the involutivity $S^{2} = 1$ forces $\ker\bar S = \{0\}$, because $\bar Sy = 0$ with $0\in\mathrm{dom}\,\bar S$ gives $y = \bar S^{2}y = \bar S0 = 0$; hence $\overline{\mathrm{ran}\,|\bar S|} = (\ker|\bar S|)^{\perp} = H$ and $U$ is an antiunitary operator with $U^{2} = \mathrm{id}$, written $J$.

**Proposition (the identities carried by the decomposition).** With $S = J\Delta^{1/2}$ one has

$$
\Delta = \bar S^{*}\bar S , \qquad J\Delta J = \Delta^{-1} , \qquad J\,\Delta^{it}\,J = \Delta^{-it} ,
$$

and the modular group $t\mapsto\Delta^{it}$ is a one-parameter group of unitaries.

**Proof.** The first identity is the definition of $|\bar S|$; from $\bar S^{2} = 1$ and $\bar S = J\Delta^{1/2}$ one gets $\mathrm{id} = J\Delta^{1/2}J\Delta^{1/2}$, whence $J\Delta^{1/2}J = \Delta^{-1/2}$ and $J\Delta J = \Delta^{-1}$; the third identity follows by functional calculus.

**Corollary (the adjoint of the left multiplication recovered).** The adjoint of the left multiplication satisfies

$$
\bar L_x^{*} = \bar L_{x^{\dagger}} = S\,\bar R_x\,S = J\Delta^{1/2}\,\bar R_x\,J\Delta^{1/2} , \qquad \jmath\,\bar L_x\,\jmath = \bar R_{x^{\dagger}} ,
$$

the first identity being the conjugation by the Tomita operator and the second its bounded version, valid without the modular operator.

**Proof.** Substituting $S = J\Delta^{1/2}$ into $S\bar R_xS = \bar L_{x^{\dagger}}$ gives the displayed product; the second identity is the exchange theorem established above, and it needs no domain condition because $\jmath$ is antiunitary and the right multiplication is bounded.

**Remark (the deviation from a tracial form).** The form is tracial exactly when $\Delta = \mathrm{id}$, in which case $S = J$ is a bounded antiunitary involution and the adjoint of the left multiplication is bounded on $A$; the modular operator is therefore the quantitative description of the failure of the involution to be a bounded adjoint operation, and it is obtained from the adjoint of the left multiplication and nothing else.

## Self-Adjointness and Unitarity

The general criteria for an operator of a Hermitian form are *The Adjoint under a Hermitian Form*, §*Self-Adjoint, Normal and Unitary*; the following is their specialisation to the left multiplications.

**Theorem (the criteria).** For $x\in A$:

1. $\bar L_x$ is self-adjoint exactly when $x = x^{\dagger}$;
2. $\bar L_x$ is normal exactly when $xx^{\dagger} = x^{\dagger}x$;
3. $\bar L_x$ is unitary exactly when $x^{\dagger}x = xx^{\dagger} = 1$, that is when $x$ is a unitary element of the algebra;
4. $\bar L_x$ is positive exactly when $x$ lies in the positive cone of *Self-Adjoint Elements and the Positive Cone*.

**Proof.** Self-adjointness is $\bar L_x = \bar L_{x^{\dagger}}$ with the left representation faithful; normality is $\bar L_x\bar L_x^{*} = \bar L_{xx^{\dagger}}$ against $\bar L_x^{*}\bar L_x = \bar L_{x^{\dagger}x}$; unitarity adds the two equations of the normal case with the value $\mathrm{id}$; positivity is $\langle L_xy,y\rangle = \langle xy,y\rangle\geq0$ for all $y$, which is the definition of the positive cone.

**Corollary (unitary left multiplications form a group).** The unitary elements of $A$ form a group and the map $x\mapsto\bar L_x$ is a homomorphism of that group into the unitary group of $H$, with inverse $x\mapsto x^{\dagger}$.

**Proof.** $(xy)^{\dagger}(xy) = y^{\dagger}x^{\dagger}xy = 1$ for unitary $x,y$; multiplicativity of the left representation.

**Proposition (the modular flow on the left multiplications).** The modular group acts by

$$
\Delta^{it}\,\bar L_x\,\Delta^{-it} = \bar L_{\sigma_t(x)} , \qquad \sigma_t(x) = \Delta^{it}x\Delta^{-it} ,
$$

so the modular automorphism of the algebra is the conjugation of the left multiplication by the modular operator.

**Proof.** The modular group is implemented by unitaries of the standard form; the conjugation of a left multiplication is the left multiplication by the conjugated element, by *The Modular Operator and Tomita-Takesaki Theory*.

**Remark (what the adjoint alone cannot see).** The adjoint of the left multiplication sees the involution, hence the real form, and it sees the modular operator through $S$; it does not see the *boundedness* of the involution, which is a property of the form and is decided by whether $\Delta = \mathrm{id}$. The unbounded aspects of the modular operator, its domain and its spectral theory, are deferred with the modular operator itself to *The Modular Operator and Tomita-Takesaki Theory* and to the analysis of *Analysis on Linear Spaces* (Part III).

## The Commutant as the Algebra of Intertwiners

**Definition.** For a representation $\pi$ of $A$ on $H$ the **commutant** is

$$
\pi(A)' = \{\,T\in B(H) : T\pi(x) = \pi(x)T \text{ for every } x\,\} ,
$$

the set of intertwiners of the representation with itself.

**Theorem (the commutant is a $\ast$-algebra of intertwiners).** $\pi(A)'$ is a unital algebra closed in the weak operator topology and closed under adjunction; for the standard representation of a Hermitian algebra it is generated by the right multiplications, $\pi(A)' = \{\bar R_x : x\in A\}''$.

**Proof.** Closure under multiplication and adjunction is immediate from $T\pi(x) = \pi(x)T$ by taking adjoints as in *Adjoints of the Intertwiners of a Hermitian Algebra*; the weak operator closure is the von Neumann bicommutant theorem of *Von Neumann Algebras and the Hilbert Algebra Completeness*; the generation by the right multiplications is the double commutant statement of *The Left and the Right Regular Representation*.

**Corollary (the adjoint is the involution seen from the commutant).** On the commutant the adjoint operation is the operation that the involution induces on the algebra, so the commutant of a Hermitian algebra is a Hermitian algebra in its own right, and the map $x\mapsto\bar R_x$ is a $\ast$-anti-isomorphism of $A$ onto the commutant's dense part.

**Proof.** $\bar R_x^{*} = \bar R_{x^{\dagger}}$ by *The Adjoint of the Left and the Right Multiplication*, so the anti-isomorphism carries the involution to the adjoint.

## The Polar Decomposition and the Standard Form

**Theorem (the polar decomposition stays in the class).** Let $T$ be a closed intertwiner. Then $T^{*}T$ is a positive self-adjoint intertwiner, $|T| = (T^{*}T)^{1/2}$ is an intertwiner, and the partial isometry $U$ of the polar decomposition $T = U|T|$ is an intertwiner; so the class of intertwiners is closed under the polar decomposition.

**Proof.** $T^{*}T$ commutes with the representation because $T$ and $T^{*}$ do, whence $|T|$ and hence $U = T|T|^{-1}$ on the orthogonal complement of the kernel commute with it too.

**Theorem (the modular transpose and the standard form).** Let $\jmath$ be the modular conjugation of the standard form. Then

$$
T\ \longmapsto\ T^{\flat} = \jmath\,T^{*}\jmath
$$

is an antilinear involution of the operator algebra that maps the commutant onto the algebra, $\{\jmath T^{*}\jmath : T\in\pi(A)'\} = \pi(A)$, and it satisfies $(ST)^{\flat} = T^{\flat}S^{\flat}$; so the modular conjugation implements the self-duality of the standard form and turns the adjoint of an intertwiner into the involution of the algebra.

**Proof.** $\jmath\pi(A)\jmath = \pi(A)'$ and $\jmath\pi(A)'\jmath = \pi(A)$ by *The Modular Operator and Tomita-Takesaki Theory*, whence the map takes the commutant onto the algebra; it is antilinear, involutive because $\jmath^{2} = \mathrm{id}$, and anti-multiplicative, $(ST)^{\flat} = T^{\flat}S^{\flat}$, because the adjoint reverses products; on the dense part $\jmath\bar R_x\jmath = \bar L_{x^{\dagger}}$, which is the involution of the algebra.

**Corollary (self-adjoint intertwiners are the fixed points of the transpose).** An intertwiner of the standard representation is self-adjoint exactly when $T^{\flat} = \jmath T\jmath$; the self-adjoint intertwiners are the real form of the commutant, and the positive intertwiners are the positive elements of the commutant, with the cone of *Self-Adjoint Elements and the Positive Cone*.

**Proof.** $T = T^{*}$ is equivalent to $T^{\flat} = \jmath T^{*}\jmath = \jmath T\jmath$; the real-form and positivity statements are the corresponding statements of the quotient algebra transported by the $\ast$-anti-isomorphism.

**Remark (what the adjoint of an intertwiner says).** The adjoint of an intertwiner is an intertwiner because the involution of the algebra is exactly the adjoint of the multiplications; the modular conjugation then turns this algebraic fact into the self-duality of the standard form: the algebra and its commutant are exchanged by $\jmath$, and the adjoint on one side is the involution on the other. There is one adjoint operation in the theory, and the intertwiners, the commutant and the algebra are three of its faces.

## Self-Adjoint Intertwiners

**Definition.** An intertwiner is **self-adjoint** when $T = T^{*}$, **positive** when $T$ is self-adjoint and $\langle T u,u\rangle\geq0$ for every $u$, and **unitary** when $T^{*}T = TT^{*} = \mathrm{id}$.

**Proposition (the spectral data of a self-adjoint intertwiner).** A self-adjoint intertwiner is a self-adjoint operator on $H$, and its spectral projections, its positive and negative parts and its modulus are intertwiners; the unitary intertwiners form a group.

**Proof.** The functional calculus of a self-adjoint operator is implemented by strong limits of polynomials in the operator, and a strong limit of intertwiners is an intertwiner; the unitary statement is $x\mapsto\bar L_x$ on the unitary group, or the corresponding statement in the commutant.

**Proposition (the commutant of the standard form is a Hermitian algebra).** With the involution $T\mapsto T^{*}$ and the form $(S,T) = \langle S\xi,T\xi\rangle$ the commutant is a Hermitian algebra whose completion is $H$, and its left regular representation is the right regular representation of $A$; the intertwiners of the commutant are the algebra itself.

**Proof.** The form is positive definite because $\xi$ is separating for the commutant; the involution is the adjoint $T\mapsto T^{*}$, which on the right multiplications is $\bar R_x\mapsto\bar R_{x^{\dagger}}$; the double commutant theorem gives $\pi(A)'' = \pi(A)'{}'$, whence the last statement.

## Summary

The involution of a Hermitian algebra is a bounded adjoint operation on the algebra and a closable antilinear operator on the completion, bounded exactly when the form is tracial; its closure is the **Tomita operator** $S(x\xi)=x^{\dagger}\xi$, whose polar decomposition $\bar S=J\Delta^{1/2}$ produces the modular conjugation and the modular operator. The **modular conjugation** exchanges the two sides, $\jmath\bar L_x\jmath=\bar R_{x^{\dagger}}$, fixes every two-sided operator, $\jmath\bar\Theta_x\jmath=\bar\Theta_x$, and realises the standard form $(\mathcal{M},H,\jmath,P)$ with its self-dual cone $P=P^{\natural}$. The **commutant** of the left representation is the algebra of intertwiners, generated by the right multiplications, and the modular transpose $T\mapsto T^{\flat}=\jmath T^{*}\jmath$ carries it onto the algebra; the polar decomposition of a closed intertwiner stays inside the class. The algebraic counterparts of all of these — the adjoint axiom, the sandwich and its adjoint, the intertwiners and their adjoints, the self-adjoint and unitary elements — are in the Part I articles named in the introduction.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$, $\dagger$, $\langle\cdot,\cdot\rangle$ | Hermitian algebra with involution and form |
| $H$, $\xi = \iota(1)$ | Completion and cyclic vector |
| $\bar L_x$, $\bar R_x$ | Left and right multiplication extended to $H$ |
| $S(x\xi) = x^{\dagger}\xi$ | Tomita operator, the closure of the involution |
| $\bar S = J\Delta^{1/2}$ | Polar decomposition of the Tomita operator |
| $\Delta = \bar S^{*}\bar S$ | Modular operator, $J\Delta J = \Delta^{-1}$ |
| $\jmath$ | Modular conjugation, $\jmath\bar L_x\jmath = \bar R_{x^{\dagger}}$ |
| $\Delta^{it}$ | Modular flow, $\sigma_t = \mathrm{Ad}\,\Delta^{it}$ |
| $(\mathcal{M},H,\jmath,P)$ | Standard form with self-dual cone $P = P^{\natural}$ |
| $\mathcal{M}^{c}$ | Commutant of the left representation |
| $T^{\flat} = \jmath T^{*}\jmath$ | Modular transpose of an intertwiner |

## Further Reading

- Jacques Dixmier, *Von Neumann Algebras* (North-Holland, 1981), for Hilbert algebras, the involution and the standard form.
- Serban Stratila and László Zsidó, *Lectures on von Neumann Algebras* (Abacus Press, 1979), for the Tomita operator and the self-dual cone.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 2 (Academic Press, 1986), for the modular operator and the polar decomposition of a closed operator.
- Masamichi Takesaki, *Tomita's Theory of Modular Hilbert Algebras and its Applications*, Lecture Notes in Mathematics 128 (Springer, 1970), for the modular conjugation and the standard form.
- Ola Bratteli and Derek W. Robinson, *Operator Algebras and Quantum Statistical Mechanics*, vol. 1 (Springer, 1987), for the standard form and the modular group.
