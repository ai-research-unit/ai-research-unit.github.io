
# __Exact Sequences__

## Introduction

Exactness is the language in which module theory is stated once the objects themselves are understood. Instead of saying separately that a map is injective, that its image is a kernel, and that a quotient is isomorphic to something, one writes a single chain of modules and maps and requires that at each module the image of the incoming map equals the kernel of the outgoing one. The gain is that whole families of isomorphisms and decompositions become the exactness of one sequence, and that functors are classified by how much exactness they preserve.

Throughout, $R$ is a commutative ring with identity $1 \neq 0$ and modules are left $R$-modules, as in the preceding article of this category. The vocabulary fixed here — exactness, short exact sequence, splitting, left and right exactness, $\operatorname{Ext}$ — is used by every other article of the category. The snake lemma and the five lemma are the two diagram lemmas that make the language computable; both are proved here rather than quoted, because their proofs are the only place where the connecting maps are constructed.

Exactness is a condition on a sequence of modules and homomorphisms, and it is preserved by the familiar constructions in a way that is best organised by the language of functors. The article ends by recording which of the two functors attached to a module — $\operatorname{Hom}_R(M,-)$ and $-\otimes_R M$ — preserve which halves of a short exact sequence, since that asymmetry is the origin of the notions of projective, injective and flat module.

## Exactness

### Exactness at a Module

Let

$$
\cdots \longrightarrow M_{i+1} \xrightarrow{f_{i+1}} M_i \xrightarrow{f_i} M_{i-1} \longrightarrow \cdots
$$

be a sequence of $R$-modules and $R$-linear maps, indexed so that consecutive maps compose.

**Definition.** The sequence is **exact at $M_i$** if $\operatorname{im} f_{i+1}=\ker f_i$. It is **exact** if it is exact at every module that has both an incoming and an outgoing map. A sequence indexed by $\mathbb{Z}$ is exact if it is exact at every $M_i$.

Because $\operatorname{im} f_{i+1} \subseteq \ker f_i$ is equivalent to $f_i \circ f_{i+1}=0$, exactness is the conjunction of the always-testable vanishing of composites with the reverse inclusion. Exactness at one place says that the kernel of one map is exhausted by the image of the previous one: every element killed by $f_i$ comes from somewhere in $M_{i+1}$.

**Example.** For a homomorphism $f:M \to N$ the sequences

$$
0 \longrightarrow \ker f \longrightarrow M \xrightarrow{f} N, \qquad M \xrightarrow{f} N \longrightarrow \operatorname{coker} f \longrightarrow 0
$$

are exact, where $\operatorname{coker} f=N/\operatorname{im} f$. At the middle $M$ or $N$ respectively the condition is a tautology: the image of $\ker f \to M$ is $\ker f$ by definition, and the kernel of $N \to \operatorname{coker} f$ is $\operatorname{im} f$ by definition of the quotient.

### Injective and Surjective Maps

Three short exact pieces carry all the information.

**Proposition.** (i) $0 \to A \xrightarrow{f} B$ is exact if and only if $f$ is injective. (ii) $B \xrightarrow{g} C \to 0$ is exact if and only if $g$ is surjective. (iii) $0 \to A \xrightarrow{f} B \xrightarrow{g} C \to 0$ is exact if and only if $f$ is injective, $\operatorname{im} f=\ker g$, and $g$ is surjective; then $C \cong B/f(A)$.

*Proof.* The map $0 \to A$ has image $0$, and $\ker f=0$ is injectivity; the map $C \to 0$ has kernel $C$, and $\operatorname{im} g=C$ is surjectivity. For (iii), exactness at $A$ and $C$ gives (i) and (ii) and exactness at $B$ gives the middle condition; the first isomorphism theorem gives $C \cong B/\ker g=B/f(A)$. $\square$

The notation $0$ stands for the zero module, and a map from or to it is the only one that exists.

### Short Exact Sequences

**Definition.** A **short exact sequence** is an exact sequence of the form

$$
0 \longrightarrow A \xrightarrow{i} B \xrightarrow{q} C \longrightarrow 0 .
$$

It presents $B$ as an **extension** of $C$ by $A$: the submodule $i(A)$ is isomorphic to $A$, the quotient $B/i(A)$ is isomorphic to $C$, and the map $i$ identifies $A$ with a submodule whose quotient is $C$. Conversely, every submodule $A \subseteq B$ yields the short exact sequence $0 \to A \to B \to B/A \to 0$, and up to isomorphism every short exact sequence arises this way.

An extension is more than the pair of modules $A$ and $C$: the middle module $B$ and the way $A$ sits inside it are extra data. The standard example is

$$
0 \longrightarrow \mathbb{Z} \xrightarrow{\ \cdot 2\ } \mathbb{Z} \longrightarrow \mathbb{Z}/2\mathbb{Z} \longrightarrow 0,
$$

where the middle module is $\mathbb{Z}$ and not $\mathbb{Z}\oplus\mathbb{Z}/2\mathbb{Z}$; the difference is exactly the question of splitting, treated below.

### The Kernel–Cokernel Calculus

For an $R$-linear map $f:M \to N$ there are four modules attached to it: the **kernel** $\ker f$, the **image** $\operatorname{im} f$, the **cokernel** $\operatorname{coker} f=N/\operatorname{im} f$, and the **coimage** $\operatorname{coim} f=M/\ker f$. The first isomorphism theorem says that $f$ factors as

$$
M \xrightarrow{\ \text{projection}\ } \operatorname{coim} f \xrightarrow{\ \cong\ } \operatorname{im} f \xrightarrow{\ \text{inclusion}\ } N,
$$

a surjection followed by an isomorphism followed by an injection. In the language of exact sequences this says that $0 \to \ker f \to M \to \operatorname{coim} f \to 0$ and $0 \to \operatorname{im} f \to N \to \operatorname{coker} f \to 0$ are short exact, and that $\operatorname{coim} f \cong \operatorname{im} f$. The category of $R$-modules is additive and has kernels and cokernels with $\operatorname{coim} \cong \operatorname{im}$; this is what it means for it to be abelian, and it is the reason every computation below can be done by chasing elements.

## The Snake Lemma

### The Diagram

Consider $R$-modules and homomorphisms forming exact rows

$$
A \xrightarrow{\ f\ } B \xrightarrow{\ g\ } C \xrightarrow{\ \ } 0, \qquad 0 \xrightarrow{\ \ } A' \xrightarrow{\ f'\ } B' \xrightarrow{\ g'\ } C',
$$

together with maps $a:A \to A'$, $b:B \to B'$ and $c:C \to C'$ commuting with them, so that $g'f'=0$, $gf=0$, $f'a=bf$ and $g'b=cg$ all hold. The maps $a,b,c$ restrict to the induced maps $\ker a \to \ker b \to \ker c$ on kernels and induce $\operatorname{coker} a \to \operatorname{coker} b \to \operatorname{coker} c$ on cokernels, obtained by restricting and by passing to quotients. Thus $\ker a \to \ker b$ is the restriction of $f$, and $\operatorname{coker} a \to \operatorname{coker} b$ is induced by $f'$.

### The Connecting Homomorphism

The content of the lemma is a map from $\ker c$ to $\operatorname{coker} a$ that is not induced by any map of the diagram.

**Construction.** Let $c_0 \in \ker c \subseteq C$. Since $g$ is surjective, choose $b_0 \in B$ with $g(b_0)=c_0$. Then $g'(b(b_0))=c(g(b_0))=c(c_0)=0$, so $b(b_0) \in \ker g'=\operatorname{im} f'$, and since $f'$ is injective there is a unique $a_0' \in A'$ with $f'(a_0')=b(b_0)$. Define

$$
\partial(c_0)=a_0' \bmod \operatorname{im} a \ \in \operatorname{coker} a .
$$

**Well-definedness.** Two choices of lift differ by an element of $\ker g=\operatorname{im} f$, say $b_0$ and $b_0+f(a_1)$. Commutativity gives $b(b_0+f(a_1))=b(b_0)+b(f(a_1))=b(b_0)+f'(a(a_1))$, so the resulting preimage $a_0'+a(a_1)$ differs from $a_0'$ by an element of $\operatorname{im} a$, and the class in $\operatorname{coker} a$ is unchanged. The map $\partial$ is $R$-linear because the choices may be made linearly.

### The Snake Lemma

**Lemma (snake).** In the diagram above there is an exact sequence

$$
\ker a \longrightarrow \ker b \longrightarrow \ker c \xrightarrow{\ \partial\ } \operatorname{coker} a \longrightarrow \operatorname{coker} b \longrightarrow \operatorname{coker} c ,
$$

where the first two maps are the restrictions of $f$ and $g$ and the last two are induced by $f'$ and $g'$. If in addition $f$ is injective and $g'$ is surjective, the sequence extends to a long exact sequence

$$
0 \longrightarrow \ker a \longrightarrow \ker b \longrightarrow \ker c \xrightarrow{\ \partial\ } \operatorname{coker} a \longrightarrow \operatorname{coker} b \longrightarrow \operatorname{coker} c \longrightarrow 0 .
$$

*Proof.* Exactness at $\ker b$: the composite $\ker a \to \ker b \to \ker c$ is the restriction of $gf=0$, so it vanishes. Conversely, if $b_0 \in \ker b$ has $g(b_0)=0$, then $b_0 \in \ker g=\operatorname{im} f$, say $b_0=f(a_0)$, and $b(b_0)=0$ gives $f'(a(a_0))=b(f(a_0))=b(b_0)=0$, so $a(a_0)=0$ by injectivity of $f'$; thus $a_0 \in \ker a$ and $b_0$ is in the image.

Exactness at $\ker c$: that $\partial$ vanishes on the image of $\ker b$ is the computation $b_0 \in \ker b$ gives $b(b_0)=0$, hence $a_0'=0$. Conversely, if $\partial(c_0)=0$, then with the notation of the construction $a_0' \in \operatorname{im} a$, say $a_0'=a(a_1)$, and $b(b_0-f(a_1))=b(b_0)-f'(a(a_1))=0$, so $b_0-f(a_1) \in \ker b$ and its image under $g$ is $g(b_0)-g(f(a_1))=c_0-0=c_0$. Hence $c_0$ is in the image of $\ker b \to \ker c$.

Exactness at $\operatorname{coker} a$: the composite $\partial$ followed by the map induced by $f'$ sends $c_0$ to $f'(a_0')=b(b_0)$, which is zero in $\operatorname{coker} b$ because it lies in $\operatorname{im} b$. Conversely, if the class of $a_0'$ in $\operatorname{coker} a$ dies in $\operatorname{coker} b$, then $f'(a_0')=b(b_1)$ for some $b_1 \in B$, and $g'(b(b_1))=g'(f'(a_0'))=0$ forces $0=c(g(b_1))$, so $g(b_1) \in \ker c$; the construction applied to $g(b_1)$ with lift $b_1$ returns the class of $a_0'$. Hence the kernel of $\operatorname{coker} a \to \operatorname{coker} b$ is contained in the image of $\partial$.

Exactness at $\operatorname{coker} b$: the composite of the maps induced by $f'$ and $g'$ is induced by $g'f'=0$. Conversely, suppose the class of $b_0'$ in $\operatorname{coker} b$ maps to zero in $\operatorname{coker} c$, that is $g'(b_0') \in \operatorname{im} c$, say $g'(b_0')=c(c_0)$ for some $c_0 \in C$. Since $g$ is surjective, $c_0=g(b_0)$ for some $b_0 \in B$; then $g'(b_0'-b(b_0))=c(c_0)-c(g(b_0))=0$, so $b_0'-b(b_0) \in \ker g'=\operatorname{im} f'$, say $b_0'-b(b_0)=f'(a_0')$. Hence the class of $b_0'$ in $\operatorname{coker} b$ equals the class of $f'(a_0')$, which is the image of the class of $a_0'$ in $\operatorname{coker} a$. The two extra terms of the long sequence are obtained from the corresponding statements for $f$ injective and $g'$ surjective by the same argument at the ends. $\square$

### The Long Exact Sequence in Practice

The snake lemma is used in the form "a short exact sequence of complexes gives a long exact sequence in homology". Its most frequent concrete shape is the following: from a short exact sequence $0 \to A \to B \to C \to 0$ and an inclusion of one such sequence into another, it produces the connecting map that shifts degree by one. This is the mechanism by which $\operatorname{Ext}$ and $\operatorname{Tor}$ acquire their long exact sequences, and it is why the derived functors of a half-exact functor fit into one long sequence rather than into unrelated pieces.

## The Five Lemma and Its Relatives

### The Five Lemma

Consider $R$-modules $A_1,\dots,A_5$ and $B_1,\dots,B_5$, with exact rows

$$
A_1 \xrightarrow{\ \ } A_2 \xrightarrow{\ \ } A_3 \xrightarrow{\ \ } A_4 \xrightarrow{\ \ } A_5, \qquad B_1 \xrightarrow{\ \ } B_2 \xrightarrow{\ \ } B_3 \xrightarrow{\ \ } B_4 \xrightarrow{\ \ } B_5,
$$

and maps $\alpha_i:A_i \to B_i$ making the two rows into a commutative ladder.

**Lemma (five).** If $\alpha_1,\alpha_2,\alpha_4,\alpha_5$ are isomorphisms, then $\alpha_3$ is an isomorphism. More precisely, if $\alpha_2,\alpha_4$ are injective and $\alpha_1$ is surjective then $\alpha_3$ is injective, and if $\alpha_2,\alpha_4$ are surjective and $\alpha_5$ is injective then $\alpha_3$ is surjective.

*Proof.* Let the top horizontal maps be $\beta_i:A_i \to A_{i+1}$ and the bottom ones $\beta_i':B_i \to B_{i+1}$, so that $\alpha_{i+1}\beta_i=\beta_i'\alpha_i$ for each $i$.

Injectivity. Suppose $\alpha_2,\alpha_4$ injective and $\alpha_1$ surjective. Let $a_3 \in A_3$ with $\alpha_3(a_3)=0$. Then $\alpha_4\beta_3(a_3)=\beta_3'\alpha_3(a_3)=0$, so $\beta_3(a_3)=0$ by injectivity of $\alpha_4$, and exactness gives $a_3=\beta_2(a_2)$ for some $a_2 \in A_2$. Now $\beta_2'\alpha_2(a_2)=\alpha_3\beta_2(a_2)=\alpha_3(a_3)=0$, so $\alpha_2(a_2) \in \ker\beta_2'=\operatorname{im}\beta_1'$, say $\alpha_2(a_2)=\beta_1'(b_1)$. By surjectivity of $\alpha_1$ write $b_1=\alpha_1(a_1)$; then $\alpha_2(a_2)=\beta_1'\alpha_1(a_1)=\alpha_2\beta_1(a_1)$, so $a_2=\beta_1(a_1)$ by injectivity of $\alpha_2$, and $a_3=\beta_2\beta_1(a_1)=0$ by exactness. Hence $\alpha_3$ is injective.

Surjectivity. Suppose $\alpha_2,\alpha_4$ surjective and $\alpha_5$ injective. Let $b_3 \in B_3$. Since $\alpha_4$ is surjective there is $a_4 \in A_4$ with $\beta_3'(b_3)=\alpha_4(a_4)$. Then $\alpha_5\beta_4(a_4)=\beta_4'\alpha_4(a_4)=\beta_4'\beta_3'(b_3)=0$, so $\beta_4(a_4)=0$ by injectivity of $\alpha_5$, and exactness gives $a_4=\beta_3(a_3')$ for some $a_3' \in A_3$. Now $\beta_3'(b_3-\alpha_3(a_3'))=\beta_3'(b_3)-\beta_3'\alpha_3(a_3')=\alpha_4(a_4)-\alpha_4\beta_3(a_3')=0$, so $b_3-\alpha_3(a_3') \in \ker\beta_3'=\operatorname{im}\beta_2'$, say $b_3-\alpha_3(a_3')=\beta_2'(b_2)$. By surjectivity of $\alpha_2$ write $b_2=\alpha_2(a_2)$; then $b_3-\alpha_3(a_3')=\beta_2'\alpha_2(a_2)=\alpha_3\beta_2(a_2)$, so $b_3=\alpha_3(a_3'+\beta_2(a_2))$. Hence $\alpha_3$ is surjective. $\square$

### The Short Five Lemma

The case that is used most often takes both rows short exact.

**Corollary (short five).** Let

$$
0 \xrightarrow{\ \ } A \xrightarrow{\ \ } B \xrightarrow{\ \ } C \xrightarrow{\ \ } 0, \qquad 0 \xrightarrow{\ \ } A' \xrightarrow{\ \ } B' \xrightarrow{\ \ } C' \xrightarrow{\ \ } 0
$$

be short exact sequences, with maps $\alpha:A \to A'$, $\beta:B \to B'$ and $\gamma:C \to C'$ commuting with them. If $\alpha$ and $\gamma$ are isomorphisms then $\beta$ is an isomorphism; and if $\alpha$ is injective and $\gamma$ is surjective then $\beta$ is injective, while if $\alpha$ is surjective and $\gamma$ is injective then $\beta$ is surjective.

*Proof.* This is the five lemma with the outer terms zero: the two extra entries of a five-term row are the zero modules, whose maps are isomorphisms. $\square$

The short five lemma is the precise sense in which a short exact sequence determines its middle term up to isomorphism from its two ends, once the inclusions and projections are fixed. It does *not* say that the middle term is determined by the ends alone; the sequence $0 \to \mathbb{Z} \xrightarrow{\cdot 2} \mathbb{Z} \to \mathbb{Z}/2\mathbb{Z} \to 0$ shows otherwise.

## Splitting

### Sections and Retractions

Let $0 \to A \xrightarrow{i} B \xrightarrow{q} C \to 0$ be a short exact sequence.

**Definition.** A **section** of the sequence is a map $s:C \to B$ with $q \circ s=\operatorname{id}_C$. A **retraction** is a map $r:B \to A$ with $r \circ i=\operatorname{id}_A$.

A section is a choice, for each element of $C$, of a lift in $B$ depending linearly on the element; a retraction is a linear way of reading off the $A$-component. Existence of either is a strong condition.

**Lemma.** If a section or a retraction exists, then $i$ has image a direct summand of $B$ and $B \cong A \oplus C$ compatibly with $i$ and $q$; the sequence is then said to **split**.

### The Splitting Lemma

**Lemma (splitting).** For a short exact sequence $0 \to A \xrightarrow{i} B \xrightarrow{q} C \to 0$ the following are equivalent: (i) there is a section $s$; (ii) there is a retraction $r$; (iii) $B \cong A \oplus C$ with $i$ the inclusion of the first summand and $q$ the projection onto the second.

*Proof.* (i) $\Rightarrow$ (iii): define $\varphi:A \oplus C \to B$ by $\varphi(a,c)=i(a)+s(c)$. It is $R$-linear. If $\varphi(a,c)=0$, applying $q$ gives $c=0$, and then $i(a)=0$ gives $a=0$; so $\varphi$ is injective. For surjectivity, given $b \in B$, put $c=q(b)$ and $b'=b-s(c)$; then $q(b')=0$, so $b'=i(a)$ for a unique $a \in A$, and $b=\varphi(a,c)$. Thus $\varphi$ is an isomorphism. (iii) $\Rightarrow$ (i) and (iii) $\Rightarrow$ (ii): in the direct sum the map $c \mapsto (0,c)$ is a section and $(a,c)\mapsto a$ is a retraction. (ii) $\Rightarrow$ (iii): define $\psi:B \to A\oplus C$ by $\psi(b)=(r(b),q(b))$ and check injectivity and surjectivity by the same computation as above with the roles exchanged. $\square$

The splitting of the sequence is equivalent to the existence of an idempotent endomorphism of $B$ with image $i(A)$, namely $i \circ r$ or $\operatorname{id}_B-s\circ q$; this is the idempotent criterion for a direct summand met in the first article of the category.

**Examples.** Every short exact sequence of vector spaces splits, because a subspace always has a complement: choose a basis of $i(A)$ and extend it. Over $\mathbb{Z}$ the sequence $0 \to \mathbb{Z} \xrightarrow{\cdot 2} \mathbb{Z} \to \mathbb{Z}/2\mathbb{Z} \to 0$ does not split, since a section would give an element $c$ of $\mathbb{Z}$ with $2c=1$, impossible. More generally, a short exact sequence over a general ring need not split, and the obstruction to splitting is measured by $\operatorname{Ext}^1$ below.

## Exactness of $\operatorname{Hom}$

### The Functor $\operatorname{Hom}_R(M,-)$

Fix a module $M$. For each module $N$ the set $\operatorname{Hom}_R(M,N)$ is an $R$-module under pointwise operations, and a map $f:N \to N'$ induces $f_*:\operatorname{Hom}_R(M,N) \to \operatorname{Hom}_R(M,N')$, $f_*(h)=f \circ h$, making $\operatorname{Hom}_R(M,-)$ a functor to $R$-modules. It is additive: $(f+f')_*=f_*+f'_*$.

**Theorem.** The functor $\operatorname{Hom}_R(M,-)$ is **left exact**: if $0 \to A \xrightarrow{f} B \xrightarrow{g} C$ is exact then

$$
0 \longrightarrow \operatorname{Hom}_R(M,A) \xrightarrow{f_*} \operatorname{Hom}_R(M,B) \xrightarrow{g_*} \operatorname{Hom}_R(M,C)
$$

is exact.

*Proof.* If $f_*(h)=0$ then $f \circ h=0$; since $f$ is injective, $h=0$, so $f_*$ is injective. Next, $g_* f_*=(g \circ f)_*=0$, so $\operatorname{im} f_* \subseteq \ker g_*$. Conversely, let $h \in \operatorname{Hom}_R(M,B)$ with $g \circ h=0$. Then $\operatorname{im} h \subseteq \ker g=\operatorname{im} f$, and since $f$ is injective the map $f^{-1}:\operatorname{im} f \to A$ is a well-defined homomorphism; the composite $f^{-1} \circ h$ is an element of $\operatorname{Hom}_R(M,A)$ with $f_*(f^{-1}h)=h$. So $\ker g_* \subseteq \operatorname{im} f_*$. $\square$

Left exactness here is exactly the statement that $\operatorname{Hom}_R(M,-)$ preserves kernels. It does not in general preserve cokernels: applying it to $0 \to \mathbb{Z} \xrightarrow{\cdot 2} \mathbb{Z} \to \mathbb{Z}/2\mathbb{Z} \to 0$ with $M=\mathbb{Z}/2\mathbb{Z}$ gives

$$
0 \longrightarrow \operatorname{Hom}(\mathbb{Z}/2\mathbb{Z},\mathbb{Z}) \longrightarrow \operatorname{Hom}(\mathbb{Z}/2\mathbb{Z},\mathbb{Z}) \longrightarrow \operatorname{Hom}(\mathbb{Z}/2\mathbb{Z},\mathbb{Z}/2\mathbb{Z}),
$$

and the last map is not surjective, because the two left groups are zero while $\operatorname{Hom}(\mathbb{Z}/2\mathbb{Z},\mathbb{Z}/2\mathbb{Z}) \cong \mathbb{Z}/2\mathbb{Z}$ contains the identity. The failure is measured by $\operatorname{Ext}^1_R(M,-)$.

### Exactness in the First Variable

The same argument applied to the contravariant functor $\operatorname{Hom}_R(-,N)$ gives the dual statement.

**Theorem.** $\operatorname{Hom}_R(-,N)$ is **left exact in the first variable**: if $A \xrightarrow{f} B \xrightarrow{g} C \to 0$ is exact then

$$
0 \longrightarrow \operatorname{Hom}_R(C,N) \xrightarrow{g^*} \operatorname{Hom}_R(B,N) \xrightarrow{f^*} \operatorname{Hom}_R(A,N)
$$

is exact.

*Proof.* Here $g^*(h)=h \circ g$ and $f^*(h)=h \circ f$. Injectivity of $g^*$ uses that $g$ is surjective: if $h \circ g=0$ then $h$ vanishes on $\operatorname{im} g=C$. The vanishing of $f^*g^*$ uses $gf=0$. For the reverse inclusion, let $h \in \operatorname{Hom}_R(B,N)$ with $h \circ f=0$; then $h$ factors through $B/\operatorname{im} f=B/\ker g \cong \operatorname{im} g=C$, so there is a well-defined $\bar h:C \to N$ with $\bar h \circ g=h$, that is $g^*(\bar h)=h$. $\square$

Combining the two variables, $\operatorname{Hom}_R(-,-)$ is left exact as a functor of either argument, and in a short exact sequence it produces the four-term exact sequence of the two statements. Exactness of $\operatorname{Hom}$ in both variables, without the loss of surjectivity, is the defining property of a projective first argument or an injective second argument.

## Exactness of the Tensor Product

The tensor product of modules is defined and developed; its exactness is recorded here because it is the companion asymmetry to the one just proved. Let $-\otimes_R M$ denote the functor $N \mapsto N \otimes_R M$.

**Theorem.** The functor $-\otimes_R M$ is **right exact**: if $A \xrightarrow{f} B \xrightarrow{g} C \to 0$ is exact then

$$
A \otimes_R M \xrightarrow{f \otimes \operatorname{id}} B \otimes_R M \xrightarrow{g \otimes \operatorname{id}} C \otimes_R M \longrightarrow 0
$$

is exact. It is not in general left exact.

*Proof.* This is proved in the article of this category on flatness and exactness, where the construction of the tensor product by generators and relations is available. $\square$

So $\operatorname{Hom}$ loses surjectivity and tensor loses injectivity, and the modules for which the loss does not occur are the injective and projective modules on one side and the flat modules on the other. The example $\mathbb{Z}/2\mathbb{Z} \otimes_{\mathbb{Z}} \mathbb{Z} \xrightarrow{\ \cdot 2\ } \mathbb{Z}/2\mathbb{Z} \otimes_{\mathbb{Z}} \mathbb{Z}$ is the zero map on $\mathbb{Z}/2\mathbb{Z}$, so tensoring the non-split sequence $0 \to \mathbb{Z} \xrightarrow{\cdot 2} \mathbb{Z} \to \mathbb{Z}/2\mathbb{Z} \to 0$ with $\mathbb{Z}/2\mathbb{Z}$ destroys injectivity.

## Extensions and $\operatorname{Ext}^1$

### Extensions

**Definition.** Two extensions $0 \to A \to E \to C \to 0$ and $0 \to A \to E' \to C \to 0$ of $C$ by $A$ are **equivalent** if there is an isomorphism $\varphi:E \to E'$ that is the identity on the submodule $A \subseteq E$ and induces the identity on the quotient $C$. By the short five lemma, any map $E \to E'$ commuting with the maps of the two sequences is automatically an isomorphism.

**Theorem.** Equivalence classes of extensions of $C$ by $A$ form an abelian group under the **Baer sum**, written $\operatorname{Ext}^1_R(C,A)$, in which the class of the split extension $E=A\oplus C$ is the identity. The construction of the Baer sum and the identification of this group with the first derived functor of $\operatorname{Hom}_R(C,-)$, computed from a projective resolution of $C$, are given in the article of this category on projective and injective modules.

Thus the failure of a short exact sequence to split is an element of $\operatorname{Ext}^1_R(C,A)$, and the sequence splits exactly when that element vanishes. A module $P$ is projective precisely when every extension of $P$ by $C$ splits for all $C$, and a module $I$ is injective precisely when every extension of $C$ by $I$ splits for all $C$; these are the characterisations used.

### The Long Exact Sequence

Applying $\operatorname{Hom}_R(M,-)$ to a short exact sequence $0 \to A \to B \to C \to 0$ and continuing past the four left exact terms produces the **long exact sequence**

$$
0 \to \operatorname{Hom}(M,A) \to \operatorname{Hom}(M,B) \to \operatorname{Hom}(M,C) \xrightarrow{\ \delta\ } \operatorname{Ext}^1(M,A) \to \operatorname{Ext}^1(M,B) \to \operatorname{Ext}^1(M,C) \to \cdots,
$$

whose connecting map $\delta$ is the snake-lemma map of the previous section. The same construction applied to $-\otimes_R M$ produces the long exact sequence of $\operatorname{Tor}$. The two long exact sequences are the computational engine of the homological part of this category.

## Summary

A sequence of modules is exact when at each module the image of the incoming map equals the kernel of the outgoing one. Exactness packages injectivity and surjectivity: $0 \to A \to B$ is exact exactly when the map is injective, $B \to C \to 0$ exactly when it is surjective, and a short exact sequence $0 \to A \xrightarrow{i} B \xrightarrow{q} C \to 0$ presents $B$ as an extension of $C$ by $A$ with $C \cong B/i(A)$. Every short exact sequence is, up to isomorphism, of the form $0 \to A \to B \to B/A \to 0$.

The snake lemma attaches to a commutative diagram with exact rows a connecting homomorphism $\ker c \to \operatorname{coker} a$ and an exact sequence joining the kernels to the cokernels, and it is the origin of every long exact sequence in the category. The five lemma, specialised to the short five lemma, says that in a map of short exact sequences the middle vertical map is injective, surjective or bijective according as the outer two are, so the isomorphism class of the middle is controlled by the two ends once the inclusions are fixed.

A short exact sequence splits exactly when it has a section, equivalently a retraction, equivalently when the middle module is the direct sum of the two ends compatibly with the maps. Every sequence of vector spaces splits; over $\mathbb{Z}$ the sequence $0 \to \mathbb{Z} \xrightarrow{\cdot 2} \mathbb{Z} \to \mathbb{Z}/2\mathbb{Z} \to 0$ does not. The functor $\operatorname{Hom}_R(M,-)$ is left exact and $\operatorname{Hom}_R(-,N)$ is left exact in the first variable, while $-\otimes_R M$ is right exact; each functor loses one half of exactness, and the modules for which the loss does not occur are projective, injective or flat. Extensions of $C$ by $A$ are classified by $\operatorname{Ext}^1_R(C,A)$, with the split extension as the identity, and continuing the half-exact functors past their exact range gives the long exact sequences that the rest of the category uses.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | commutative ring with identity $1 \neq 0$ unless stated otherwise |
| $M$, $N$, $A$, $B$, $C$ | modules, left unless stated |
| $\ker f$, $\operatorname{im} f$ | kernel and image of a homomorphism |
| $\operatorname{coker} f=N/\operatorname{im} f$, $\operatorname{coim} f=M/\ker f$ | cokernel and coimage |
| $0$ | the zero module; its only maps to or from any module are zero |
| $0 \to A \to B \to C \to 0$ | short exact sequence; $B$ an extension of $C$ by $A$ |
| $\operatorname{Hom}_R(M,N)$ | $R$-module of homomorphisms $M \to N$ |
| $f_*$, $f^*$ | post-composition and pre-composition by $f$ on $\operatorname{Hom}$ |
| $s$, $r$ | section $qs=\operatorname{id}_C$; retraction $ri=\operatorname{id}_A$ |
| $\partial$ | connecting homomorphism of the snake lemma |
| $\delta$ | connecting map of a long exact sequence |
| $\operatorname{Ext}^1_R(C,A)$ | group of extensions of $C$ by $A$ under Baer sum |
| $\operatorname{Tor}$ | derived functor of the tensor product, developed later |
| $\otimes_R$ | tensor product over $R$, developed elsewhere in this category |
| $\mathbb{Z}/n\mathbb{Z}$ | integers modulo $n$ |





## Further Reading

- M. F. Atiyah and I. G. Macdonald, *Introduction to Commutative Algebra* (Addison-Wesley, 1969), for exact sequences and the tensor–hom comparison in commutative algebra.
- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for the exactness conventions and the snake lemma.
- Henri Cartan and Samuel Eilenberg, *Homological Algebra* (Princeton University Press, 1956), for the origin of the diagram lemmas and of $\operatorname{Ext}$ and $\operatorname{Tor}$.
- David S. Dummit and Richard M. Foote, *Abstract Algebra* (Wiley, 3rd ed. 2004), for the splitting lemma and elementary examples.
- Thomas W. Hungerford, *Algebra* (Springer, 1974), for exact sequences, the five lemma and the snake lemma.
- Saunders Mac Lane, *Homology* (Springer, 1995), for the diagram chases and their categorical organisation.
- Joseph J. Rotman, *An Introduction to Homological Algebra* (Springer, 2nd ed. 2009), for the long exact sequences of $\operatorname{Ext}$ and $\operatorname{Tor}$.
- Charles A. Weibel, *An Introduction to Homological Algebra* (Cambridge University Press, 1994), for derived functors and the Baer sum.
